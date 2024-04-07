# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time; import board
import busio; import csv
import adafruit_sht31d

from datetime import datetime

#----------------------------------------------------------
with open('SHT31D_data.csv', '+a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Date','Time',
                         'SHT31.temp (#1)', 'SHT31.RH (#1)',
                         'SHT31.temp (#2)', 'SHT31.RH (#2)',
                         'SHT31.temp (#3)', 'SHT31.RH (#3)',
                         'SHT31.temp (#4)', 'SHT31.RH (#4)'])

#----------------------------------------------------------
# Create sensor object, communicating over the board's default I2C bus
# For 2 sensors in DEFAULT i2c line
# For using the default address (address=0x44):
# For specific address, connecting ADDR to VDD to make address=0x45

i2c = busio.I2C(board.D3, board.D2) #for DEFAULT i2c line
#i2c = busio.I2C(board.SCL, board.SDA) #for DEFAULT i2c line
#print(i2c.scan())

try:    
    sht1 = adafruit_sht31d.SHT31D(i2c)
except:
    pass
try:
    sht2 = adafruit_sht31d.SHT31D(i2c, address=0x45)
except:
    pass

# For 2 sensors in RESERVED i2c line
i2c = busio.I2C(board.D1, board.D0) #for RESERVED i2c line
#print(i2c.scan())

try:    
    sht3 = adafruit_sht31d.SHT31D(i2c)
except:
    pass
try:
    sht4 = adafruit_sht31d.SHT31D(i2c, address=0x45)
except:
    pass

#----------------------------------------------------------
while True:
    reading = []
    
    try:
        reading.append('%.3f' %sht1.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %sht1.relative_humidity)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %sht2.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %sht2.relative_humidity)
    except:
        reading.append("NA")
   #-------------------------------------------
    try:
        reading.append('%.3f' %sht3.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %sht3.relative_humidity)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %sht4.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %sht4.relative_humidity)
    except:
        reading.append("NA")
 
        
    #-------------------------------------------
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    print('\nSHT31D')
    print ('Time: ',date, current_time) 
    print ('temp1','\tRH1', '\ttemp2', '\tRH2', '\ttemp3', '\tRH3', '\ttemp4', '\tRH4',)
    print (reading)
    
    
    with open('SHT31D_data.csv', '+a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([date, current_time,
                             reading[0], reading[1],
                             reading[2],reading[3],
                             reading[4], reading[5],
                             reading[6], reading[7]])    
    
    time.sleep(10) # Time interval (s) for data printing