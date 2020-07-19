import os
import datetime
from time import time, sleep
from random import randint, choice

from gpiozero import RGBLED, Button, Buzzer

from exercise import Exercise
from challenge import Challenge
from all_activities import exercises
from oled import OLED

#define inputs and outputs
led    = RGBLED(red=17, green=27, blue=22)
button = Button(4, pull_up=False)
buzzer = Buzzer(18)
oled   = OLED()
oled.clear_image()

'''
Cycle through different modes using button. Hold button down for more than 2 seconds and the
LED will turn green and the displayed mode will be selected.

NORMAL - regular minute timing
LIGHTNING - reduces minutes into seconds for fast activity draw

Called from main and result passed into generate_rand_time
'''
def select_mode():
    select = False
    modes = ["NORMAL", "LIGHTNING"]
    num_modes = len(modes) - 1
    num = 0

    while not select:

        if num > num_modes:
            num = 0
        else:
            num += 1
        oled.show_msg("Select Mode:", modes[num]

        button.wait_for_press()
        held_time = time()
        sleep(0.05)
        while button.is_pressed():
            if time() - held_time > 2:
                led.color = Color("green")
                select = True
            delay(0.05)
    
    led.off()
    return modes[num]

'''
generates a random amount of time based on activity intensity
''''
def generate_rand_time(intensity, mode):

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
        interval = randint(1, 5)   # start

    print("interval_time =", interval)  #TODO: Testing only, can remove during normal operation
    log_data("Interval time = " + str(interval))

    if mode == "LIGHTNING":
        return interval
    elif mode == "NORMAL":
        return (interval * 60)

'''
Creates or appends to file in logs directory with below date format
Each line contains the time of entry, followed by a tab, the entry text and a newline
'''
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

'''
Main thread
'''
def main():

    mode = select_mode()
    interval_time = generate_rand_time("start", mode)
    start_time = time()
    log_data("")
    log_data("---------- New Session:  " + mode + " mode ----------")
    log_data("")

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
            interval_time = generate_rand_time(intensity, mode)

        sleep(1)

if __name__ == "__main__":
    main()
