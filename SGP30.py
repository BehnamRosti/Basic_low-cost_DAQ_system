import time
import board
import busio
import csv
import adafruit_sgp30

from datetime import datetime

with open('SGP30_data.csv', '+a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Date', 'Time',
                         'SGP30.eCO2 (#1)', 'SGP30.TVOC (#1)',
                         'SGP30.eCO2 (#2)', 'SGP30.TVOC (#2)'])

#----------------------------------------------------------
i2c = busio.I2C(board.D3, board.D2) #for DEFAULT i2c line
#i2c = busio.I2C(board.SCL, board.SDA) #for DEFAULT i2c line
#i2c = board.I2C()  # uses board.SCL and board.SDA
#print(i2c.scan())
try:    
    sgp1 = adafruit_sgp30.Adafruit_SGP30(i2c)
except:
    pass

i2c = busio.I2C(board.D1, board.D0) #for RESERVED i2c line
#print(i2c.scan())
try:    
    sgp2 = adafruit_sgp30.Adafruit_SGP30(i2c)
except:
    pass

#sgp1.set_iaq_baseline(0x8973, 0x8AAE)
#sgp2.set_iaq_baseline(0x8973, 0x8AAE)
#sgp1.set_iaq_relative_humidity(celsius=22.1, relative_humidity=44)
#elapsed_sec = 0

#----------------------------------------------------------
while True:
    reading = []

    try:
        reading.append('%.3f' %sgp1.eCO2)	#eCO2 (ppm)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %sgp1.TVOC)	#TVOC (ppb)
    except:
        reading.append("NA")

    #-------------------------------------------
    try:
        reading.append('%.3f' %sgp2.eCO2)	#eCO2 (ppm)
    except:
        reading.append("NA")
    try:
        reading.append('%.3f' %sgp2.TVOC)	#TVOC (ppb)
    except:
        reading.append("NA")
        
    #-------------------------------------------
    '''elapsed_sec += 1
    if elapsed_sec > 10:
        elapsed_sec = 0
        print(
            "**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x"
            %(sgp1.baseline_eCO2, sgp1.baseline_TVOC)
            )'''
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    print('\nSGP30')
    print ('Time: ',date, current_time) 
    print ('eCO2_#1','\tTVOC_#1', '\teCO2_#2','\tTVOC_#2')
    print (reading)

           
    with open('SCD30_data.csv', '+a', newline='') as csvfile:
      spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
      spamwriter.writerow([date, current_time,
                           reading[0], reading[1],
                           reading[2], reading[3]])
  
       
    time.sleep(10) # Time interval (s) for data printing

