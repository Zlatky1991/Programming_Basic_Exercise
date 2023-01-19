steps_to_goal = 0
command = ""
steps_going_home = 0
while True:
    steps_walking = input()

    if steps_walking == "Going home":
        steps_to_goal += steps_walking
        if steps_going_home >= 10000:
            steps_going_home -= 10000
            print(f"Goal reached! Good job!")
            print(f"{steps_going_home} steps over the goal!")
        else:
            print(f"{abs(steps_going_home - 10000)} more steps to reach goal.")
        break
    elif steps_walking != "Going home":
        steps_walking = int(steps_walking)
        steps_to_goal += steps_walking
        if steps_to_goal >= 10000:
            steps_to_goal -= 10000
            print(f"Goal reached! Good job!")
            print(f"{steps_to_goal} steps over the goal!")
            break
        steps_going_home += steps_to_goal

