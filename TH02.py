#!/usr/bin/env python
# -*- coding: utf-8 -*-
import PyBCM2835

class TH02:
	ADDRESS	= 0x40
	CONFIG_REG = 0x03
	STATUS_REG = 0x00
	DATAH_REG = 0x01		
	DATAL_REG = 0x02
	ID_REG = 0x17
	ID = 0x90

	def readReg(self,register):
		data=""+chr(0)
		PyBCM2835.i2c_read_register_rs(chr(register),data,1)		
		return int(ord(data[0]))
	def writeReg(self,register,value):
		PyBCM2835.i2c_write(chr(register)+chr(value),2)		
	def startFastTempConversion(self):
		self.writeReg(CONFIG_REG,chr(0x11),1)
	def startFastHumidityConversion(self):
		self.writeReg(CONFIG_REG,chr(0x10),1)
	def setHeaterState(self,value):
		regValue = self.readReg(CONFIG_REG)
		if(value==1):
			regValue = regValue | 1<<1			
		self.writeReg(CONFIG_REG,chr(value),1)
	def readTemp(self):
		regValue = (self.readReg(DATAH_REG)<<8)|self.readReg(DATAL_REG)
		temp = (regValue / 32.0)-50
		return temp
	def readHumidity(self):
		regValue = (self.readReg(DATAH_REG)<<8)|self.readReg(DATAL_REG)
		humidity = (regValue / 16.0)-24
		return humidity
