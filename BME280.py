# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio
import csv
import adafruit_bme280.advanced as adafruit_bme280
#from adafruit_bme280 import basic as adafruit_bme280

from datetime import datetime

with open('BME280_data.csv', '+a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Date', 'Time',
                         'BME280.temp (#1)', 'BME280.RH (#1)', 'BME280.pressure (#1)',
                         'BME280.temp (#2)', 'BME280.RH (#2)', 'BME280.pressure (#2)',
                         'BME280.temp (#3)', 'BME280.RH (#3)', 'BME280.pressure (#3)',
                         'BME280.temp (#4)', 'BME280.RH (#4)', 'BME280.pressure (#4)'])
                           
#----------------------------------------------------------
i2c = busio.I2C(board.D3, board.D2) #for DEFAULT i2c line
#i2c = busio.I2C(board.SCL, board.SDA) #for DEFAULT i2c line
#i2c = board.I2C()  # uses board.SCL and board.SDA
#print(i2c.scan())

# For using the default address (address=0x77):
# For specific address, connecting SDO to GND to make address=0x76

try:    
    bme1 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    bme1.sea_level_pressure = 1013.25 # change this to match the location's pressure (hPa) at sea level
except:
    pass

try:    
    bme2 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)
    bme2.sea_level_pressure = 1013.25 # change this to match the location's pressure (hPa) at sea level
except:
    pass

i2c = busio.I2C(board.D1, board.D0) #for RESERVED i2c line
#print(i2c.scan())

try:    
    bme3 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    bme3.sea_level_pressure = 1013.25 # change this to match the location's pressure (hPa) at sea level
except:
    pass

try:    
    bme4 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)
    bme4.sea_level_pressure = 1013.25 # change this to match the location's pressure (hPa) at sea level
except:
    pass

#----------------------------------------------------------
while True:
    reading = []

    try:
        reading.append('%.3f' %bme1.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %bme1.relative_humidity)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %bme1.pressure)
    except:
        reading.append("NA")

    try:
        reading.append('%.3f' %bme2.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %bme2.relative_humidity)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %bme2.pressure)
    except:
        reading.append("NA")
    #-------------------------------------------
    try:
        reading.append('%.3f' %bme3.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %bme3.relative_humidity)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %bme3.pressure)
    except:
        reading.append("NA")

    try:
        reading.append('%.3f' %bme4.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %bme4.relative_humidity)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %bme4.pressure)
    except:
        reading.append("NA")
        
    #-------------------------------------------     
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    print('\nBME280')   
    print ('Time: ',date, current_time) 
    print ('temp1','\tRH1', '\tpressure1 (hPa)', '\ttemp2','\tRH2', '\tpressure2 (hPa)',
           '\ttemp3','\tRH3', '\tpressure3 (hPa)', '\ttemp4','\tRH4', '\tpressure4 (hPa)')
    print (reading)

   
    with open('BME280_data.csv', '+a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([date, current_time,
                             reading[0], reading[1], reading[2],
                             reading[3], reading[4], reading[5],
                             reading[6], reading[7], reading[8],
                             reading[9], reading[10], reading[11]])
     
    time.sleep(10) # Time interval (s) for data printing (min:2s)
    
