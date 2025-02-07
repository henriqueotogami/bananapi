import paho.mqtt.client as mqtt
import random
import sys
import os
import subprocess

# Henrique Otogami - 06/02/2025
# https://github.com/henriqueotogami/bananapi


# Configuração do cliente
client_api      = mqtt.CallbackAPIVersion.VERSION2
client_protocol = mqtt.MQTTv31
client_security = mqtt.ssl.PROTOCOL_TLS
client_username = "your_username_here"
client_password = "your_password_here"
client_url = "your_url_here"
client_port     = 8883

device_id       = f'bananapi-{random.randint(0,100)}'
# device_id       = "bananapi-77"
target_topic    = "bananapi"
topic_qos       = 0
# message         = "Enviando mensagem do script python"

# Callback para conexão
def on_connect(client, userdata, flags, rc):
    message = "Conectado ao broker! Código de retorno: " + str(rc)
    print(message)
    client.subscribe(target_topic)

# Callback para mensagens recebidas
def on_message(client, userdata, msg):
    message = 'Mensagem recebida no tópico ' + str(msg.topic) + ': ' + str(msg.payload.decode())
    print(message)

# Inicio da conexão com o cliente MQTT
# ============================
client = mqtt.Client(client_api, client_id = device_id)
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(tls_version = client_security)
client.username_pw_set(client_username, client_password)

connection  = client.connect(host = client_url, port = client_port)
# ============================
# Fim da conexão com o cliente MQTT

print("\nMQTT - Publisher - Início")
print("\nDevice ID = "  + str(device_id))
print("\nTopic = "      + str(target_topic))
print("\nClient = "     + str(client.socket()))
print("\nConnection = " + str(connection))

# Identificação do sistema operacional
if(sys.platform == "linux"):
    print("\nLinux foi identificado")

    # Disponibilização do pino do LED para utilização
    os.system('sudo echo 7 > /sys/class/gpio/export')
    os.system('sudo echo out > /sys/class/gpio/gpio7/direction')

    while(True):
        # Usuário informa se vai acender ou apagar o LED ou se vai sair do loop
        switch_led = input("Turn on (1) / off (0) LED = ")

        if(switch_led == "quit"): break

        # Formatação do comando shell para acender ou apagar o LED
        turn_on_or_off = "1" if switch_led == "1" else "0"
        set_gpio7_value = 'sudo echo ' + str(turn_on_or_off) + ' > /sys/class/gpio/gpio7/value'
        os.system(set_gpio7_value)

        # Consulta do estado do LED para notificar o cliente do MQTT
        get_gpio7_value = 'sudo cat /sys/class/gpio/gpio7/value'
        try:
            # Armazena o estado do LED
            is_led_on_or_off = subprocess.check_output(get_gpio7_value, shell=True, text=True).strip()
            print("O valor do GPIO7 é: " + is_led_on_or_off)
        except subprocess.CalledProcessError as e:
            print("Erro ao executar o comando")

        # Formatação da mensagem para o Broker
        message_to_broker = "led on" if is_led_on_or_off == "1" else "led off"

        # Envio da mensagem e Resposta do Broker
        answer = client.publish(topic = target_topic, payload = message_to_broker, qos = topic_qos, retain = True)

        print("\nMensagem para o Broker = " + message_to_broker)
        print("\nMensagem foi publicada no Broker = " + str(answer.is_published()))
        print("\nMensagem enviada com sucesso para o Broker!")
else:
    print("\nSistema operacional = " + sys.platform)
    print("\nImplementação suporta apenas o Linux")    

print("\nMQTT - Publisher - Fim")