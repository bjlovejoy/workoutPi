from gpiozero import Button, LED, PWMLED, RGBLED, Buzzer
from gpiozero.tones import Tone
from time import time, sleep
from random import randint
#from oled import

led = RGBLED(red=17, green=27, blue=22)

"""
push ups, sit ups, jumping jacks, burpees, planks, push up planks,
squats, lunges, bicyles, scissor kicks, curls, bench press, run/jog,
peck deck, downward dog, flutter kicks, crunches, superman, upward seal,
run in place, bicycle sit up, sit up with legs in the air, mountain climbers,
move weight side to side with knees in the air, stretches?, 

"""

#for most, blink 3 times in color of activity type and play buzzer 3 times
#for reminders, play buzzer once, but still with 3 blinks
#in meantime, turn led on and off every 1 second (use built-in blink feature)
#red:intense, orange:moderate, yellow:easy, green:go, blue:get water, purple:yoga

#include display for water

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
    if generated_num > self.max:
      pass #do challenge stuff, scale down to use as index for list
    
    else:
      num = int(generated_num/self.increment) * self.increment
      self.display(num)
      
  def handle_challenge(self):
    pass
    
class Challenge:
  def __init__(self, style, description):
    self.style = style
    self.description = description
  
  def display(self):
    print(description)
    #for time challenges, show either count-down or "Press to stop"
  
  
exercises = [Exercise("Push-Ups", 5, 20, 1, 5, 10), Exercise("Sit Ups", 5, 30)]
num_exercises = len(exercises)


interval_min = 15
interval_time = interval_min * 60  #need to delay between 10-20 minutes based on exercise intensity
start_time = time()

def main():
  while True:

    if time() - start_time > interval_time:  #use minutes
      #do stuff here
      #flash light color of intensity and sound buzzer occasionally until button is pressed
      activity = exercises[randint(0, num_exercises-1)]
      info = activity.generate_rand_reps

      num_reps  = info[0]  #number of reps
      intensity = info[1]  #intensity
      #need to light, buzzer and display

      start_time = time()

    sleep(1)

if __name__ = "__main__":
  main()
