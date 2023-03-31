import RPi.GPIO as GPIO
from time import *
from PlantClass import Plant


PLANT_A_PUMP_PIN = 12
PLANT_B_PUMP_PIN = 16
PLANT_C_PUMP_PIN = 20
PLANT_D_PUMP_PIN = 21

plantA = Plant('A', 0, 0.5, 0, 0, 0, PLANT_A_PUMP_PIN)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(plantA.pumpPin, GPIO.OUT)

plantA.watering()
