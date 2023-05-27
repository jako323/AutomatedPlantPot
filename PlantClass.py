import time

import plantSetupInfo
import humiditySensor
import pump

class Plant:
	def __init__(self, symbol, pumpPin, humiditySensorSpiChannel):
		self.symbol = symbol
		self.pumpPin = pumpPin
		self.humiditySensorSpiChannel = humiditySensorSpiChannel

		self.mode = 0					# 0 - plant is off, 1 - manual mode, 2 - time interval mode, 3 - humidity control mode
		self.waterAmount = 0			# in ml, the converted to pump time duration
		self.wateringTime = 0			# time of scheduled watering
		self.humidityThreshold = 0		# in %
		self.minWateringInterval = 0	# in seconds

		self.updateLastScheduledDay()
		self.updateLastWateringTime()
	

	def updateParameters(self):
		self.mode = plantSetupInfo.PLANT_MODE[self.symbol]
		self.waterAmount = plantSetupInfo.PLANT_WATERAMOUNT[self.symbol]
		self.wateringTime = plantSetupInfo.PLANT_WATERINGTIME[self.symbol]
		self.humidityThreshold = plantSetupInfo.PLANT_HUMIDITYTRESHOLD[self.symbol]
		tempWateringInterval = plantSetupInfo.PLANT_MINWATERINGINTERVAL[self.symbol]
		self.minWateringInterval = tempWateringInterval[0] * 3600 + tempWateringInterval[1] * 60 + tempWateringInterval[2]
		# print("Plant", self.symbol, "parameters were updated.")


	def updateLastScheduledDay(self):
		self.lastScheduledDay = time.localtime()[2]
		print("Plant's", self.symbol, "last Scheduled Day was set to:", self.lastScheduledDay)


	def updateLastWateringTime(self):
		self.lastWateringEpochTime = (int)(time.time())
		print("Plant's", self.symbol, "last watering time was set to:", time.localtime(self.lastWateringEpochTime))


	def checkForWateringNeed(self, currentEpochTime):
		# Device Turned off
		if (self.mode == 0):
			print("Plant", self.symbol, "is turned off.")
			return False
		
		# Manual mode	#TODO: Add conditions
		elif (self.mode == 1):
			print("Plant ", self.symbol, " is running on mode ", self.mode, ".", sep='')
			return True
		
		# Time interval mode
		elif(self.mode == 2
       		and time.localtime(currentEpochTime)[2] != self.lastScheduledDay
			and time.localtime(currentEpochTime)[3] >= self.wateringTime[0]
			and time.localtime(currentEpochTime)[4] >= self.wateringTime[1]):
			print("Plant ", self.symbol, " is running on mode ", self.mode, ".", sep='')
			return True
		
		# Humidity control mode
		elif(self.mode == 3
       		and self.getHumidityLevel() < self.humidityThreshold
			and currentEpochTime >= (self.lastWateringEpochTime + self.minWateringInterval)):
			print("Plant ", self.symbol, " is running on mode ", self.mode, ".", sep='')
			return True
			
		else:
			print("Plant ", self.symbol, " doesn't need to be watered     (Current humidity level: ", humiditySensor.readInPercentage(self.humiditySensorSpiChannel), "%)", sep="")
			return False


	def watering(self):
		print(" | Plant", self.symbol, "is now watered.")		
		pump.turnOn(self.pumpPin)
		wateringDuration = self.calculateWateringDuration()
		time.sleep(wateringDuration)
		pump.turnOff(self.pumpPin)

		self.updateLastWateringTime()
		if (self.mode == 2):
			self.updateLastScheduledDay()


	def calculateWateringDuration(self):
		return self.waterAmount * 2
	

	def getHumidityLevel(self):		# TODO: Write code working with sensors.
		return humiditySensor.readInPercentage(self.humiditySensorSpiChannel)
	
