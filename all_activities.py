from exercise import Exercise
from challenge import Challenge

#red:intense, orange:moderate, yellow:easy, green:go, blue:get water, purple:yoga
#underscores will be added automatically, feel free to use spaces in activity names


'''
Challenges

Ex.                    Challenge("name", "style", "description", num_time_sec=60)

_stopwatch_ = Challenge(_stopwatch_, "stopwatch", "Do __ _____ as fast as possible")
_counter_ = Challenge(_counter_, "counter", "Do as many _____ as you can in ", __)
'''
push_up_stopwatch_10 = Challenge("push_up_stopwatch_10", "stopwatch", "Do 10 pushups as fast as possible")
push_up_stopwatch_15 = Challenge("push_up_stopwatch_15", "stopwatch", "Do 15 pushups as fast as possible")
push_up_stopwatch_20 = Challenge("push_up_stopwatch_20", "stopwatch", "Do 20 pushups as fast as possible")
push_up_counter_30s  = Challenge("push_up_counter_30s", "counter", "Do as many pushups as you can in 30 sec", 30)
push_up_counter_1m   = Challenge("push_up_counter_1m", "counter", "Do as many pushups as you can in 1 min", 60)

sit_up_stopwatch_20 = Challenge("sit_up_stopwatch_20", "stopwatch", "Do 20 situps as fast as possible")
sit_up_stopwatch_30 = Challenge("sit_up_stopwatch_30", "stopwatch", "Do 30 situps as fast as possible")
sit_up_counter_30s  = Challenge("sit_up_counter_30s", "counter", "Do as many situps as you can in 30 sec", 30)
sit_up_counter_1m   = Challenge("sit_up_counter_1m", "counter", "Do as many situps as you can in 1 min", 60)

burpees_stopwatch_10 = Challenge("burpees_stopwatch_10", "stopwatch", "Do 10 burpees as fast as possible")
burpees_stopwatch_15 = Challenge("burpees_stopwatch_15", "stopwatch", "Do 15 burpees as fast as possible")
burpees_counter_30s  = Challenge("burpees_counter_30s", "counter", "Do as many burpees as you can in 30 sec", 30)
burpees_counter_1m   = Challenge("burpees_counter_1m", "counter", "Do as many burpees as you can in 1 min", 60)


'''
Exercises

Ex.           Exercise("name", min, max, low_threshold, high_threshold, multiplier=1, yoga=False, style="num", unit="rep", challenges=list())
'''
push_up         = Exercise("Push Ups", 5, 15, 7, 11, challenges=[push_up_stopwatch_10, push_up_stopwatch_15, push_up_stopwatch_20, push_up_counter_30s, push_up_counter_1m])
sit_up          = Exercise("Sit Ups",  5, 30, 10, 20, multiplier=5, challenges=[sit_up_stopwatch_20, sit_up_stopwatch_30, sit_up_counter_30s, sit_up_counter_1m])
crunches        = Exercise("Crunches", 10, 40, 20, 30, multiplier=2)
jumping_jacks   = Exercise("Jumping Jacks", 10, 50, 25, 40, multiplier=5)
burpees         = Exercise("Burpees", 5, 15, 4, 10, challenges=[burpees_stopwatch_10, burpees_stopwatch_15, burpees_counter_30s, burpees_counter_1m])
planks          = Exercise("Plank", 30, 120, 30, 60, multiplier=30, style="time", unit="sec")
push_up_planks  = Exercise("Push Up Plank", 5, 10, 4, 6, challenges=[])

exercises = [push_up, sit_up, crunches, jumping_jacks, burpees]




"""
squats, lunges, bicyles, scissor kicks, curls, bench press, run/jog,
peck deck, downward dog, flutter kicks, superman, upward seal,
run in place, bicycle sit up, sit up with legs in the air, mountain climbers,
move weight side to side with knees in the air, stretches?, 

"""