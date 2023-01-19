days_tournament = int(input())

donation = 0
win_rate = 0
lose_rate = 0
win_tournament = 0
lose_tournament = 0
for i in range(days_tournament):

        while True:
            sport = input()

            if sport == "Finish":
                break

            while True:
                result = input()

                if result == "win":
                    win_rate += 1
                    donation += 20
                    win_tournament += 1
                    break
                elif result == "lose":
                    lose_tournament += 1
                    break
                break
        if win_rate > lose_rate:
            donation += donation * 0.1

if win_tournament > lose_tournament:
    donation += donation * 0.2
    print(f"You won the tournament! Total raised money: {donation:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {donation:.2f}")

