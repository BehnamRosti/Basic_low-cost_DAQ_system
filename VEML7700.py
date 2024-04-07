# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio
import csv
import adafruit_veml7700 

from datetime import datetime


with open('VEML7700_data.csv', '+a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Date', 'Time',
                         'VEML7700.ambient_light (#1)', 'VEML7700.lux (#1)',
                         'VEML7700.ambient_light (#2)', 'VEML7700.lux (#2)'])

#----------------------------------------------------------
i2c = busio.I2C(board.D3, board.D2) #for DEFAULT i2c line
#i2c = busio.I2C(board.SCL, board.SDA) #for DEFAULT i2c line
#print(i2c.scan())

# For using the default address (address=0x10):

try:
    veml1 = adafruit_veml7700.VEML7700(i2c)
    veml1.light_gain = veml1.ALS_GAIN_1_8 
    veml1.light_integration_time = veml1.ALS_25MS
except:
    pass


i2c = busio.I2C(board.D1, board.D0) #for RESERVED i2c line
#print(i2c.scan())

try:    
    veml2 = adafruit_veml7700.VEML7700(i2c)
    veml2.light_gain = veml2.ALS_GAIN_1_8 
    veml2.light_integration_time = veml2.ALS_25MS
except:
    pass

#----------------------------------------------------------   
while True:
    reading = []
    
    try:
        reading.append('%.3f' %veml1.light)    
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %veml1.lux)
    except:
        reading.append("NA")      
    #-------------------------------------------   
    try:
        reading.append('%.3f' %veml2.light)    
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %veml2.lux)
    except:
        reading.append("NA")  
    
    #------------------------------------------- 
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    print('\nVEML7700')
    print("Time", date, current_time)
    print ('ambient light1','\tlux1', '\tambient light2', '\tlux2')
    print (reading)
       
    
    with open('VEML7700_data.csv', '+a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([date, current_time,
                             reading[0], reading[1],
                             reading[2], reading[3]])
        
    time.sleep(10.0) # Time interval (s) for data printing

    



