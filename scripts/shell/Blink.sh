# Shell script para o artigo Como piscar um LED utilizando BananaPi e Python via SSH
# Henrique Otogami 28/01/2025

# Exportação do pino físico: 29 (GPIO 7)
$ sudo echo 7 > /sys/class/gpio/export

# Definição de direção do pino: saída (out)
$ sudo echo out > /sys/class/gpio/gpio7/direction

# Definição do valor de nível lógico: alto (1)
$ sudo echo 1 > /sys/class/gpio/gpio7/value

# Definição do valor de nível lógico: baixo (0)
$ sudo echo 0 > /sys/class/gpio/gpio7/value

# Consultar a direção do pino:
$ sudo cat /sys/class/gpio/gpio7/direction

# Consultar o valor do pino:
$ sudo cat /sys/class/gpio/gpio7/value