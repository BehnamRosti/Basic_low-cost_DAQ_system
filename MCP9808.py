# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio
import csv
import adafruit_mcp9808

from datetime import datetime

#----------------------------------------------------------
with open('MCP9808_data.csv', '+a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Date','Time',
                         'MCP9808 (#1)','MCP9808 (#2)','MCP9808 (#3)','MCP9808 (#4)',
                         'MCP9808 (#5)','MCP9808 (#6)','MCP9808 (#7)','MCP9808 (#8)',
                         'MCP9808 (#9)','MCP9808 (#10)','MCP9808 (#11)','MCP9808 (#12)',
                         'MCP9808 (#13)','MCP9808 (#14)','MCP9808 (#15)','MCP9808 (#16)']) 

#----------------------------------------------------------
# Create sensor object, communicating over the board's default I2C bus
# For 4 sensors in DEFAULT i2c line
# For using the default address (address=0x18):
# For specific address, connecting A0 to VDD ==> address=0x19
# For specific address, connecting A1 to VDD ==> address=0x1a
# For specific address, connecting A0&A2 to VDD ==> address=0x1b
# For specific address, connecting A2 to VDD ==> address=0x1c
# For specific address, connecting A0&A2 to VDD ==> address=0x1d
# For specific address, connecting A1&A2 to VDD ==> address=0x1e
# For specific address, connecting A0&A1&A2 to VDD ==> address=0x1f

i2c = busio.I2C(board.D3, board.D2) #for DEFAULT i2c line
#i2c = busio.I2C(board.SCL, board.SDA) #for DEFAULT i2c line
#i2c = board.I2C()  # uses board.SCL and board.SDA
#print(i2c.scan())
try:    
    mcp1 = adafruit_mcp9808.MCP9808(i2c)
except:
    pass
try:
    mcp2 = adafruit_mcp9808.MCP9808(i2c, address=0x19)
except:
    pass
try:
    mcp3 = adafruit_mcp9808.MCP9808(i2c, address=0x1a)
except:
    pass
try:
    mcp4 = adafruit_mcp9808.MCP9808(i2c, address=0x1b)
except:
    pass
try:
    mcp5 = adafruit_mcp9808.MCP9808(i2c, address=0x1c)
except:
    pass
try:
    mcp6 = adafruit_mcp9808.MCP9808(i2c, address=0x1d)
except:
    pass
try:
    mcp7 = adafruit_mcp9808.MCP9808(i2c, address=0x1e)
except:
    pass
try:
    mcp8 = adafruit_mcp9808.MCP9808(i2c, address=0x1f)
except:
    pass

# For 4 sensors in RESERVED i2c line
i2c = busio.I2C(board.D1, board.D0) #for RESERVED i2c line
#print(i2c.scan())
try:    
    mcp9 = adafruit_mcp9808.MCP9808(i2c)
except:
    pass
try:
    mcp10 = adafruit_mcp9808.MCP9808(i2c, address=0x19)
except:
    pass
try:
    mcp11 = adafruit_mcp9808.MCP9808(i2c, address=0x1a)
except:
    pass
try:
    mcp12 = adafruit_mcp9808.MCP9808(i2c, address=0x1b)
except:
    pass
try:
    mcp13 = adafruit_mcp9808.MCP9808(i2c, address=0x1c)
except:
    pass
try:
    mcp14 = adafruit_mcp9808.MCP9808(i2c, address=0x1d)
except:
    pass
try:
    mcp15 = adafruit_mcp9808.MCP9808(i2c, address=0x1e)
except:
    pass
try:
    mcp16 = adafruit_mcp9808.MCP9808(i2c, address=0x1f)
except:
    pass

#----------------------------------------------------------
while True:
    reading = []

    try:
        reading.append('%.3f' %mcp1.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %mcp2.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %mcp3.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %mcp4.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %mcp5.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %mcp6.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %mcp7.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %mcp8.temperature)
    except:
        reading.append("NA")
    #-------------------------------------------
    try:
        reading.append('%.3f' %mcp9.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %mcp10.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %mcp11.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %mcp12.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %mcp13.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %mcp14.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %mcp15.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %mcp16.temperature)
    except:
        reading.append("NA")
    #-------------------------------------------

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    print('\nMCP9808')
    print ('Time: ',date, current_time) 
    print ('temp1','\ttemp2', '\ttemp3','\ttemp4', '\ttemp5', '\ttemp6', '\ttemp7', '\ttemp8',
           '\ntemp9','\ttemp10', '\ttemp11','\ttemp12', '\ttemp13', '\ttemp14', '\ttemp15', '\ttemp16')
    print (reading[0], reading[1], reading[2],reading[3],reading[4], reading[5], reading[6], reading[7])
    print (reading[8], reading[9], reading[10],reading[11],reading[12],reading[13],reading[14],reading[15])

    
    with open('MCP9808_data.csv', '+a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([date, current_time,
                             reading[0], reading[1], reading[2],reading[3],
                             reading[4], reading[5], reading[6], reading[7],
                             reading[8], reading[9], reading[10],reading[11],
                             reading[12], reading[13], reading[14], reading[15]])    
    

    time.sleep(10) # Time interval (s) for data printing 

   

    
