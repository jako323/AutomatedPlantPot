import RPi.GPIO as GPIO
import time

import plantSetupInfo

class Plant:
	def __init__(self, symbol, pumpPin, humiditySensorPin):
		self.symbol = symbol
		self.pumpPin = pumpPin
		self.humiditySensorPin = humiditySensorPin

		self.mode = 0					# 0 - plant is off, 1 - manual mode, 2 - time interval mode, 3 - time plus humidity control mode, 4 - humidity control mode
		self.waterAmount = 0			# in ml, the converted to pump time duration
		self.wateringTime = 0			# time of scheduled watering
		self.humidityThreshold = 0		# in %
		self.minWateringInterval = 0	# in hours

		self.lastWateringTime = (time.localtime()[2], time.localtime()[3], time.localtime()[4])	
	

	def updateParameters(self):
		self.mode = plantSetupInfo.PLANT_MODE[self.symbol]
		self.waterAmount = plantSetupInfo.PLANT_WATERAMOUNT[self.symbol]
		self.wateringTime = plantSetupInfo.PLANT_WATERINGTIME[self.symbol]
		self.humidityThreshold = plantSetupInfo.PLANT_HUMIDITYTRESHOLD[self.symbol]
		self.minWateringInterval = plantSetupInfo.PLANT_MINWATERINGINTERVAL[self.symbol]


	def updateLastWateringTime(self):
		self.lastWateringTime = (time.localtime()[2], time.localtime()[3], time.localtime()[4])


	def checkForWateringNeed(self, currentTime):
		if (self.mode == 1):	# Manual mode	#TODO: Add conditions
			return True
		elif(self.mode == 2):	# Time interval mode	#TODO: Add conditions
			return True
		elif (self.mode ==3):	# Time interval + Humidity control mode	#TODO: Add conditions
			return True
		elif(self.mode == 4):	# Humidity control mode	#TODO: Add conditions
			return True
		else:
			print("The plant", self.symbol, "is turned off or wrong mode was declared.")
			return False


	def watering(self):
		print("The plant", self.symbol, "is now watered.")		
		self.pumpOn()
		wateringDuration = self.calculateWateringDuration()
		time.sleep(wateringDuration)
		self.pumpOff()


	def calculateWateringDuration(self):
		return self.waterAmount * 2


	def pumpOn(self):
		GPIO.output(self.pumpPin, GPIO.HIGH)
	

	def pumpOff(self):
		GPIO.output(self.pumpPin, GPIO.LOW)

