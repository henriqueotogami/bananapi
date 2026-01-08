import os
import time

os.system('echo "bananapi - start blink"')
os.system('sudo echo 7 > /sys/class/gpio/export')
os.system('sudo echo out > /sys/class/gpio/gpio7/direction')
os.system('sudo cat /sys/class/gpio/gpio7/value')
os.system('sudo cat /sys/class/gpio/gpio7/direction')

for index in range(10):
    os.system('sudo echo "bananapi - pisca 1"')
    os.system('sudo echo 1 > /sys/class/gpio/gpio7/value')
    time.sleep(3)
    os.system('sudo echo "bananapi - pisca 2"')
    os.system('sudo echo 0 > /sys/class/gpio/gpio7/value')
    time.sleep(3)