one_goal = 0
two_goals = 0
three_goals = 0
ten_goals = 0
player1, player2, player3, player10 = "", "", "", ""
player = input()
while player != "END":
    goals_scored = int(input())

    if goals_scored >= 10:
        if goals_scored == ten_goals:
            player10 = player10
        else:
            player10 = player
            ten_goals = goals_scored
        break
    elif goals_scored >= 3:
        if goals_scored == three_goals:
            player3 = player3
        else:
            three_goals = goals_scored
            player3 = player
    elif goals_scored == 2:
        if goals_scored == two_goals:
            player2 = player2
        else:
            two_goals = 2
            player2 = player
    elif goals_scored == 1:
        if goals_scored == two_goals:
            player1 = player1
        else:
            one_goal = 1
            player1 = player
    player = input()

if ten_goals > three_goals:
    print(f"{player10} is the best player!")
    print(f"He has scored {ten_goals} goals and made a hat-trick !!!")
elif three_goals > two_goals:
    print(f"{player3} is the best player!")
    print(f"He has scored {three_goals} goals and made a hat-trick !!!")
elif two_goals > one_goal:
    print(f"{player2} is the best player!")
    print(f"He has scored {two_goals} goals.")
else:
    print(f"{player1} is the best player!")
    print(f"He has scored {one_goal} goals.")