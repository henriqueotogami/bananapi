import paho.mqtt.client as mqtt
import random

client_api = mqtt.CallbackAPIVersion.VERSION2
client_protocol = mqtt.MQTTv31
client_security = mqtt.ssl.PROTOCOL_TLS
client_username = "your_username_here"
client_password = "your_password_here"
client_url = "your_url_here"
client_port = 8883

device_id = f'bananapi-{random.randint(0,100)}'
target_topic = "bananapi"
topic_qos = 0
message = "Enviando mensagem do script python"

def on_connect(client, userdata, flags, rc):
    print(f"Conectado com código de resultado: {rc}")


client = mqtt.Client(client_api, client_id = device_id)
client.on_connect = on_connect
secure = client.tls_set(tls_version = client_security)
client.username_pw_set(client_username,client_password)
connection = client.connect(host = client_url, port = client_port)


print("Client = ")
print(client.socket())

print("Connection = ")
print(connection)

message = client.publish(topic = target_topic, payload = message, qos = topic_qos, retain = True)
print("Message = ")
print(message.is_published())

print("Mensagem enviada para o Broker!")

# client.loop_forever()
# sudo pip3 install paho-mqtt

# scp /Users/henriquematheusalvespereira/Documents/Github/bananapi/python/PublishMQTT.py pi@bananapi-zero.local:otogamidev/