import paho.mqtt.client as mqtt
import random
import sys
import subprocess
import os
import time
from dotenv   import load_dotenv
from datetime import datetime

# Henrique Otogami - 06/02/2025
# https://github.com/henriqueotogami/bananapi

# ================================================================

class BlinkPublishMQTT:

    def __init__(self):
        self.client          = None
        self.client_username = None
        self.client_password = None
        self.client_url      = None
        self.client_port     = 8883
        self.device_id       = f'bananapi-{random.randint(0,100)}'
        self.target_topic    = "bananapi"
        self.topic_qos       = 0
        self.client_api      = mqtt.CallbackAPIVersion.VERSION2
        self.client_protocol = mqtt.MQTTv31
        self.client_security = mqtt.ssl.PROTOCOL_TLS

# ================================================================

    def start_client(self) -> mqtt.Client:
        """Inicia a configuração do cliente do protocolo MQTT"""

        load_dotenv()
        
        self.client_username = os.getenv("MQTT_CLIENT_USERNAME")
        self.client_password = os.getenv("MQTT_CLIENT_PASSWORD")
        self.client_url      = os.getenv("MQTT_CLIENT_URL")

        self.client = mqtt.Client(self.client_api, client_id = self.device_id)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.tls_set(tls_version = self.client_security)
        self.client.username_pw_set(self.client_username, self.client_password)
        return self.client

# ================================================================

    def on_connect(self, client, userdata, flags, rc):
        """Callback para conexão"""
        message = "Conectado ao broker! Código de retorno: " + str(rc)
        print(message)
        client.subscribe(self.target_topic)
 
# ================================================================

    def on_message(self, client, userdata, msg):
        """Callback para mensagens recebidas"""
        message = 'Mensagem recebida no tópico ' + str(msg.topic) + ': ' + str(msg.payload.decode())
        print(message)

# ================================================================

    def print_header(self, device_id, target_topic, client, connection):
        """Imprime o cabeçalho com as informações de conexão"""
        print("\nMQTT - Publisher - Início | " + datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        print("\nDevice ID = "  + str(device_id))
        print("\nTopic = "      + str(target_topic))
        print("\nClient = "     + str(client.socket()))
        print("\nConnection = " + str(connection))

# ================================================================

    def export_gpio(self) -> bool:
        """
        Consulta a disponibilidade do pino de GPIO7 com base na leitura da direção do pino.

        Se o pino não está disponível, tenta fazer a exportação dele.
        """
        # Consulta a direção do pino GPIO 7
        get_gpio7_direction = 'direction'
        error_message = "\nErro ao ler a direção do pino GPIO7"
        gpio7_direction = self.read_gpio(get_gpio7_direction, error_message)
        print("\nGPIO7 direction = " + gpio7_direction)

        # Verificação da disponibilização do pino GPIO7
        is_already_gpio_exported = gpio7_direction != "NONE"
        if(is_already_gpio_exported): 
            print("\nPino exportado anteriormente")
            self.unexport_gpio()
        
        # Por alguma razão, mesmo deportando a gpio, parece que ela fica presa
        # Testei valores dentro desse intervalo de 20 retentativas
        # E não achei um valor aceitável de retentativas
        retries = range(0,20)
        # Disponibilização do pino do LED para utilização
        for index in retries:
            try:
                # Devido a problemas de permissões, o redirecionamento (">") finaliza antes do comando "sudo" de fato exportar o pino
                subprocess.run("sudo echo 7 > tmp", shell = True, check=True)
                subprocess.run("sudo cp tmp /sys/class/gpio/export", shell = True, check=True)

                subprocess.run("sudo echo out > tmp", shell = True, check=True)
                subprocess.run("sudo cp tmp /sys/class/gpio/gpio7/direction", shell = True, check=True)
                print("\nPino agora exportado e disponível para uso")
                return True
            except subprocess.CalledProcessError as exception:
                print(f"\nException : {exception}")
                print("\nFalha na exportação do pino de GPIO7. Retentativa = " + str(index))
                time.sleep(1)
                self.unexport_gpio()
                time.sleep(1)
                if(index > 20): 
                    print("\nRetentativas excedidas")
                    return False
            except Exception as exception:
                print(f"\nErro inesperado : {exception}")

        return False


# ================================================================

    def switch_gpio(self, switch_led):
        """Realiza o acionamento do pino de GPIO7 para ligar ou desligar o LED."""
        # Formatação do comando shell para acender ou apagar o LED
        turn_on_or_off = "1" if switch_led == "1" else "0"
        set_gpio7_value = 'sudo echo ' + str(turn_on_or_off) + ' > /sys/class/gpio/gpio7/value'
        try:
            subprocess.run(set_gpio7_value, shell=True, check=True)
        except subprocess.CalledProcessError as exception:
            print("\nFalha no acionamento do pino de GPIO7")
        except Exception as exception:
            print(f"\nErro inesperado : {exception}")

# ================================================================

    def read_gpio(self, target, error_message) -> str:
        """
        Realiza a leitura do pino de GPIO7.
        
        Se a leitura falhar, retorna o valor padrão NONE.
        """
        read_gpio7 = "NONE"
        get_gpio7 = 'sudo cat /sys/class/gpio/gpio7/' + target
        try:
            read_gpio7 = subprocess.check_output(get_gpio7, shell=True, text=True).strip()
            print("\nO valor do GPIO7 é: " + read_gpio7)
        except subprocess.CalledProcessError as exception:
            print(error_message)
        except Exception as exception:
            print(f"\nErro inesperado : {exception}")
        finally:
            return read_gpio7

# ================================================================
        
    def send_and_read_message(self, client, is_led_on_or_off):
        """
        Envia a mensagem para o Broker, informando se o LED está ligado ou desligado.
        
        Imprime se a mensagem de resposta, informando se foi publicada no Broker.
        """
        # Formatação da mensagem para o Broker
        message_to_broker = "led on" if is_led_on_or_off == "1" else "led off"
        message_to_broker = message_to_broker + str(" | ") + datetime.now().strftime("%Y-%m-%d %H:%M %p")

        # Envio da mensagem e Resposta do Broker
        answer = client.publish(topic = self.target_topic, payload = message_to_broker, qos = self.topic_qos, retain = True)

        print("\nMensagem para o Broker = " + message_to_broker)
        print("\nMensagem foi publicada no Broker = " + str(answer.is_published()))
        print("\nMensagem enviada com sucesso para o Broker!")

# ================================================================

    def unexport_gpio(self):
        """Deporta o pino do GPIO7"""
        # Disponibilização do pino do LED para utilização
        try:
            subprocess.run('sudo echo 7 > /sys/class/gpio/unexport', shell=True, check=True)
            print("\nPino deportado e indisponível para uso")
        except subprocess.CalledProcessError as exception:
            print("\nFalha na deportação do pino de GPIO7")
        except Exception as exception:
            print(f"\nErro inesperado : {exception}")

# ============================================================================
    def run_bananapi(self, blink, client):
        """Inicia o gerenciamento de GPIO da Bananapi"""
        message_start_system = "Iniciando sistema | " + datetime.now().strftime("%Y-%m-%d %H:%M %p")
        client.publish(topic = self.target_topic, payload = message_start_system, qos = self.topic_qos, retain = True)
            
        is_exported_gpio = blink.export_gpio()
        if(is_exported_gpio == False):
            print("\nEncerrando sistema. Equipamento sem acesso a GPIO.")
            return

        get_gpio7_direction = 'direction'
        error_message = "\nErro ao ler a direção do pino GPIO7"
        gpio7_direction = blink.read_gpio(get_gpio7_direction, error_message)
        print("\nGPIO7 direction = " + gpio7_direction)
            
        while(True):
            # Usuário informa se vai acender ou apagar o LED ou se vai sair do loop
            print("\nDigite 1 (ligar LED) | 0 (desligar LED) | quit (encerrar)")
            switch_led = input("Entrada = ")
            if(switch_led == "quit"): break

            blink.switch_gpio(switch_led)

            # Consulta do estado do LED para notificar o cliente do MQTT
            get_gpio7_value = 'value'
            error_message="\nErro ao ler o estado do pino do GPIO7"
            is_led_on_or_off = blink.read_gpio(get_gpio7_value, error_message)

            blink.send_and_read_message(client, is_led_on_or_off)


        blink.unexport_gpio()

# ============================================================================

# Se o código for executado diretamente -> __name__ será "__main__"
# Se o código for importado em outro módulo -> __name__ será o nome do arquivo
if __name__ == "__main__":

    blink = BlinkPublishMQTT()
    client = blink.start_client()
    connection = client.connect(host = blink.client_url, port = blink.client_port) # type: ignore
    blink.print_header(blink.device_id, blink.target_topic, client, connection)

    # Identificação do sistema operacional
    if(sys.platform == "linux"):
        print("\nLinux foi identificado")
        blink.run_bananapi(blink, client)
    else:
        print("\nSistema operacional = " + sys.platform)
        print("\nImplementação suporta apenas o Linux")

    
    message_finish_system = "Finalizando sistema | " + datetime.now().strftime("%Y-%m-%d %H:%M %p")
    client.publish(topic = blink.target_topic, payload = message_finish_system, qos = blink.topic_qos, retain = True)
    print("\nMQTT - Publisher - Fim | " + datetime.now().strftime("%Y-%m-%d %H:%M %p"))

# ============================================================================