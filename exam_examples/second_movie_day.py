pics_time = int(input())
number_of_scenes = int(input())
scenes_duration = int(input())

field_preparation = pics_time * 0.15
time_to_shoot_the_scenes = number_of_scenes * scenes_duration
#Останалото време да се закръгли до най-близкото цяло число.
needed_time = round(time_to_shoot_the_scenes + field_preparation)
diff = abs(needed_time - pics_time)

if needed_time > pics_time:
    print(f"You managed to finish the movie on time! You have {diff} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {diff} minutes.")

