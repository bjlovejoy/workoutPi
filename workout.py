from time import time, sleep
from random import randint

from gpiozero import RGBLED, Button, Buzzer
from colorzero import Color   #need to install this?  -> make requirements file with gpiozero, oled, etc.

from exercise import Exercise
from challenge import Challenge
from oled import OLED

led    = RGBLED(red=17, green=27, blue=22)
button = Button(4, pull_up=False)  #TODO: set pin number
buzzer = Buzzer(18)  #TODO: set pin number
oled   = OLED()

"""
push ups, sit ups, jumping jacks, burpees, planks, push up planks,
squats, lunges, bicyles, scissor kicks, curls, bench press, run/jog,
peck deck, downward dog, flutter kicks, crunches, superman, upward seal,
run in place, bicycle sit up, sit up with legs in the air, mountain climbers,
move weight side to side with knees in the air, stretches?, 

"""

#red:intense, orange:moderate, yellow:easy, green:go, blue:get water, purple:yoga
  

exercises = [Exercise("Push-Ups", 5, 20, 1, 5, 10), Exercise("Sit Ups", 5, 30)]  #TODO: replace spaces with underscores, and have underscores removed when printing
num_exercises = len(exercises)


def generate_rand_time(intensity):

    interval = 0

    if intensity == "easy":
        interval = randint(10, 17)
    elif intensity == "moderate":
        interval = randint(15, 20)
    elif intensity == "vigorous":
        interval = randint(20, 30)
    elif intensity == "yoga":
        interval = randint(10, 17)
    else:
        interval = randint(1, 5)

    print("interval_time =", interval)
    return (interval)    #TODO: replace *60

def main():

    interval_time = generate_rand_time("start")
    start_time = time()

    while True:

        if time() - start_time > interval_time:

            #randomly select exercise and number of reps/challenge items
            activity = exercises[randint(0, num_exercises-1)]
            print("New activity selected =", activity)
            num_reps, intensity = activity.generate_rand_reps()
            print("num_reps =", num_reps, "\tintensity =", intensity)
            
            #notify user of new activity continuously and wait for button input
            activity.wait_for_input(intensity, button, led, buzzer)

            #display message on OLED display, wait for user to finish exercise and handle any cleanup
            if intensity ==  "challenge":
                challenge_index = num_reps
                activity.handle_challenge(challenge_index, button, led, buzzer, oled)

            else:
                activity.handle_regular(num_reps, button, led, buzzer, oled)
            
            start_time = time()
            interval_time = generate_rand_time(intensity)

        sleep(1)

if __name__ == "__main__":
    main()
