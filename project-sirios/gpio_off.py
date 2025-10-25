#!/usr/bin/env python

print("Content-type: text/html\n")

import subprocess
import os

FNULL = open(os.devnull, 'w')

subprocess.call("echo 0 | sudo tee /sys/class/gpio/gpio7/value", shell=True, stdout=FNULL, stderr=FNULL)

print("LED DESLIGADO")