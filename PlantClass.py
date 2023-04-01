import RPi.GPIO as GPIO
from time import *

from plantSetupInfo_dev import *

class Plant:
	def __init__(self, symbol, pumpPin, humiditySensorPin):
		self.symbol = symbol
		self.pumpPin = pumpPin
		self.humiditySensorPin = humiditySensorPin
		self.mode = 0					# 0 - plant is off, 1 - manual mode, 2 - strict time mode, 3 - time plus humidity measure mode, 4 - humidity measure mode
		self.waterAmount = 0			# in ml, the converted to pump time duration
		self.wateringTime = 0			# time of scheduled watering
		self.humidityThreshold = 0		# in %
		self.minWateringInterval = 0	# in hours
	

	def updateParameters(self):
		self.mode = PLANT_MODE[self.symbol]
		self.waterAmount = PLANT_WATERAMOUNT[self.symbol]
		self.wateringTime = PLANT_WATERINGTIME[self.symbol]
		self.humidityThreshold = PLANT_HUMIDITYTRESHOLD[self.symbol]
		self.minWateringInterval = PLANT_MINWATERINGINTERVAL[self.symbol]


	def checkForWateringNeed(self):
		if (self.mode == 1):	# Manual mode	#TODO: Add conditions
			return True
		elif(self.mode == 2):	# Time interval mode #TODO: Add conditions
			return True
		elif(self.mode == 3):	# Humidity control mode #TODO: Add conditions
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