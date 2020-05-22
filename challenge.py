import os
from time import time

from gpiozero import Button, RGBLED, Buzzer
from colorzero import Color

from oled import OLED

class Challenge:
    def __init__(self, name, style, description, num_time=60):
        """
        name: name of the challenge to save to text file (str)
        style: how long it takes to do activity ("stopwatch") or how many done in timeframe ("counter")   (str)
        num_time: time for "counter" challenges (int)
        description: text to output to OLED display for challenge (str)
        """
        
        self.name = name
        self.style = style
        self.num_time = num_time
        self.description = description
    
    def save_results_counter(self, button, oled):
        records_path = "/home/pi/workoutPi/records/" + self.name
        edit_file = False
        nums = list()

        collecting = True
        num = 0
        print(num)
        oled.show_num(num)

        while collecting:
            button.wait_for_press()
            start = time()
            while button.is_pressed:
                sleep(0.01)
            if time() - start > 1.5:
                collecting = False
            else:
                num += 1
                print(num)
                oled.show_num(num)

        if os.path.getsize(records_path) > 0:
            with open(records_path, 'r') as rec:
                nums = rec.readlines()
                if recorded_time > int(nums[0].rstrip('\n')):
                    nums[2] = nums[1]
                    nums[1] = nums[0]
                    nums[0] = str(recorded_time) + '\n'
                    edit_file = True

                elif recorded_time > int(nums[1].rstrip('\n')):
                    nums[2] = nums[1]
                    nums[1] = str(recorded_time) + '\n'
                    edit_file = True

                elif recorded_time > int(nums[2].rstrip('\n')):
                    nums[2] = str(recorded_time) + '\n'
                    edit_file = True

            if edit_file:
                with open(records_path, "w") as rec:
                    rec.writelines(nums)
        
        else:
            record = str(recorded_time) + '\n'
            nums.append(record)
            nums.append("0\n")
            nums.append("0\n")
            with open(records_path, "w") as rec:
                rec.writelines(nums)

        #TODO: oled.multiline print all elements of times
    
    def save_results_stopwatch(self, recorded_time, oled):
        records_path = "/home/pi/workoutPi/records/" + self.name    #TODO: make sure records directory is added to .git_ignore
        edit_file = False
        times = list()

        if os.path.getsize(records_path) > 0:
            with open(records_path, 'r') as rec:
                times = rec.readlines()
                if recorded_time > int(times[0].rstrip('\n')):
                    times[2] = times[1]
                    times[1] = times[0]
                    times[0] = str(recorded_time) + '\n'
                    edit_file = True

                elif recorded_time > int(times[1].rstrip('\n')):
                    times[2] = times[1]
                    times[1] = str(recorded_time) + '\n'
                    edit_file = True

                elif recorded_time > int(times[2].rstrip('\n')):
                    times[2] = str(recorded_time) + '\n'
                    edit_file = True

            if edit_file:
                with open(records_path, "w") as rec:
                    rec.writelines(times)
        
        else:
            record = str(recorded_time) + '\n'
            times.append(record)
            times.append("0\n")
            times.append("0\n")
            with open(records_path, "w") as rec:
                rec.writelines(times)

        #TODO: oled.multiline print all elements of times
"""
TODO:

    def retrieve_results(self):
        pass  #similar to above, but collect old results and print to screen
            #do special effects with buzzer/lights/display if beat records
"""