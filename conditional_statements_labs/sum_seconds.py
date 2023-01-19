
first_runner = int(input())
second_runner = int(input())
third_runner = int(input())

total_time = first_runner + second_runner + third_runner

minutes = total_time // 60
seconds = total_time % 60

if seconds < 10:
    print(f'{minutes}:0{seconds:}')
else:
    print(f'{minutes}:{seconds:}')