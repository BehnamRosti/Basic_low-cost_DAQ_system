# SPDX-FileCopyrightText: 2020 Bryan Siepert, written for Adafruit Industries
# SPDX-License-Identifier: Unlicense

import time
import board
import busio
import csv
import adafruit_bh1750

from datetime import datetime


with open('BH1750_data.csv', '+a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Date', 'Time',
                         'light_out', 'light_in'])

#----------------------------------------------------------
i2c = busio.I2C(board.D3, board.D2) #for DEFAULT i2c line
#i2c = busio.I2C(board.SCL, board.SDA) #for DEFAULT i2c line
#print(i2c.scan())

# For using the default address (address=0x23):
# For specific address, connecting ADDR/AD0 to Vin to make address=0x5c

# You can change the operation MODE among SHUTDOWN, CONTINUOUS and ONE_SHOT
# You can chosse the measurement RESOLUTION among:
# LOW (4 lux precision, 16ms ==> brighter light)
# MID (1 lux precision, 120ms)
# HIGH (0,5 lux precision, 120ms ==> dimmer light)


try:    
    bh1 = adafruit_bh1750.BH1750(i2c)
    bh1.mode = adafruit_bh1750.Mode.CONTINUOUS 
    bh1.resolution = adafruit_bh1750.Resolution.LOW
    
    
except:
    pass

'''
try:    
    bh2 = adafruit_bh1750.BH1750(i2c, address=0x5c)
    bh2.mode = adafruit_bh1750.Mode.CONTINUOUS 
    bh2.resolution = adafruit_bh1750.Resolution.LOW
except:
    pass
'''

i2c = busio.I2C(board.D1, board.D0) #for RESERVED i2c line
#print(i2c.scan())

try:    
    bh3 = adafruit_bh1750.BH1750(i2c)
    bh3.mode = adafruit_bh1750.Mode.CONTINUOUS 
    bh3.resolution = adafruit_bh1750.Resolution.LOW
except:
    pass
'''
try:    
    bh4 = adafruit_bh1750.BH1750(i2c, address=0x5c)
except:
    pass
'''
#----------------------------------------------------------   
while True:
    reading = []
    
    try:
        reading.append('%.3f' %bh1.lux)
    except:
        reading.append("NA")
    '''
    try:
        reading.append('%.3f' %bh2.lux)
    except:
        reading.append("NA")
    '''
    #-------------------------------------------
    try:
        reading.append('%.3f' %bh3.lux)
    except:
        reading.append("NA")
    '''
    try:
        reading.append('%.3f' %bh4.lux)
    except:
        reading.append("NA")
    '''
    
    #------------------------------------------- 
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    print('\nBH1750')    
    print("Time", date, current_time)
    print ('lux_out', 'lux_out2','\tlux_in')
    print (reading)
       
    
    with open('BH1750_data.csv', '+a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([date, current_time,
                             reading[0], reading[1]])

        
    time.sleep(10) # Time interval (s) for data printing

    


