import smbus
import time
import sys
import csv

from datetime import datetime

with open('SDP_data.csv', '+a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Date','Time',
                         'sdp810(Bus0)','sdp610(Bus0)',
                         'sdp810(Bus1)','sdp610(Bus1)'])

#----------------------------------------------------------   
def readDP_sdp610(busnum):
    bus=smbus.SMBus(busnum) #The default i2c bus
    addr = 0x40
    MAXPRESSURE = 25
    if (MAXPRESSURE == 500):
        scalefactor = 60.0
    elif (MAXPRESSURE == 125):
        scalefactor = 240.0
    elif (MAXPRESSURE == 25):
        scalefactor = 1200.0
    else:
        print >> sys.stderr, "Falsche Druckangabe!"
        exit(1)
    
    bus.write_byte(addr,0xF1)
    time.sleep(1)
    MSB = bus.read_byte(addr)
    LSB = bus.read_byte(addr)
    result = (MSB << 8) + LSB
  
    if result > 0x7FFF:
        result = result - 0x10000
    differential_pressure = float(result/scalefactor)
    #print("Bus: "+str(busnum)+" => SDP610 Diffirential Pressure: "+'%.3f'%differential_pressure+" PA")
    return differential_pressure
    #time.sleep(1)
    bus.close()
  
#----------------------------------------------------------
def readDP_sdp810(busnum):
    bus=smbus.SMBus(busnum) #The default i2c bus
    address=0x25
    bus.write_i2c_block_data(address, 0x3F, [0xF9]) #Stop any cont measurement of the sensor
    time.sleep(1)
    bus.write_i2c_block_data(address, 0x36, [0X03]) # The command code 0x3603 is split into two arguments, cmd=0x36 and [val]=0x03 
    time.sleep(1)
    reading=bus.read_i2c_block_data(address,0,9)
    pressure_value=reading[0]+float(reading[1])/255
    if pressure_value>=0 and pressure_value<128:
        differential_pressure=pressure_value*240/256 #scale factor adjustment
    elif pressure_value>128 and pressure_value<=256:
        differential_pressure=-(256-pressure_value)*240/256 #scale factor adjustment
    elif pressure_value==128:
        differential_pressure=99999999 #Out of range
    #print("Bus: "+str(busnum)+" => SDP810 Diffirential Pressure: "+'%.3f'%differential_pressure+" PA")
    return differential_pressure
    bus.close()
  
#----------------------------------------------------------
while True:
    reading = []
  
    try:
        reading.append('%.3f'%readDP_sdp810(0))       #sdp810 on bus 0
    except:
        reading.append("NA")
    try:
        reading.append('%.3f'%readDP_sdp610(0))       #sdp610 on bus 0
    except:
        reading.append("NA")
    try:
        reading.append('%.3f'%readDP_sdp810(1))       #sdp810 on bus 1
    except:
        reading.append("NA")
    try:
        reading.append('%.3f'%readDP_sdp610(1))       #sdp610 on bus 1
    except:
        reading.append("NA")
        
    #-------------------------------------------
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    print('\nSDP610/810')
    print ('Time: ',date, current_time) 
    print ('SDP1_810','\tSDP1_610', '\tSDP2_810','\tSDP2_610')
    print (reading)

    with open('SDP_data.csv', '+a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([date, current_time,
                           reading[0], reading[1],
                           reading[2] ,reading[3]])

    time.sleep(7)   # Time interval (s) for data printing (need to be adjusted by -3s)

