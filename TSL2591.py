# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
# TSL2591 sensor is used to monitor the detected light value

import time
import board
import busio
import csv
import adafruit_tsl2591

from datetime import datetime

with open('TSL2591_data.csv', '+a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Date', 'Time',
                         'TSL2591.total_light (#1)', 'TSL2591.infrared_light (#1)',
                         'TSL2591.total_light (#2)', 'TSL2591.infrared_light (#2)'])

#----------------------------------------------------------
i2c = busio.I2C(board.D3, board.D2) #for DEFAULT i2c line
#i2c = busio.I2C(board.SCL, board.SDA) #for DEFAULT i2c line
#print(i2c.scan())

try:    
    tsl1 = adafruit_tsl2591.TSL2591(i2c)
    tsl1.gain = adafruit_tsl2591.GAIN_LOW #for high amouont of outdoor radiation
    tsl1.integration_time = adafruit_tsl2591.INTEGRATIONTIME_100MS
except:
    pass

i2c = busio.I2C(board.D1, board.D0) #for RESERVED i2c line
#print(i2c.scan())

try:    
    tsl2 = adafruit_tsl2591.TSL2591(i2c)
    tsl2.gain = adafruit_tsl2591.GAIN_LOW #for high amouont of outdoor radiation
    tsl2.integration_time = adafruit_tsl2591.INTEGRATIONTIME_100MS
except:
    pass

#----------------------------------------------------------
while True:
    reading = []
    
    try:
        reading.append('%.3f' %tsl1.lux)
    except:
        reading.append("NA")     
    try:
        reading.append('%.3f' %tsl1.infrared)
    except:
        reading.append("NA")
    #-------------------------------------------
    try:
        reading.append('%.3f' %tsl2.lux)
    except:
        reading.append("NA")     
    try:
        reading.append('%.3f' %tsl2.infrared)
    except:
        reading.append("NA")

    #------------------------------------------- 
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    print('\nTSL2591')
    print ('Time: ',date, current_time) 
    print ('lux1','\tIR1(nm)','\tlux2','\tIR2(nm)')
    print (reading)
      
    
    with open('TSL2591_data.csv', '+a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([date, current_time,
                             reading[0], reading[1],
                             reading[2], reading[3] ])
        
    time.sleep(10) # Time interval (s) for data printing

