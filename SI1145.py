 # SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
 # SPDX-FileCopyrightText: Copyright (c) 2022 Carter Nelson for Adafruit Industries
 # SPDX-License-Identifier: Unlicense
 
import time
import board
import busio
import csv
import adafruit_si1145
 
 
from datetime import datetime

with open('SI1145_data.csv', '+a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Date','Time',
                         'SI1145.visible_light (#1)', 'SI1145.infrared (#1)', 'SI1145.UV_index (#1)',
                         'SI1145.visible_light (#2)', 'SI1145.infrared (#2)', 'SI1145.UV_index (#2)'])

#----------------------------------------------------------
i2c = busio.I2C(board.D3, board.D2) #for DEFAULT i2c line
#i2c = busio.I2C(board.SCL, board.SDA) #for DEFAULT i2c line
#print(i2c.scan())

try:    
    si1 = adafruit_si1145.SI1145(i2c)
except:
    pass

i2c = busio.I2C(board.D1, board.D0) #for RESERVED i2c line
#print(i2c.scan())

try:    
    si2 = adafruit_si1145.SI1145(i2c)
except:
    pass

#----------------------------------------------------------
# loop forever printing values
while True:
    reading = []
    
    # als: a two tuple of the Ambient Light System (ALS) => visible and infrared values
    #vis1, ir1 = si1.als
    try:
        reading.append('%.3f' %si1.als[0])
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %si1.als[1])
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %si1.uv_index)
    except:
        reading.append("NA")

    #-------------------------------------------
    #vis2, ir2 = si2.als
    try:
        reading.append('%.3f' %si2.als[0])
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %si2.als[1])
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %si2.uv_index)
    except:
        reading.append("NA")

    #------------------------------------------- 
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    print('\nSI1145')
    print ('Time: ',date, current_time) 
    print ('lux1','\tIR1 (nm)', '\tUV_index1','\tlux2','\tIR2 (nm)', '\tUV_index2')
    print (reading)
       
    
    with open('SI1145_data.csv', '+a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([date, current_time,
                             reading[0], reading[1], reading[2],
                             reading[3], reading[4], reading[5],])
      
    time.sleep(10) # Time interval (s) for data printing
