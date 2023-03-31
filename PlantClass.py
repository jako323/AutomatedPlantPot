import RPi.GPIO as GPIO
from time import *

class Plant:
	def __init__(self, symbol, mode, waterAmount, wateringInterval, humidityThreshold, minWateringInterval, pumpPin):
		self.symbol = symbol
		self.mode = mode
		self.waterAmount = waterAmount
		self.wateringInterval = wateringInterval
		self.humidityThreshold = humidityThreshold
		self.minWateringInterval = minWateringInterval
		self.pumpPin = pumpPin
	

	def checkForWateringNeed(self):
		if (self.mode == 1):	# Manual mode	#TODO: Add conditions
			return True
		elif(self.mode == 2): #TODO: Add conditions
			return True
		elif(self.mode == 3):	#TODO: Add conditions
			return True
		else:
			print("The plant", self.symbol, "is turned off or wrong mode was declared.")
			return False


	def watering(self):
		print("The plant", self.symbol, "is now watered.")		
		self.pumpOn()
		wateringDuration = self.calculateWateringDuration()
		sleep(wateringDuration)
		self.pumpOff()


	def calculateWateringDuration(self):
		return self.waterAmount * 2


	def pumpOn(self):
		GPIO.output(self.pumpPin, GPIO.HIGH)
	

	def pumpOff(self):
		GPIO.output(self.pumpPin, GPIO.LOW)