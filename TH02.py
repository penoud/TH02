#!/usr/bin/env python
# -*- coding: utf-8 -*-
import PyBCM2835

class TH02:
        ADDRESS = 0x40
        CONFIG_REG = 0x03
        STATUS_REG = 0x00
        DATAH_REG = 0x01
        DATAL_REG = 0x02
        ID_REG = 0x17
        ID = 0x90

        def __init__(self):
                if not (PyBCM2835.init()):
                        raise EnvironmentError("Cannot initialize BCM2835.")
                PyBCM2835.i2c_begin()
        def writeReg(self,register,value):
                PyBCM2835.i2c_setSlaveAddress(self.ADDRESS)
                PyBCM2835.i2c_write(chr(register)+chr(value),2)
        def readReg(self,register):
                PyBCM2835.i2c_setSlaveAddress(self.ADDRESS)
                data=""+chr(0)
                PyBCM2835.i2c_read_register_rs(chr(register),data,1)
                return data
        def startFastTempConversion(self):
                self.writeReg(self.CONFIG_REG,0x31)
                PyBCM2835.delay(19)
        def startFastHumidityConversion(self):
                self.writeReg(self.CONFIG_REG,0x30)
                PyBCM2835.delay(19)
        def startTempConversion(self):
                self.writeReg(self.CONFIG_REG,0x11)
                PyBCM2835.delay(36)
        def startHumidityConversion(self):
                self.writeReg(self.CONFIG_REG,0x10)
                PyBCM2835.delay(36)
        def setHeaterState(self,value):
                regValue = self.readReg(self.CONFIG_REG)
                if(value==1):
                        regValue = regValue | 1<<1
                self.writeReg(self.CONFIG_REG,chr(value),1)
        def readTemp(self):
                datah = ord(self.readReg(self.DATAH_REG))
                datal = ord(self.readReg(self.DATAL_REG))
                regValue = (datah<<6) | (datal>>2)
                temp = (regValue / 32.0)-50
                return temp
        def readHumidity(self):
                datah = ord(self.readReg(self.DATAH_REG))
                datal = ord(self.readReg(self.DATAL_REG))
                regValue = (datah<<4) | (datal>>4)
                humidity = (regValue / 16.0)-24
                return humidity
