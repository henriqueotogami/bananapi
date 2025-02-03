import paho.mqtt.client as mqtt
import random
import sys
import os

client_api      = mqtt.CallbackAPIVersion.VERSION2
client_protocol = mqtt.MQTTv31
client_security = mqtt.ssl.PROTOCOL_TLS
client_username = "your_username_here"
client_password = "your_password_here"
client_url = "your_url_here"
client_port     = 8883

# device_id       = f'bananapi-{random.randint(0,100)}'
devide_id       = "bananapi-77"
target_topic    = "bananapi"
topic_qos       = 0
# message         = "Enviando mensagem do script python"

# Callback para conexão
def on_connect(client, userdata, flags, rc):
    print(f"Conectado ao broker! Código de retorno: {rc}")
    client.subscribe(target_topic)  # Inscreve-se em um tópico

# Callback para mensagens recebidas
def on_message(client, userdata, msg):
    print(f"Mensagem recebida no tópico {msg.topic}: {msg.payload.decode()}")


client = mqtt.Client(client_api, client_id = device_id)
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(tls_version = client_security)
client.username_pw_set(client_username, client_password)

connection  = client.connect(host = client_url, port = client_port)

print("\nMQTT - Publish")
print("\nDevice ID = "  + str(device_id))
print("\nTopic = "      + str(target_topic))
print("\nClient = "     + str(client.socket()))
print("\nConnection = " + str(connection))

if(sys.platform == "linux"):
    print("\nLinux has found")

os.system('sudo echo 7 > /sys/class/gpio/export')
os.system('sudo echo out > /sys/class/gpio/gpio7/direction')

while(True):
    switch_led = input("Turn on (1) / off (0) LED = ")
    if(switch_led == "quit"): break

    turn_on_or_off = "1" if switch_led == "1" else "0"
    os.system(f'sudo echo {turn_on_or_off} > /sys/class/gpio/gpio7/value')

    is_led_on_or_off = os.system('sudo cat /sys/class/gpio/gpio7/value')
    message_to_broker = "led on" if is_led_on_or_off == "1" else "led off"

    print(message_to_broker)
    answer      = client.publish(topic = target_topic, payload = message_to_broker, qos = topic_qos, retain = True)
    print("\nAnswer = "     + str(answer.is_published()))
    print("\nMensagem enviada para o Broker!")

# client.loop_forever()
# sudo pip3 install paho-mqtt

# scp /Users/henriquematheusalvespereira/Documents/Github/bananapi/python/PublishMQTT.py pi@bananapi-zero.local:otogamidev/

# python3 -m pip install --upgrade pip
# sudo apt install python 3.10