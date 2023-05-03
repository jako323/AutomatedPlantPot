import RPi.GPIO as GPIO

def turnOn(pumpPin):
    print(" | Pump is on.")
    GPIO.output(pumpPin, GPIO.HIGH)

def turnOff(pumpPin):
    print(" | Pump is off.")
    GPIO.output(pumpPin, GPIO.LOW)