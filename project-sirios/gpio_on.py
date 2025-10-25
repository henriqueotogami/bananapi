#!/usr/bin/env python

print("Content-type: text/html\n")

import subprocess
import os

FNULL = open(os.devnull, 'w')

subprocess.call("echo 7 | sudo tee /sys/class/gpio/unexport", shell=True, stdout=FNULL, stderr=FNULL)
subprocess.call("echo 7 | sudo tee /sys/class/gpio/export", shell=True, stdout=FNULL, stderr=FNULL)
subprocess.call("echo out | sudo tee /sys/class/gpio/gpio7/direction", shell=True, stdout=FNULL, stderr=FNULL)
subprocess.call("echo 1 | sudo tee /sys/class/gpio/gpio7/value", shell=True, stdout=FNULL, stderr=FNULL)

print("LED LIGADO")