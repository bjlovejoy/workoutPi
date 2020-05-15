import os
from time import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

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
    
    def record_score(self, button):

        collecting = True
        num = 0
        print(num)

        while collecting:
            start = time()
            button.wait_for_press()
            if time() - start < 2:
                collecting = False
            else:
                num += 1
                print(num)
            sleep(0.15)
    
    def save_results_stopwatch(self, name, recorded_time):
        records_path = "/home/pi/workoutPi/records/" + name
        edit_file = False
        times = list()

        if os.path.getsize(fullpathhere) > 0:
            with open(records_path, 'r') as rec:
                times = rec.readlines()
                if recorded_time > int(times[0].rstrip('\n')):    #TODO: fix list handling and newlines/writing
                    times[0] = str(recorded_time) + '\n'
                    edit_file = True

                elif recorded_time > int(times[1].rstrip('\n')):
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



    def retrieve_results(self):
        pass  #similar to above, but collect old results and print to screen
            #do special effects with buzzer/lights/display if beat records