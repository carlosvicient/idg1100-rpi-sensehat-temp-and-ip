#import dependencies
from sense_hat import SenseHat
import sys
import time

#Global variables
sense = SenseHat()
text_colour = (25, 157, 36)
back_colour = (157, 25, 146)
argument = sys.argv[1]
text =  'Hello world!' if argument is None else argument
scroll_speed = 0.2 #the bigger the number, the lower the speed
iterations = 4

#Configurations - rotate screen automatically using the data from the accelerometer
#This function is called before printing text
def auto_rotate_display():
	#read data from the sensors
	raw = sense.get_accelerometer_raw()
	x = round(raw['x'], 0)
	y = round(raw['y'], 0)

	rotation = 0
	if x == -1:
		rotation = 90
	elif y == -1: 
		rotation = 180
	elif x == 1: 
		rotation = 270
	sense.set_rotation(rotation)

auto_rotate_display()
sense.show_message(text, text_colour=text_colour, back_colour=back_colour, scroll_speed = scroll_speed)