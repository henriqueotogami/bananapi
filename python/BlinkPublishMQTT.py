import paho.mqtt.client as mqtt
import random
import sys
import os
import subprocess

# Henrique Otogami - 06/02/2025
# https://github.com/henriqueotogami/bananapi

# ================================================================
# Configuração do cliente
client_api      = mqtt.CallbackAPIVersion.VERSION2
client_protocol = mqtt.MQTTv31
client_security = mqtt.ssl.PROTOCOL_TLS
client_username = "henriqueotogami"
client_password = "foxveb-medzyN-4faqsu"
client_url = "a8e2e0370f1440c98baa28fb14edc0d0.s1.eu.hivemq.cloud"
client_port     = 8883
device_id       = f'bananapi-{random.randint(0,100)}'
target_topic    = "bananapi"
topic_qos       = 0
# ================================================================

def on_connect(client, userdata, flags, rc):
    """Callback para conexão"""
    message = "Conectado ao broker! Código de retorno: " + str(rc)
    print(message)
    client.subscribe(target_topic)
 
# ================================================================

def on_message(client, userdata, msg):
    """Callback para mensagens recebidas"""
    message = 'Mensagem recebida no tópico ' + str(msg.topic) + ': ' + str(msg.payload.decode())
    print(message)

# ================================================================

def start_client() -> mqtt.Client:
    """Inicia a configuração do cliente do protocolo MQTT"""
    client = mqtt.Client(client_api, client_id = device_id)
    client.on_connect = on_connect
    client.on_message = on_message
    client.tls_set(tls_version = client_security)
    client.username_pw_set(client_username, client_password)
    return client

# ================================================================

def print_header(device_id, target_topic, client, connection):
    """Imprime o cabeçalho com as informações de conexão"""
    print("\nMQTT - Publisher - Início")
    print("\nDevice ID = "  + str(device_id))
    print("\nTopic = "      + str(target_topic))
    print("\nClient = "     + str(client.socket()))
    print("\nConnection = " + str(connection))

# ================================================================

def export_gpio():
    """
    Consulta a disponibilidade do pino de GPIO7 com base na leitura da direção do pino.

    Se o pino não está disponível, tenta fazer a exportação dele.
    """
    # Consulta a direção do pino GPIO 7
    get_gpio7_direction = 'direction'
    error_message = "\nErro ao ler a direção do pino GPIO7"
    gpio7_direction = read_gpio(get_gpio7_direction, error_message)

    # Verificação da disponibilização do pino GPIO7
    if(gpio7_direction == "NONE"): 
        print("\nPino não disponível para uso")
    else:
        # Disponibilização do pino do LED para utilização
        os.system('sudo echo 7 > /sys/class/gpio/export')
        os.system('sudo echo out > /sys/class/gpio/gpio7/direction')
        print("\nPino agora exportado e disponível para uso")

# ================================================================

def switch_gpio(switch_led):
    """Realiza o acionamento do pino de GPIO7 para ligar ou desligar o LED."""
    # Formatação do comando shell para acender ou apagar o LED
    turn_on_or_off = "1" if switch_led == "1" else "0"
    set_gpio7_value = 'sudo echo ' + str(turn_on_or_off) + ' > /sys/class/gpio/gpio7/value'
    os.system(set_gpio7_value)

# ================================================================

def read_gpio(target, error_message) -> str:
    """
    Realiza a leitura do pino de GPIO7.
    
    Se a leitura falhar, retorna o valor padrão NONE.
    """
    read_gpio7 = "NONE"
    get_gpio7 = 'sudo cat /sys/class/gpio/gpio7/' + target
    try:
        read_gpio7 = subprocess.check_output(get_gpio7, shell=True, text=True).strip()
        print("\nO valor do GPIO7 é: " + read_gpio7)
    except subprocess.CalledProcessError as e:
        print(error_message)
    finally:
        return read_gpio7

# ================================================================
        
def send_and_read_message(client, is_led_on_or_off):
    """
    Envia a mensagem para o Broker, informando se o LED está ligado ou desligado.
    
    Imprime se a mensagem de resposta, informando se foi publicada no Broker.
    """
    # Formatação da mensagem para o Broker
    message_to_broker = "led on" if is_led_on_or_off == "1" else "led off"

    # Envio da mensagem e Resposta do Broker
    answer = client.publish(topic = target_topic, payload = message_to_broker, qos = topic_qos, retain = True)

    print("\nMensagem para o Broker = " + message_to_broker)
    print("\nMensagem foi publicada no Broker = " + str(answer.is_published()))
    print("\nMensagem enviada com sucesso para o Broker!")

# ================================================================

def main():
    """
    Método principal para ligar ou desligar um led e notificar o Broker HiveMQ no protocolo MQTT.
    
    Pino utilizado = 29 (físico) ou GPIO7 (virtual)
    
    Entradas:
    - Ligar LED = 1
    - Desligar LED = 0
    - Encerrar script = quit
    """
    client = start_client()
    connection = client.connect(host = client_url, port = client_port)
    print_header(device_id, target_topic, client, connection)

    # Identificação do sistema operacional
    if(sys.platform == "linux"):
        print("\nLinux foi identificado")
        export_gpio()
            
        while(True):
            # Usuário informa se vai acender ou apagar o LED ou se vai sair do loop
            print("\nDigite 1 (ligar LED) | 0 (desligar LED) | quit (encerrar)")
            switch_led = input("Entrada = ")
            if(switch_led == "quit"): break
            switch_gpio(switch_led)

            # Consulta do estado do LED para notificar o cliente do MQTT
            get_gpio7_value = 'value'
            error_message="\nErro ao ler o estado do pino do GPIO7"
            is_led_on_or_off = read_gpio(get_gpio7_value, error_message)

            send_and_read_message(client, is_led_on_or_off)
    else:
        print("\nSistema operacional = " + sys.platform)
        print("\nImplementação suporta apenas o Linux")    

    print("\nMQTT - Publisher - Fim")

# ============================================================================
# Se o código for executado diretamente -> __name__ será "__main__"
# Se o código for importado em outro módulo -> __name__ será o nome do arquivo
if __name__ == "__main__":
    main()