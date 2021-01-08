import time
import RPi.GPIO as GPIO
import dht_config
from mfrc522 import SimpleMFRC522


GPIO.setmode(GPIO.BCM)

GPIO_PIR = 21
GPIO_TEMP = 20

print ("PIR Module basic test (CTRL-C to exit)")

GPIO.setwarnings(False)

# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)
GPIO.setup(GPIO_TEMP,GPIO.IN)

reader = SimpleMFRC522()
sensor = dht_config.DHT(GPIO_TEMP)

try:

    print ("Por favor espere")
    time.sleep(1)
    print ("Identifiquese con la tarjeta")
    id, text = reader.read()
    print(id)
    

  # Loop until users quits with CTRL-C
    while id == id :
      GPIO.setup(GPIO_PIR,GPIO.IN)
      GPIO.setup(GPIO_TEMP,GPIO.IN)
      time.sleep(2)
      estado_presencia = GPIO.input(GPIO_PIR)
      estado_temperatura = GPIO.input(GPIO_TEMP)
      print(estado_presencia)
      if estado_presencia == 1:
        print("Se detecta  presencia")
        time.sleep(1)
        humi,temp = sensor.read()
        print(temp,'ºC')
        print("Por favor espere")
        time.sleep(2)
        print(estado_temperatura)
        time.sleep(1)
      else :
        print("No hay presencia")
        time.sleep(2)
except KeyboardInterrupt:
        print("Quit")
  # Reset GPIO settings
GPIO.cleanup()