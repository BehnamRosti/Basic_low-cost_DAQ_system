# SPDX-FileCopyrightText: 2020 Bryan Siepert, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
import time
import board
import busio
import csv
import adafruit_tmp117

from datetime import datetime

with open('TMP117_data.csv', '+a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Date', 'Time',
                         'TMP117.temp (#1)', 'TMP117.temp (#2)', 'TMP117.temp (#3)', 'TMP117.temp (#4)'
                         'TMP117.temp (#5)', 'TMP117.temp (#6)', 'TMP117.temp (#7)', 'TMP117.temp (#8)'])
                                 
#help(adafruit_tmp117)
#----------------------------------------------------------
i2c = busio.I2C(board.D3, board.D2) #for DEFAULT i2c line
#i2c = busio.I2C(board.SCL, board.SDA) #for DEFAULT i2c line
#print(i2c.scan())

# For using the default address (address=0x48):
# For specific address, connecting ADDR to VDD ==> address=0x49
# For specific address, connecting ADDR to SDA ==> address=0x4a
# For specific address, connecting ADDR to SCL ==> address=0x4b

try:    
    tmp1 = adafruit_tmp117.TMP117(i2c)
except:
    pass
try:    
    tmp2 = adafruit_tmp117.TMP117(i2c, address=0x49)
except:
    pass
try:    
    tmp3 = adafruit_tmp117.TMP117(i2c, address=0x4a)
except:
    pass
try:    
    tmp4 = adafruit_tmp117.TMP117(i2c, address=0x4b)
except:
    pass

i2c = busio.I2C(board.D1, board.D0) #for RESERVED i2c line
#print(i2c.scan())

try:    
    tmp5 = adafruit_tmp117.TMP117(i2c)
except:
    pass
try:    
    tmp6 = adafruit_tmp117.TMP117(i2c, address=0x49)
except:
    pass
try:    
    tmp7 = adafruit_tmp117.TMP117(i2c, address=0x4a)
except:
    pass
try:    
    tmp8 = adafruit_tmp117.TMP117(i2c, address=0x4b)
except:
    pass

#----------------------------------------------------------
while True:
    reading = []

    try:
        reading.append('%.3f' %tmp1.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %tmp2.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %tmp3.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %tmp4.temperature)
    except:
        reading.append("NA")
    #-------------------------------------------
    try:
        reading.append('%.3f' %tmp5.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %tmp6.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %tmp7.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %tmp8.temperature)
    except:
        reading.append("NA")
        
    #-------------------------------------------     
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    print('\nTMP117')
    print ('Time: ',date, current_time) 
    print ('temp1','\ttemp2', '\ttemp3', '\ttemp4', '\ttemp5', '\ttemp6', '\ttemp7', '\ttemp8')
    print (reading)
    
    with open('TMP117_data.csv', '+a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([date, current_time,
                             reading[0], reading[1], reading[2], reading[3],
                             reading[4], reading[5], reading[6], reading[7]])
     
    time.sleep(10) # Time interval (s) for data printing
