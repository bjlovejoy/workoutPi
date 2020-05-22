from time import time, sleep
from random import randint
import sys

from gpiozero import Button, RGBLED, Buzzer
from colorzero import Color

from challenge import Challenge
from oled import OLED

class Exercise:

    def __init__(self, name, min, max, increment=1, low_threshold=None, high_threshold=None, yoga=False, style="num", unit="rep", challenges=list()):
        """
        name: name of the exercise/activity (str)
        min/max: lowest/highest number of reps (int)
        increment: ensures number of reps is a multiple of this number (1, 2, 5, 10, etc.) (int)
        low_threshold: between easy and moderate activities (number is included in easy) (int)
        high_threshold: between moderate and vigorous activities (number is included in moderate) (int)
        yoga: if the exercise is a yoga activity (bool)
        style: number of reps or for certain amount of time (str - "num", "time")
        unit: measure of exercise (rep, sec, min, mile, laps, etc.) (str)
        challenges: a list of Challenge objects (list)
        """

        self.name           = name
        self.min            = min    #make sure min in >= increment
        self.max            = max
        self.increment      = increment
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
        colors = [Color("red"), Color("orange"), Color("yellow"), Color("green"), Color("blue"), Color("purple"), Color("white")]

        if intensity == "challenge":
            num = 7

        else:
            num = 3
            if intensity == "yoga":
                led.color = colors[5]
            elif intensity == "vigorous":
                led.color = colors[0]
            elif intensity == "moderate":
                led.color = colors[1]
            elif intensity == "easy":
                led.color = colors[2]

        for i in range(num):
            if intensity == "challenge":
                led.color = colors[i]
            buzzer.on()
            led.on()
            sleep(0.1)
            buzzer.off()
            led.off()
            sleep(0.1)

        start = time()
        delay = 60

        while not self.button_pressed:

            if time() - start > delay:
                notify_and_wait(0.2, button, buzzer, True)
                notify_and_wait(0.2, button, buzzer, False)
                start = time()
            else:
                notify_and_wait(0.2, button, led, True)
                if self.button_pressed:
                    notify_and_wait(0.01, button, led, False)
                else:
                    notify_and_wait(0.8, button, led, False)
        
        self.button_pressed = False
        sleep(0.5)
        led.on()
    
    def notify_and_wait(self, sleep_time, input_device, output_device, output_state):
        """
        sleep_time: desired time to sleep (int: in seconds)
        input_device: button
        output_device: led or buzzer
        output_state: desired state of output device (bool); True is on(), False is off()
        """

        wait_interval = 0.01   #time between alternating sleep and button reading

        if output_state == True:
            output_device.on()
        else:
            output_device.off()

        for i in range(int(sleep_time/wait_interval)):
            if input_device.is_pressed:
                self.button_pressed = True
            sleep(wait_interval)
    
    def handle_regular(self, num, button, led, buzzer, oled):
        num = int(generated_num/self.increment) * self.increment
        print(num, self.unit, "\t", self.name)
        oled.num_with_exercise(num, self.unit, self.name)
        sleep(0.5)

        if self.style == "num":
            button.wait_for_press()
        
        elif self.style == "time":
            button.wait_for_press()
            led.off()
            led.color = Color("green")
            sleep(5)
            led.on()
            sleep(num)
            led.off()
            buzzer.on()
            sleep(0.3)
            buzzer.off()
        
        else:
            print("ERROR: style not supported ->", self.style, "->", self.name)   #TODO: consider output file (add to .git_ignore) -> same with all prints
            led.color = Color("red")
            for i in range(10):
                led.on()
                sleep(0.1)
                led.off()
                sleep(0.1)
            sys.exit()

    def handle_challenge(self, challenge_index, button, led, buzzer, oled):
        text = self.challenges[challenge_index].description
        print(text)
        oled.text_block(text)
        sleep(0.5)

        if self.challenges[challenge_index].style == "stopwatch":
            button.wait_for_press()
            led.off()
            led.color = Color("green")
            sleep(5)
            led.on()
            start = time()
            button.wait_for_press()
            led.off()
            stop = round(time() - start, 3)
            print("Stopwatch event time:", stop)
            oled.show_time(stop)
            button.wait_for_press()
            self.challenges[challenge_index].save_results_stopwatch(stop, oled)
            button.wait_for_press()
        
        elif self.challenges[challenge_index].style == "counter":
            button.wait_for_press()
            led.off()
            led.color = Color("green")
            sleep(5)
            led.on()
            sleep(self.challenges[challenge_index].num_time)
            led.off()
            buzzer.on()
            sleep(0.5)
            buzzer.off()
            self.challenges[challenge_index].save_results_counter(button, oled)
            button.wait_for_press()
        
        else:
            print("ERROR: style not supported ->", self.style, "->", self.name)
            led.color = Color("red")
            for i in range(10):
                led.on()
                sleep(0.1)
                led.off()
                sleep(0.1)
            sys.exit()