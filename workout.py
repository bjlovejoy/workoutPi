from time import time, sleep
from random import randint, choice

from gpiozero import RGBLED, Button, Buzzer
from colorzero import Color   #TODO: make requirements file with gpiozero, oled, etc.

from exercise import Exercise
from challenge import Challenge
from oled import OLED

led    = RGBLED(red=17, green=27, blue=22)
button = Button(4, pull_up=False)  #TODO: set pin number
buzzer = Buzzer(18)  #TODO: set pin number
oled   = OLED()
oled.clear_image()

"""
push ups, sit ups, crunches, jumping jacks, burpees, planks, push up planks,
squats, lunges, bicyles, scissor kicks, curls, bench press, run/jog,
peck deck, downward dog, flutter kicks, crunches, superman, upward seal,
run in place, bicycle sit up, sit up with legs in the air, mountain climbers,
move weight side to side with knees in the air, stretches?, 

"""

#red:intense, orange:moderate, yellow:easy, green:go, blue:get water, purple:yoga

push_up_stopwatch_10 = Challenge("push_up_stopwatch_10", "stopwatch", "Do 10 pushups as fast as possible")
push_up_stopwatch_15 = Challenge("push_up_stopwatch_15", "stopwatch", "Do 15 pushups as fast as possible")
push_up_stopwatch_20 = Challenge("push_up_stopwatch_20", "stopwatch", "Do 20 pushups as fast as possible")

push_up_counter_30s = Challenge("push_up_counter_30s", "counter", "Do as many pushups as you can in 30 sec", 3)  #TODO: make 3, 6 -> 30, 60
push_up_counter_1m = Challenge("push_up_counter_1m", "counter", "Do as many pushups as you can in 1 min", 6)

sit_up_stopwatch_20 = Challenge("sit_up_stopwatch_20", "stopwatch", "Do 20 situps as fast as possible")
sit_up_stopwatch_30 = Challenge("sit_up_stopwatch_30", "stopwatch", "Do 30 situps as fast as possible")

sit_up_counter_30s = Challenge("sit_up_counter_30s", "counter", "Do as many situps as you can in 30 sec", 3)
sit_up_counter_1m = Challenge("sit_up_counter_1m", "counter", "Do as many situps as you can in 1 min", 6)

push_up = Exercise("Push_Ups", 5, 6, 1, 7, 12, challenges=[push_up_stopwatch_10, push_up_stopwatch_15, push_up_stopwatch_20, push_up_counter_30s, push_up_counter_1m])
sit_up  = Exercise("Sit_Ups",  5, 30, 5, 10, 20, challenges=[sit_up_stopwatch_20, sit_up_stopwatch_30, sit_up_counter_30s, sit_up_counter_1m])



exercises = [push_up]  #TODO: replace spaces with underscores, and have underscores removed when printing


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
            activity = choice(exercises)
            print("New activity selected =", activity.name)
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
            
            led.off()
            oled.clear_image()
            
            start_time = time()
            interval_time = generate_rand_time(intensity)

        sleep(1)

if __name__ == "__main__":
    main()
