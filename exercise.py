
from gpiozero import Button, RGBLED, Buzzer
from time import time, sleep

class Exercise:

    def __init__(self, name, min, max, increment=1, low_threshold=None, high_threshold=None, yoga=False, challenges=list()):
        """
        name: name of the exercise/activity (str)
        min/max: lowest/highest number of reps (int)
        increment: ensures number of reps is a multiple of this number (1, 2, 5, 10, etc.) (int)
        low_threshold: between easy and moderate activities (number is included in easy) (int)
        high_threshold: between moderate and vigorous activities (number is included in moderate) (int)
        yoga: if the exercise is a yoga activity (bool)
        challenges: a list of Challenge objects (list)
        """

        self.name           = name
        self.min            = min   #TODO: if min is less than increment, set to increment
        self.max            = max
        self.increment      = increment
        self.low_threshold  = low_threshold
        self.high_threshold = high_threshold
        self.yoga           = yoga
        self.challenges     = challenges

        self.num_challenges = len(challenges)
        self.max_total      = self.max + self.num_challenges  #to be used for random number generation
    
    def display(self, num):
        print(num, "\t", self.name, sep="")
  
    def wait_for_input(self, intensity, led, button, buzzer):
        
        num = 0
        button_pressed = False
        colors = ["red", "orange", "yellow", "green", "blue", "purple", "white"]

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

        while not button_pressed:

            if time() - start > delay:
                buzzer.on()
                sleep(0.2)
                buzzer.off()
                sleep(0.2)
            else:
                led.on()
                sleep(0.2)
                button_pressed = button.is_pressed
                led.off()
                sleep(0.5)
  
    def generate_rand_reps(self):
        
        generated_num = randint(self.min, self.max_total)
        intensity = None
        
        if self.yoga:
            intensity = "yoga"
        
        elif generated_num > self.max:
            intensity = "challenge"
            generated_num -= self.max + 1  #convert into index to access challenges list
        
        else:
            if generated_num > high_threshold:
                intensity = "vigorous"
            elif generated_num > low_threshold:
                intensity = "moderate"
            else:
                intensity = "easy"
        
        return (generated_num, intensity)
    
    def handle_regular(self):
        num = int(generated_num/self.increment) * self.increment
        self.display(num)
      
    def handle_challenge(self):
        pass