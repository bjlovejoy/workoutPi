from time import time, sleep
from random import randint

from gpiozero import RGBLED, Button, Buzzer
from colorzero import Color   #need to install this?  -> make requirements file with gpiozero, oled, etc.

from exercise import Exercise
from challenge import Challenge
from oled import OLED

led    = RGBLED(red=17, green=27, blue=22)
button = Button(, pull_up=False)  #TODO: set pin number
buzzer = Buzzer()  #TODO: set pin number
oled   = OLED()

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
                activity.handle_challenge(challenge_index, button, led, buzzer, oled)

            else:
                activity.handle_regular(num_reps, button, led, buzzer, oled)
            
            
            start_time = time()

        sleep(1)

if __name__ = "__main__":
    main()
