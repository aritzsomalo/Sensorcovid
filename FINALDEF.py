import time
import RPi.GPIO as GPIO
import dht_config
from mfrc522 import SimpleMFRC522
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



def presencia():
  GPIO_PIR = 21
  GPIO.setup(GPIO_PIR,GPIO.IN)
  estado_presencia = GPIO.input(GPIO_PIR)
  return estado_presencia



def tarjeta():
  reader = SimpleMFRC522()
  id, text = reader.read()
  return id

def temperatura():
  GPIO_TEMP = 20
  GPIO.setup(GPIO_TEMP,GPIO.IN)
  sensor = dht_config.DHT(GPIO_TEMP)
  humi,temp = sensor.read()
  return temp



