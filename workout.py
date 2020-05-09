from gpiozero import Button, LED, PWMLED, RGBLED, Buzzer
from gpiozero.tones import Tone
from time import time, sleep
from random import randint
#from oled import

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
#red:vigorous, blue:easy ?

class Exercise:

  def _init_(self, name, min, max, challenges):

    self.name = name
    self.min  = min
    self.max  = max
    self.challenges = challenges  #list? dict? list of dict? custom class?

  def display(self:
    pass

exercises = [Exercise("Push Ups", 5, 20), Exercise("Sit Ups", 5, 30)]
num_exercises = len(exercises)


interval_min = 15
interval_sec = interval_min * 60
start_time = time()

while True:

  if time() - start_time > interval_sec:  #use minutes

    pass #do stuff here
    start_time = time()

  sleep(1)
