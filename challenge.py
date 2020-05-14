from time import time

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
    
    def display(self):
        print(description)
        #for time challenges, show either count-down or "Press to stop"
        #TODO: use OLED
    
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
    
    def save_results(self):
        pass  #use open to save in unique file (save top 3-5)
    
    def retrieve_results(self):
        pass  #similar to above, but collect old results and print to screen
            #do special effects with buzzer/lights/display if beat records