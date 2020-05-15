from time import time, sleep
from random import randint

from gpiozero import RGBLED, Button, Buzzer
from colorzero import Color   #need to install this?  -> make requirements file with gpiozero, oled, etc.

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from exercise import Exercise
from challenge import Challenge

led    = RGBLED(red=17, green=27, blue=22)
button = Button(, pull_up=False)  #TODO: set pin number
buzzer = Buzzer()  #TODO: set pin number
oled   = Adafruit_SSD1306.SSD1306_128_64(rst=None)

oled.begin()    #Initialize library
oled.clear()    #Clear display
oled.display()  #Update display

#Create blank image for drawing (mode '1' for 1-bit color)
width = oled.width
height = oled.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)  #Get drawing object to draw on image
draw.rectangle((0,0,width,height), outline=0, fill=0)  #Draw a black filled box to clear the image

#Define some constants to allow easy resizing of shapes
padding = -2
top = padding
bottom = height - padding
x = 0  #Move left to right keeping track of the current x position for drawing shapes

font = ImageFont.load_default()

"""
push ups, sit ups, jumping jacks, burpees, planks, push up planks,
squats, lunges, bicyles, scissor kicks, curls, bench press, run/jog,
peck deck, downward dog, flutter kicks, crunches, superman, upward seal,
run in place, bicycle sit up, sit up with legs in the air, mountain climbers,
move weight side to side with knees in the air, stretches?, 

"""

#for most, blink 3 times in color of activity type and play buzzer 3 times
#for reminders, play buzzer once, but still with 3 blinks
#in meantime, turn led on and off every 1 second (use built-in blink feature)
#red:intense, orange:moderate, yellow:easy, green:go, blue:get water, purple:yoga
#include display for water


  
  
exercises = [Exercise("Push-Ups", 5, 20, 1, 5, 10), Exercise("Sit Ups", 5, 30)]
num_exercises = len(exercises)

#in minutes
interval_min = 10
interval_max = 20

interval_time = interval_min * 60  #TODO: need to delay between 10-20 minutes based on exercise intensity
start_time = time()

#TODO: first activity should be within 5 minutes of plugging it in

def generate_rand_time():
    pass  #TODO: start with 1-5 minutes as the bottom "else"

def main():
    while True:

        if time() - start_time > interval_time:

            #randomly select excersice and number of reps/challenge items
            activity = exercises[randint(0, num_exercises-1)]
            num_reps, intensity = activity.generate_rand_reps()
            
            #notify user of new activity continuously and wait for button input
            activity.wait_for_input(intensity, button, led, buzzer)

            #display message on OLED display, wait for user to finish exercise and handle any cleanup
            if intensity ==  "challenge":
                challenge_index = num_reps
                activity.handle_challenge(challenge_index, button, led, buzzer)

            else:
                activity.handle_regular(num_reps, button, led, buzzer)
            
            
            start_time = time()

        sleep(1)

if __name__ = "__main__":
    main()
