import time
import board
import busio
import csv
import adafruit_scd30

from datetime import datetime

with open('SCD30_data.csv', '+a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Date', 'Time',
                         'SCD30.temp (#1)', 'SCD30.RH (#1)', 'SCD30.CO2 (#1)',
                         'SCD30.temp (#2)', 'SCD30.RH (#2)', 'SCD30.CO2 (#2)'])
 
#----------------------------------------------------------
i2c = busio.I2C(board.D3, board.D2) #for DEFAULT i2c line
#i2c = busio.I2C(board.SCL, board.SDA) #for DEFAULT i2c line
#i2c = board.I2C()  # uses board.SCL and board.SDA
#print(i2c.scan())
try:    
    scd1 = adafruit_scd30.SCD30(i2c)
except:
    pass


i2c = busio.I2C(board.D1, board.D0) #for RESERVED i2c line
#print(i2c.scan())
try:    
    scd2 = adafruit_scd30.SCD30(i2c)  
except:
    pass

#----------------------------------------------------------
while True:
    reading = []
    
    try:
        reading.append('%.3f' %scd1.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %scd1.relative_humidity)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %scd1.CO2)
    except:
        reading.append("NA")
    #-------------------------------------------
    try:
        reading.append('%.3f' %scd2.temperature)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %scd2.relative_humidity)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %scd2.CO2)
    except:
        reading.append("NA")
        
    #-------------------------------------------        
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    print('\nSCD30')
    print ('Time: ',date, current_time) 
    print ('temp1','\tRH1', '\tppm1','\ttemp2', '\tRH2', '\tppm2')
    print (reading)

           
    with open('SCD30_data.csv', '+a', newline='') as csvfile:
      spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
      spamwriter.writerow([date, current_time,
                           reading[0], reading[1], reading[2],
                           reading[3], reading[4], reading[5]])
  
       
    time.sleep(10) # # Time interval (s) for data printing

    
    
