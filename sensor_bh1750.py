#!/usr/bin/python
import smbus

DEVICE     = 0x23 # Default device I2C address
 
POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value

bus = smbus.SMBus(1)

def convertToNumber(data):
  return ((data[1] + (256 * data[0])) / 1.2)

def readLight(addr=DEVICE):
  data = bus.read_i2c_block_data(addr,0x21)
  return convertToNumber(data)

def main():
    light = str(readLight())
    file = open('data.txt', 'w')
    file.write(light)
    file.close()
    print "Light Level : " + `light` + " lx"
   
if __name__=="__main__":
   main()
