#!/usr/bin/env python
# -*- coding: utf-8 -*-
import TH02
import PyBCM2835

def main():
        myTH02 = TH02.TH02()
        while(1):
                myTH02.startFastHumidityConversion()
                humidity = myTH02.readHumidity()
                myTH02.startFastTempConversion()
                temp = myTH02.readTemp()
                PyBCM2835.delay(1000)
                print "Temp = " + str(temp) + " C, humidity = " + str(humidity)


if __name__ == '__main__':
    main()
