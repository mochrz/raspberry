#!/usr/bin/python
import sys
import time

from . import Raspberry_Pi_2_Driver as driver

# Define error constants
DHT_SUCCESS        =  0
DHT_ERROR_TIMEOUT  = -1
DHT_ERROR_CHECKSUM = -2
DHT_ERROR_ARGUMENT = -3
DHT_ERROR_GPIO     = -4
TRANSIENT_ERRORS = [DHT_ERROR_CHECKSUM, DHT_ERROR_TIMEOUT]

# Define sensor type constant
# DHT22  = 22

# Define values
sensor = 22
pin = 14

def readSensor(sensor, pin):
    # Validate pin is a valid GPIO.
    if pin is None or int(pin) < 0 or int(pin) > 31:
        raise ValueError('Pin must be a valid GPIO number 0 to 31.')
    # Get a reading from C driver code.
    result, humidity, temp = driver.read(sensor, int(pin))

    # errorDetection(result)
    return (humidity, temp)

def readRetry(sensor, pin, retries, delay):
    # Function will attempt to read multiple times until a good reading will be found
    for i in range(retries):
        humidity, temperature = readSensor(sensor, pin)
        if humidity is not None and temperature is not None:
            return (humidity, temperature)
        time.sleep(delay)
    return (None, None)

def main():
    humidity, temperature = readRetry(sensor, pin, 15, 2)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        measValue = '{0:0.1f}'.format(temperature, humidity)
        file = open('data2.txt', 'w')
        file.write(measValue)
        file.close()
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)
   
if __name__=="__main__":
   main()
