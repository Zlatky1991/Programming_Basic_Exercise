team_points = 0

football_team = input()
games_played = int(input())
wins = 0
draws = 0
lose = 0

for num in range(games_played):
    result = input()

    if result == "W":
        team_points += 3
        wins += 1
    elif result == "D":
        team_points += 1
        draws += 1
    elif result == "L":
        team_points = team_points
        lose += 1

if games_played == 0:
    print(f"{football_team} hasn't played any games during this season.")
else:
    percent_games_won = (wins * 100) / games_played
    print(f"{football_team} has won {team_points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {lose}")
    print(f"Win rate: {percent_games_won:.2f}%")