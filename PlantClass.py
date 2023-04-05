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

		self.lastWateringEpochTime = (int)(time.time())
	

	def updateParameters(self):
		self.mode = plantSetupInfo.PLANT_MODE[self.symbol]
		self.waterAmount = plantSetupInfo.PLANT_WATERAMOUNT[self.symbol]
		self.wateringTime = plantSetupInfo.PLANT_WATERINGTIME[self.symbol]
		self.humidityThreshold = plantSetupInfo.PLANT_HUMIDITYTRESHOLD[self.symbol]
		tempWateringInterval = plantSetupInfo.PLANT_MINWATERINGINTERVAL[self.symbol]
		self.minWateringInterval = tempWateringInterval[0] * 3600 + tempWateringInterval[1] * 60 + tempWateringInterval[2]
		print("Plant", self.symbol, "parameters were updated.")


	def updateLastWateringTime(self):
		self.lastWateringEpochTime = (int)(time.time())
		print("Plant", self.symbol, "last watering time was set to:", time.localtime(self.lastWateringEpochTime))


	def checkForWateringNeed(self, currentEpochTime):
		# Device Turned off
		if (self.mode == 0):
			print("Plant", self.symbol, "is turned off.")
			return False
		# Manual mode	#TODO: Add conditions
		elif (self.mode == 1):
			return True
		# Time interval mode	#TODO: Add conditions
		elif(self.mode == 2):
			return True
		# Time interval + Humidity control mode	#TODO: Add conditions
		elif (self.mode == 3):
			return True
		# Humidity control mode
		elif(self.mode == 4
       		and self.getHumidityLevel() < self.humidityThreshold
			and currentEpochTime >= (self.lastWateringEpochTime + self.minWateringInterval)):
			print("Plant", self.symbol, "is running on mode 4.")
			return True
		else:
			print("Plant", self.symbol, "doesn't need to be watered.")
			return False


	def watering(self):
		print("Plant", self.symbol, "is now watered.")		
		self.pumpOn()
		wateringDuration = self.calculateWateringDuration()
		time.sleep(wateringDuration)
		self.pumpOff()
		self.updateLastWateringTime()


	def calculateWateringDuration(self):
		return self.waterAmount * 2


	def pumpOn(self):
		GPIO.output(self.pumpPin, GPIO.HIGH)
	

	def pumpOff(self):
		GPIO.output(self.pumpPin, GPIO.LOW)
	

	def getHumidityLevel(self):		# TODO: Write code working with sensors.
		# Read from sensor
		value = 10
		return value

