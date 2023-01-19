bad_grade = int(input())

count_score = 0
count_bad_grade = 0
count_grade = 0
last_problem = ""
flag = True

while True:
    name_task = input()

    if name_task == "Enough":
        break
    current_grade = int(input())
    count_grade += 1
    count_score += current_grade
    last_problem = name_task

    if current_grade <= 4:
        count_bad_grade += 1
        if count_bad_grade == bad_grade:
            flag = False
            break

if flag:
    print(f"Average score: {count_score / count_grade:.2f}")
    print(f"Number of problems: {count_grade}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {count_bad_grade} poor grades.")