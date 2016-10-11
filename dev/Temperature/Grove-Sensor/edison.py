import time
import pyupm_grove as grove

def main_1():
# Create the temperature sensor object using AIO pin 0
	temp = grove.GroveTemp(1)
	print temp.name()

                   # Read the temperature ten times, printing both the Celsius and
                       # equivalent Fahrenheit temperature, waiting one second between reading
	for i in range(0, 10):
 		celsius = temp.value()
 		#fahrenheit = celsius * 9.0/5.0 + 32.0;
 		print "Temperature:"+str(celsius)
		time.sleep(15)
main_1()
