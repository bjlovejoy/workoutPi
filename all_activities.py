from exercise import Exercise
from challenge import Challenge

#red:intense, orange:moderate, yellow:easy, green:go, blue:get water, purple:yoga
#underscores will be added automatically, feel free to use spaces in activity names


'''
Challenges

Ex.                    Challenge("name", "style", "description", num_time_sec=60, lowest=True)

_stopwatch_ = Challenge(_stopwatch_, "stopwatch", "Do __ _____ as fast as possible")
_counter_ = Challenge(_counter_, "counter", "Do as many _____ as you can in ", __)
'''
push_up_stopwatch_10 = Challenge("push_up_stopwatch_10", "stopwatch", "Do 10 pushups as fast as possible")
push_up_stopwatch_15 = Challenge("push_up_stopwatch_15", "stopwatch", "Do 15 pushups as fast as possible")
push_up_stopwatch_20 = Challenge("push_up_stopwatch_20", "stopwatch", "Do 20 pushups as fast as possible")
push_up_counter_30s  = Challenge("push_up_counter_30s", "counter", "Do as many pushups as you can in 30 sec", 30)
push_up_counter_1m   = Challenge("push_up_counter_1m", "counter", "Do as many pushups as you can in 1 min", 60)

burpees_stopwatch_10 = Challenge("burpees_stopwatch_10", "stopwatch", "Do 10 burpees as fast as possible")
burpees_stopwatch_15 = Challenge("burpees_stopwatch_15", "stopwatch", "Do 15 burpees as fast as possible")
burpees_counter_1m   = Challenge("burpees_counter_1m", "counter", "Do as many burpees as you can in 1 min", 60)
burpees_counter_90s  = Challenge("burpees_counter_90s", "counter", "Do as many burpees as you can in 90 sec", 30)

sit_up_stopwatch_20 = Challenge("sit_up_stopwatch_20", "stopwatch", "Do 20 situps as fast as possible")
sit_up_stopwatch_30 = Challenge("sit_up_stopwatch_30", "stopwatch", "Do 30 situps as fast as possible")
sit_up_counter_30s  = Challenge("sit_up_counter_30s", "counter", "Do as many situps as you can in 30 sec", 30)
sit_up_counter_1m   = Challenge("sit_up_counter_1m", "counter", "Do as many situps as you can in 1 min", 60)

butterfly_stopwatch = Challenge("butterfly_stopwatch", "stopwatch", "How long can you butterfly kick?", lowest=False)
scissor_stopwatch   = Challenge("scissor_stopwatch", "stopwatch", "How long can you scissor kick?", lowest=False)
bicycle_counter_30s = Challenge("bicycle_counter_30s", "counter", "Do as many bicycle crunches in 30s", 30)
bicycle_counter_60s = Challenge("bicycle_counter_60s", "counter", "Do as many bicycle crunches in 60s", 60)
leg_raise_counter   = Challenge("leg_raise_counter", "counter", "Do as many leg raises as you can, no time limit", 1)

wall_sit_stopwatch  = Challenge("wall_sit_stopwatch", "stopwatch", "How long can you wall sit?", lowest=False)
dips_counter_30s    = Challenge("dips_counter_30s", "counter", "Do as many tricep dips in 30s", 30)
dips_counter_60s    = Challenge("dips_counter_60s", "counter", "Do as many tricep dips in 60s", 60)

lap_stopwatch_1     = Challenge("lap_stopwatch_1", "stopwatch", "1 lap around house, 1/10 mile")
lap_stopwatch_2     = Challenge("lap_stopwatch_2", "stopwatch", "2 laps around house, 1/5 mile")
lap_stopwatch_5     = Challenge("lap_stopwatch_5", "stopwatch", "5 laps around house, 1/2 mile")
lap_stopwatch_10    = Challenge("lap_stopwatch_10", "stopwatch", "10 laps around house, 1 mile")

curl_counter        = Challenge("curl_counter", "counter", "Do as many curls as you can, no time limit", 1)

'''
Exercises

Ex.           Exercise("name", min, max, low_threshold, high_threshold, multiplier=1, yoga=False, style="num", unit="rep", challenges=list())
'''

#Strength
push_ups            = Exercise("Push Ups", 5, 20, 7, 11, challenges=[push_up_stopwatch_10, push_up_stopwatch_15, push_up_stopwatch_20, push_up_counter_30s, push_up_counter_1m])
push_up_planks      = Exercise("Push Up Plank", 3, 10, 4, 6)
planks              = Exercise("Plank", 30, 120, 30, 60, multiplier=30, style="time", unit="sec")
jumping_jacks       = Exercise("Jumping Jacks", 10, 50, 25, 40, multiplier=5)
mountain_climbers   = Exercise("Mountain Climbers", 10, 40, 15, 25)
burpees             = Exercise("Burpees", 5, 15, 4, 9, challenges=[burpees_stopwatch_10, burpees_stopwatch_15, burpees_counter_1m, burpees_counter_90s])

#Core
crunches            = Exercise("Crunches", 10, 40, 20, 30, multiplier=2)
sit_ups             = Exercise("Sit Ups",  5, 30, 10, 20, multiplier=5, challenges=[sit_up_stopwatch_20, sit_up_stopwatch_30, sit_up_counter_30s, sit_up_counter_1m])
v_situp             = Exercise("V Situp", 5, 25, 10, 15, multiplier=5)
dead_bug            = Exercise("Dead Bug", 10, 30, 15, 20, multiplier=5)
cross_punch_situps  = Exercise("Cross Punch Situps", 5, 25, 10, 15, multiplier=5)
butterfly           = Exercise("Butterfly Kicks", 10, 60, 15, 30, multiplier=5, style="time", unit="sec", challenges=[butterfly_stopwatch])
scissor             = Exercise("Scissor Kicks", 10, 60, 15, 30, multiplier=5, style="time", unit="sec", challenges=[scissor_stopwatch])
bicycle_crunches    = Exercise("Bicycle Crunches", 5, 25, 10, 15, multiplier=5, challenges=[bicycle_counter_30s, bicycle_counter_60s])
leg_raises          = Exercise("Leg Raises", 10, 30, 15, 20, challenges=[leg_raise_counter])

#Stretch
squats              = Exercise("Squats", 10, 30, 15, 20)
jump_squats         = Exercise("Jump Squats", 5, 25, 10, 20)
high_knees          = Exercise("High Knees", 10, 30, 20, 35, multiplier=5)
wall_sit            = Exercise("Wall Sit", 15, 90, 30, 60, multiplier=5, style="time", unit="sec", challenges=[wall_sit_stopwatch])
lunges              = Exercise("Lunges", 10, 20, 15, 30)
#Tricep dip - grab surface behind you and repeatedly lower and raise your body (similar to pushup)
tricep_dips         = Exercise("Tricep Dips", 10, 30, 15, 20, challenges=[dips_counter_30s, dips_counter_60s])
russian_twists      = Exercise("Russian Twists", 10, 30, 15, 25)

#Yoga
downward_dog        = Exercise("Downward Dog", 10, 60, 0, 0, multiplier=5, yoga=True, style="time", unit="sec")
superman            = Exercise("Superman", 10, 60, 0, 0, multiplier=5, yoga=True, style="time", unit="sec")
upward_seal         = Exercise("Upward Seal", 10, 60, 0, 0, multiplier=5, yoga=True, style="time", unit="sec")

#Cardio
jog_run             = Exercise("Jog/Run in Place", 30, 120, 60, 90, multiplier=10, style="time", unit="sec")
house_run           = Exercise("Run Around House", 1, 5, 1, 2, challenges=[lap_stopwatch_1, lap_stopwatch_2, lap_stopwatch_5, lap_stopwatch_10])

#Weights
curls               = Exercise("Curls", 5, 20, 10, 15, challenges=[curl_counter])
peck_deck           = Exercise("Peck Deck", 10, 30, 15, 23)



exercises = [push_ups, push_up_planks, planks, jumping_jacks, mountain_climbers, burpees,
            crunches, sit_ups, v_situp, dead_bug, cross_punch_situps, butterfly, scissor, bicycle_crunches, leg_raises,
            squats, jump_squats, high_knees, wall_sit, lunges, tricep_dips, russian_twists,
            downward_dog, superman, upward_seal,
            jog_run, house_run,
            curls, peck_deck]


