from exercise import Exercise
from challenge import Challenge

"""
push ups, sit ups, crunches, jumping jacks, burpees, planks, push up planks,
squats, lunges, bicyles, scissor kicks, curls, bench press, run/jog,
peck deck, downward dog, flutter kicks, crunches, superman, upward seal,
run in place, bicycle sit up, sit up with legs in the air, mountain climbers,
move weight side to side with knees in the air, stretches?, 

"""

#red:intense, orange:moderate, yellow:easy, green:go, blue:get water, purple:yoga

#Ex. Exercise(name,  min, max, low_threshold, high_threshold, multiplier=1, yoga=False, style="num", unit="rep", challenges=list())
#    Challenge(name, style, description, num_time_sec=60)

push_up_stopwatch_10 = Challenge("push_up_stopwatch_10", "stopwatch", "Do 10 pushups as fast as possible")
push_up_stopwatch_15 = Challenge("push_up_stopwatch_15", "stopwatch", "Do 15 pushups as fast as possible")
push_up_stopwatch_20 = Challenge("push_up_stopwatch_20", "stopwatch", "Do 20 pushups as fast as possible")

push_up_counter_30s = Challenge("push_up_counter_30s", "counter", "Do as many pushups as you can in 30 sec", 3)  #TODO: make 3, 6 -> 30, 60
push_up_counter_1m = Challenge("push_up_counter_1m", "counter", "Do as many pushups as you can in 1 min", 6)

sit_up_stopwatch_20 = Challenge("sit_up_stopwatch_20", "stopwatch", "Do 20 situps as fast as possible")
sit_up_stopwatch_30 = Challenge("sit_up_stopwatch_30", "stopwatch", "Do 30 situps as fast as possible")

sit_up_counter_30s = Challenge("sit_up_counter_30s", "counter", "Do as many situps as you can in 30 sec", 3)
sit_up_counter_1m = Challenge("sit_up_counter_1m", "counter", "Do as many situps as you can in 1 min", 6)

push_up = Exercise("Push_Ups", 5, 6, 7, 12, challenges=[push_up_stopwatch_10, push_up_stopwatch_15, push_up_stopwatch_20, push_up_counter_30s, push_up_counter_1m])
sit_up  = Exercise("Sit_Ups",  1, 6, 2, 4, multiplier=5, challenges=[sit_up_stopwatch_20, sit_up_stopwatch_30, sit_up_counter_30s, sit_up_counter_1m])



exercises = [push_up]  #TODO: replace spaces with underscores, and have underscores removed when printing

