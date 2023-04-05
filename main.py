import RPi.GPIO as GPIO
import time
from PlantClass import Plant

# Setup section
PLANT_A_PUMP_PIN = 12
PLANT_B_PUMP_PIN = 16
PLANT_C_PUMP_PIN = 20
PLANT_D_PUMP_PIN = 21

PLANT_A_HUMSENSOR_PIN = 24
PLANT_B_HUMSENSOR_PIN = 25
PLANT_C_HUMSENSOR_PIN = 8
PLANT_D_HUMSENSOR_PIN = 7

plantA = Plant('A', PLANT_A_PUMP_PIN, PLANT_A_HUMSENSOR_PIN)
plantB = Plant('B', PLANT_B_PUMP_PIN, PLANT_B_HUMSENSOR_PIN)
plantC = Plant('C', PLANT_C_PUMP_PIN, PLANT_C_HUMSENSOR_PIN)
plantD = Plant('D', PLANT_D_PUMP_PIN, PLANT_D_HUMSENSOR_PIN)


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(plantA.pumpPin, GPIO.OUT)
GPIO.setup(plantB.pumpPin, GPIO.OUT)
GPIO.setup(plantC.pumpPin, GPIO.OUT)
GPIO.setup(plantD.pumpPin, GPIO.OUT)


plantA.updateLastWateringTime()
plantB.updateLastWateringTime()
plantC.updateLastWateringTime()
plantD.updateLastWateringTime()


# Main loop
while True:
    # Get data from the Internet section
    plantA.updateParameters()
    plantB.updateParameters()
    plantC.updateParameters()
    plantD.updateParameters()

    # Check conditions section and watering
    currentEpochTime = (int)(time.time())
    print("Current Time:", time.localtime(currentEpochTime))

    if (plantA.checkForWateringNeed(currentEpochTime)):
        plantA.watering()

    print("-----------------------")

    # Send information

    time.sleep(1)



GPIO.cleanup()
