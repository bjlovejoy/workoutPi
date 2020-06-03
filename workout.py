import os
import datetime
from time import time, sleep
from random import randint, choice

from gpiozero import RGBLED, Button, Buzzer

from exercise import Exercise
from challenge import Challenge
from all_activities import exercises
from oled import OLED

led    = RGBLED(red=17, green=27, blue=22)
button = Button(4, pull_up=False)
buzzer = Buzzer(18)
oled   = OLED()
oled.clear_image()

def generate_rand_time(intensity):

    interval = 0

    if intensity == "easy":
        interval = randint(10, 17)
    elif intensity == "moderate":
        interval = randint(15, 20)
    elif intensity == "vigorous":
        interval = randint(20, 25)
    elif intensity == "yoga":
        interval = randint(10, 15)
    elif intensity == "challenge":
        interval = randint(20, 27)
    else:
        interval = randint(1, 5)

    print("interval_time =", interval)
    log_data("Interval time = " + str(interval))
    return (interval * 60)

def log_data(text):
    
    today_date = str(datetime.date.today()).replace("-", "_")
    hour_min = (datetime.datetime.now()).strftime("%H:%M")
    log_path = "/home/pi/workoutPi/logs/error_log_" + today_date + ".txt"

    append_write = "w"
    if os.path.isfile(log_path):
        append_write = "a"

    with open(log_path, append_write) as log:
        line = hour_min + "\t" + text + "\n"
        log.write(line)

def main():

    interval_time = generate_rand_time("start")
    start_time = time()

    while True:

        if time() - start_time > interval_time:

            #randomly select exercise and number of reps/challenge items
            activity = choice(exercises)
            log_data("New activity selected = " + activity.name)
            num_reps, intensity = activity.generate_rand_reps()
            log_data("num_reps = " + str(num_reps) + "\tintensity = " + intensity)
            
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
