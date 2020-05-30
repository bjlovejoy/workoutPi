import os
import sys
import datetime
from time import time, sleep
from random import randint

from gpiozero import Button, RGBLED, Buzzer
from colorzero import Color

from challenge import Challenge
from oled import OLED

def log_data(text):
    
    hour_min = (datetime.datetime.now()).strftime("%H:%M")
    log_path = "/home/pi/workoutPi/logs/error_log_" + today_date + ".txt"

    append_write = "w"
    if os.path.isfile(log_path):
        append_write = "a"

    with open(log_path, append_write) as log:
        line = hour_min + "\t" + text + "\n"
        log.write(line)

class Exercise:

    def __init__(self, name, min, max, low_threshold, high_threshold, multiplier=1, yoga=False, style="num", unit="rep", challenges=list()):
        """
        name: name of the exercise/activity (str)
        min/max: lowest/highest number of reps (int)
        multiplier: multiplies number of reps (ex. 1-4 *5 = 5, 10, 15, 20) (int)
        low_threshold: between easy and moderate activities (number is included in easy) (int)
        high_threshold: between moderate and vigorous activities (number is included in moderate) (int)
        yoga: if the exercise is a yoga activity (bool)
        style: number of reps or for certain amount of time (str - "num", "time")
        unit: measure of exercise (rep, sec, min, mile, laps, etc.) (str)
        challenges: a list of Challenge objects (list)
        """

        self.name           = name
        self.min            = min
        self.max            = max
        self.multiplier     = multiplier
        self.low_threshold  = low_threshold
        self.high_threshold = high_threshold
        self.yoga           = yoga
        self.style          = style
        self.unit           = unit
        self.challenges     = challenges

        self.num_challenges = len(challenges)
        self.max_total      = self.max + self.num_challenges  #to be used for random number generation
        self.button_pressed = False

    def generate_rand_reps(self):
        
        generated_num = randint(self.min, self.max_total)
        intensity = None
        
        if self.yoga:
            intensity = "yoga"
        
        elif generated_num > self.max:
            intensity = "challenge"
            generated_num -= self.max + 1  #convert into index to access challenges list
        
        else:
            if generated_num > self.high_threshold:
                intensity = "vigorous"
            elif generated_num > self.low_threshold:
                intensity = "moderate"
            else:
                intensity = "easy"
        
        return (generated_num, intensity)

    def wait_for_input(self, intensity, button, led, buzzer):
        """
        intensity: yoga, challenge, vigorous, moderate, easy (str)
        led, button, buzzer: pass gpiozero objects from main script
        """
        
        num = 0
        self.button_pressed = False
        colors = [Color("red"), Color("orangered"), Color("yellow"), Color("green"), Color("blue"), Color("purple"), Color("white")]

        if intensity == "challenge":
            num = 7

        else:
            num = 3
            if intensity == "yoga":
                color = colors[5]
            elif intensity == "vigorous":
                color = colors[0]
            elif intensity == "moderate":
                color = colors[1]
            elif intensity == "easy":
                color = colors[2]

        for i in range(num):
            if intensity == "challenge":
                color = colors[i]
            buzzer.on()
            led.color = color
            sleep(0.1)
            buzzer.off()
            led.off()
            sleep(0.1)

        start = time()
        delay_sec = 60  #how long to wait before sounding the buzzer reminder

        while not self.button_pressed:

            if time() - start > delay_sec:
                self.notify_and_wait(0.2, button, buzzer, True)
                self.notify_and_wait(0.2, button, buzzer, False)
                start = time()
            else:
                self.notify_and_wait(0.2, button, led, True, color)
                if self.button_pressed:
                    self.notify_and_wait(0.01, button, led, False)
                else:
                    self.notify_and_wait(0.8, button, led, False)
        
        sleep(0.3)
        led.color = color
    
    def notify_and_wait(self, sleep_time, input_device, output_device, output_state, color=None):
        """
        sleep_time: desired time to sleep (int: in seconds)
        input_device: button
        output_device: led or buzzer
        output_state: desired state of output device (bool); True is on(), False is off()
        """

        wait_interval = 0.01   #time between alternating sleep and button reading

        if output_state == True:
            if type(output_device) is RGBLED:
                output_device.color = color
            else:
                output_device.on()
        else:
            output_device.off()

        for i in range(int(sleep_time/wait_interval)):
            if input_device.is_pressed:
                self.button_pressed = True
            sleep(wait_interval)
    
    def handle_regular(self, num, button, led, buzzer, oled):
        num *= self.multiplier
        log_data("Print to OLED: " + str(num) + " " + self.unit)
        oled.num_with_exercise(num, self.unit, self.name.replace("_", " "))
        sleep(0.5)

        if self.style == "num":
            button.wait_for_press()    #When finished with exercise
            sleep(0.1)
        
        elif self.style == "time":
            button.wait_for_press()    #To start timer
            led.off()
            sleep(5)
            led.color = Color("green")
            sleep(num)
            led.off()
            buzzer.on()
            sleep(0.3)
            buzzer.off()
        
        else:
            log_data("ERROR: style not supported -> " + self.style + " -> " + self.name)
            for i in range(10):
                led.color = Color("red")
                sleep(0.1)
                led.off()
                sleep(0.1)
            sys.exit()

    def handle_challenge(self, challenge_index, button, led, buzzer, oled):
        text = self.challenges[challenge_index].description
        log_data("Print to OLED (challenge): " + text)
        oled.challenge_block(text)
        sleep(0.5)

        if self.challenges[challenge_index].style == "stopwatch":
            button.wait_for_press()   #To begin 5 second count-down
            led.off()
            sleep(5)
            led.color = Color("green")
            start = time()
            button.wait_for_press()   #To stop timer and record time
            sleep(0.1)
            led.off()
            stop = round(time() - start, 3)
            log_data("Stopwatch event recorded time: " + str(stop))
            oled.show_time(stop)
            button.wait_for_press()   #To leave screen showing resulting time
            self.challenges[challenge_index].save_results_stopwatch(stop, oled)
            button.wait_for_press()   #To leave screen with top 3 records
        
        elif self.challenges[challenge_index].style == "counter":
            button.wait_for_press()   #To begin 5 second count-down
            led.off()
            sleep(5)
            led.color = Color("green")
            sleep(self.challenges[challenge_index].num_time_sec)
            led.off()
            buzzer.on()
            sleep(0.5)
            buzzer.off()
            self.challenges[challenge_index].save_results_counter(button, oled)
            button.wait_for_press()   #To leave screen with top 3 records
        
        else:
            log_data("ERROR: style not supported -> " + self.style + " -> " + self.name)
            for i in range(10):
                led.color = Color("red")
                sleep(0.1)
                led.off()
                sleep(0.1)
            sys.exit()