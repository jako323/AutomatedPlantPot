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


# Main loop
while True:
    # Get data from the Internet section
    plantA.updateParameters()
    plantB.updateParameters()
    plantC.updateParameters()
    plantD.updateParameters()

    # Check conditions section and watering
    currentTime = (time.localtime()[2], time.localtime()[3], time.localtime()[4])
    
    # Send information
    time.sleep(2)



GPIO.cleanup()
