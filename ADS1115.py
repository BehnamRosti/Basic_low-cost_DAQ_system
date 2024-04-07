# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# SPDX-License-Identifier: Unlicense
import time
import board
import busio
import csv
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

from datetime import datetime

with open('ADS1115_data.csv', '+a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Date', 'Time',
                         'ADS1115.vol (#1)', 'ADS1115.value (#1)',
                         'ADS1115.vol (#2)', 'ADS1115.value (#2)'])
                                 
#----------------------------------------------------------

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
# For using the default address (address=0x48):
# For specific address, connecting ADDR to VDD ==> address=0x49
# For specific address, connecting ADDR to SDA ==> address=0x4a
# For specific address, connecting ADDR to SCL ==> address=0x4b
ads = ADS.ADS1115(i2c, address=0x4b)

# Create single-ended input on channel 0
#chan = AnalogIn(ads, ADS.P0)

# Create differential input between channel A0 & A1
chan1 = AnalogIn(ads, ADS.P0, ADS.P1)
# Create differential input between channel A2 & A3
chan2 = AnalogIn(ads, ADS.P2, ADS.P3)


# Programmable Gain (PGA) to amplify the incoming signal before it reaches the ADC
# GAIN 2/3 (for an input range of +/- 6.144V)
# GAIN 1 (for an input range of +/-4.096V)
# GAIN 2 (for an input range of +/-2.048V)
# GAIN 4 (for an input range of +/-1.024V)
# GAIN 8 (for an input range of +/-0.512V)
# GAIN 16 (for an input range of +/-0.256V)
ads.gain = 1
#----------------------------------------------------------
while True:
    reading = []

    reading.append('%.5f' %chan1.voltage)

    reading.append('%.3f' %chan1.value)

    reading.append('%.5f' %chan2.voltage)

    reading.append('%.3f' %chan2.value)

        
    #-------------------------------------------     
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    print('\nADS1115')
    print ('Time: ',date, current_time) 
    print ('vol1','\tvalue1', '\tvol2', '\tvalue2')
    print (reading)

    
    with open('ADS1115_data.csv', '+a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([date, current_time,
                             reading[0], reading[1],
                             reading[2], reading[3]])

    time.sleep(10) # Time interval (s) for data printing (min:2s)



