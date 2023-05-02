import RPi.GPIO as GPIO
import time

import pinout
from PlantClass import Plant
import waterLevelSensor


# === INITIALIZING PLANTS ===
plantA = Plant('A', pinout.PLANT_A_PUMP_PIN, pinout.PLANT_A_HUMSENSOR_SPI_CHANNEL)
plantB = Plant('B', pinout.PLANT_B_PUMP_PIN, pinout.PLANT_B_HUMSENSOR_SPI_CHANNEL)
plantC = Plant('C', pinout.PLANT_C_PUMP_PIN, pinout.PLANT_C_HUMSENSOR_SPI_CHANNEL)
plantD = Plant('D', pinout.PLANT_D_PUMP_PIN, pinout.PLANT_D_HUMSENSOR_SPI_CHANNEL)
plantA.updateLastWateringTime()
plantB.updateLastWateringTime()
plantC.updateLastWateringTime()
plantD.updateLastWateringTime()


# === GPIO SETUP ===
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(plantA.pumpPin, GPIO.OUT)
GPIO.setup(plantB.pumpPin, GPIO.OUT)
GPIO.setup(plantC.pumpPin, GPIO.OUT)
GPIO.setup(plantD.pumpPin, GPIO.OUT)

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

    if (waterLevelSensor.isWaterInTank()):
        if (plantA.checkForWateringNeed(currentEpochTime)):
            plantA.watering()
        if (plantB.checkForWateringNeed(currentEpochTime)):
            plantB.watering()
        if (plantC.checkForWateringNeed(currentEpochTime)):
            plantC.watering()
        if (plantD.checkForWateringNeed(currentEpochTime)):
            plantD.watering()
    else:
        print("Water level in tank dropped below given treshold. All watering actions are suspended.")
        print("Please fill up the water compartment.")


    # === SENDING DATA TO THE INTERNET ===
    print("Current tank's water level: ", waterLevelSensor.readInPercentage(), "%", sep="")


    time.sleep(2.5)



#GPIO.cleanup()
