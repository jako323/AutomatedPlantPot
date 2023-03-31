import RPi.GPIO as GPIO
from time import *
from PlantClass import Plant


PLANT_A_PUMP_PIN = 12
PLANT_B_PUMP_PIN = 16
PLANT_C_PUMP_PIN = 20
PLANT_D_PUMP_PIN = 21

AUXILIARY_WATER_NOW_BUTTO_PIN = 25


plantA = Plant('A', 0, 0.5, 0, 0, 0, PLANT_A_PUMP_PIN)


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(plantA.pumpPin, GPIO.OUT)
GPIO.setup(AUXILIARY_WATER_NOW_BUTTO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if(plantA.checkForWateringNeed()):
        plantA.watering()
    sleep(1)


GPIO.cleanup()
