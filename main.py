#import RPi.GPIO as GPIO
import time

import pinout
from PlantClass import Plant


# === INITIALIZING PLANTS ===
plantA = Plant('A', pinout.PLANT_A_PUMP_PIN, pinout.PLANT_A_HUMSENSOR_PIN)
plantB = Plant('B', pinout.PLANT_B_PUMP_PIN, pinout.PLANT_B_HUMSENSOR_PIN)
plantC = Plant('C', pinout.PLANT_C_PUMP_PIN, pinout.PLANT_C_HUMSENSOR_PIN)
plantD = Plant('D', pinout.PLANT_D_PUMP_PIN, pinout.PLANT_D_HUMSENSOR_PIN)
plantA.updateLastWateringTime()
plantB.updateLastWateringTime()
plantC.updateLastWateringTime()
plantD.updateLastWateringTime()


# === GPIO SETUP ===
"""
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(plantA.pumpPin, GPIO.OUT)
GPIO.setup(plantB.pumpPin, GPIO.OUT)
GPIO.setup(plantC.pumpPin, GPIO.OUT)
GPIO.setup(plantD.pumpPin, GPIO.OUT)
"""

plantA.lastScheduledDay = 4

# === MAIN LOOP ===
while True:
    # === GETTING DATA FROM THE INTERNET ===
    plantA.updateParameters()
    plantB.updateParameters()
    plantC.updateParameters()
    plantD.updateParameters()

    # === WATERING ===
    currentEpochTime = (int)(time.time())
    print("Current Time:", time.localtime(currentEpochTime))

    if (plantA.checkForWateringNeed(currentEpochTime)):
        plantA.watering()
    if (plantB.checkForWateringNeed(currentEpochTime)):
        plantB.watering()
    if (plantC.checkForWateringNeed(currentEpochTime)):
        plantC.watering()
    if (plantD.checkForWateringNeed(currentEpochTime)):
        plantD.watering()

    # === SENDING INFORMATION TO THE INTERNET ===


    time.sleep(1)



#GPIO.cleanup()
