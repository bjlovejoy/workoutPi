from time import time, sleep
from random import randint

from gpiozero import Button, LED, PWMLED, RGBLED, Buzzer
from gpiozero.tones import Tone
from colorzero import Color   #need to install this?  -> make requirements file with gpiozero, oled, etc.
#from oled import

from exercise import Exercise
from challenge import Challenge

led = RGBLED(red=17, green=27, blue=22)

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


interval_min = 15
interval_time = interval_min * 60  #need to delay between 10-20 minutes based on exercise intensity
start_time = time()

def main():
  while True:

    if time() - start_time > interval_time:
      #flash light color of intensity and sound buzzer occasionally until button is pressed
      #(press button once to display and stop light/buzzer, press again after exercise complete/other for challenges)
      activity = exercises[randint(0, num_exercises-1)]
      num_reps, intensity = activity.generate_rand_reps()
      
      
      start_time = time()

    sleep(1)

if __name__ = "__main__":
  main()
