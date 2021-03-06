import os
import datetime
from time import time, sleep

from gpiozero import Button, RGBLED, Buzzer
from colorzero import Color

from oled import OLED

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

class Challenge:
    def __init__(self, name, style, description, num_time_sec=60, lowest=True):
        """
        name: name of the challenge to save to text file (str)
        style: how long it takes to do activity ("stopwatch") or how many done in timeframe ("counter")   (str)
        num_time_sec: time for "counter" challenges (int)
        description: text to output to OLED display for challenge (str)
        lowest: if True, then lowest time (stopwatch) is highest score
        """
        
        self.name = name.replace(" ", "_")
        self.style = style
        self.description = description
        self.num_time_sec = num_time_sec
        self.lowest = lowest
    
    def save_results_counter(self, button, oled, led):
        records_path = "/home/pi/workoutPi/records/" + self.name + ".txt"
        edit_file = False
        nums = list()

        select = False
        num = 0

        while not select:

            oled.show_num(num, "How many?")

            button.wait_for_press()
            held_time = time()
            sleep(0.05)
            while button.is_pressed:
                if time() - held_time > 1.5:
                    led.color = Color("green")
                    select = True
                sleep(0.05)
            
            if not select:
                num += 1
        
        led.off()

        if os.path.isfile(records_path):
            with open(records_path, 'r') as rec:
                nums = rec.readlines()
                if num > int(nums[0].rstrip('\n')):
                    nums[2] = nums[1]
                    nums[1] = nums[0]
                    nums[0] = str(num) + '\n'
                    edit_file = True

                elif num > int(nums[1].rstrip('\n')):
                    nums[2] = nums[1]
                    nums[1] = str(num) + '\n'
                    edit_file = True

                elif num > int(nums[2].rstrip('\n')):
                    nums[2] = str(num) + '\n'
                    edit_file = True

            if edit_file:
                with open(records_path, "w") as rec:
                    rec.writelines(nums)
        
        else:
            edit_file = True
            record = str(num) + '\n'
            nums.append(record)
            nums.append("0\n")
            nums.append("0\n")
            with open(records_path, "w") as rec:
                rec.writelines(nums)

        log_data("Challenge counter event saved: " + str(num) + "\tin list: " + str(nums))
        log_data("Saved location: " + records_path)

        oled.challenge_records(nums, "reps", edit_file)
    
    def save_results_stopwatch(self, recorded_time, oled):
        records_path = "/home/pi/workoutPi/records/" + self.name + ".txt"
        edit_file = False
        times = list()

        if os.path.isfile(records_path):
            with open(records_path, 'r') as rec:
                times = rec.readlines()
                if lowest:
                    if recorded_time < float(times[0].rstrip('\n')) or float(times[0].rstrip('\n')) == 0:
                        times[2] = times[1]
                        times[1] = times[0]
                        times[0] = str(recorded_time) + '\n'
                        edit_file = True

                    elif recorded_time < float(times[1].rstrip('\n')) or float(times[1].rstrip('\n')) == 0:
                        times[2] = times[1]
                        times[1] = str(recorded_time) + '\n'
                        edit_file = True

                    elif recorded_time < float(times[2].rstrip('\n')) or float(times[2].rstrip('\n')) == 0:
                        times[2] = str(recorded_time) + '\n'
                        edit_file = True
                
                else:
                    if recorded_time > float(times[0].rstrip('\n')):
                        times[2] = times[1]
                        times[1] = times[0]
                        times[0] = str(recorded_time) + '\n'
                        edit_file = True

                    elif recorded_time > float(times[1].rstrip('\n')):
                        times[2] = times[1]
                        times[1] = str(recorded_time) + '\n'
                        edit_file = True

                    elif recorded_time > float(times[2].rstrip('\n')):
                        times[2] = str(recorded_time) + '\n'
                        edit_file = True

            if edit_file:
                with open(records_path, "w") as rec:
                    rec.writelines(times)
        
        else:
            edit_file = True
            record = str(recorded_time) + '\n'
            times.append(record)
            times.append("0\n")
            times.append("0\n")
            with open(records_path, "w") as rec:
                rec.writelines(times)

        oled.challenge_records(times, "sec", edit_file)
