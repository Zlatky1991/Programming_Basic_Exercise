# Предстои Великден и едно от най-вълнуващите неща е боядисването на яйца. Наличните цветове за боядисване са:
# • червено (red)
# • оранжев (orange)
# • син (blue)
# • зелен (green)
# Напишете програма, която изчислява какъв е броят на яйцата от всеки цвят и от кой цвят яйцата са най - много, като знаете общия им брой и цвета на всяко яйце.
# Вход
# От конзолата се чете 1 ред:
# • Броят на боядисаните яйца – цяло число в интервала [1 ... 100]
# За всяко яйце се чете:
#  Цветът на яйцето – текст с възможности: "red", "orange", "blue", "green"

number_of_paint_eggs = int(input())

green = 0
red = 0
orange = 0
blue = 0
# green, red, orange, blue = 0, 0, 0, 0 пак се изброяват, само че на един ред вместо на отделен
color = ""

for count in range(number_of_paint_eggs):
    color_of_egg = input()

    if color_of_egg == "red":
        red += 1
    elif color_of_egg == "orange":
        orange += 1
    elif color_of_egg == "blue":
        blue += 1
    elif color_of_egg == "green":
        green += 1

max_number = max(orange, blue, red, green)

if red == max_number:
    color = red
elif green == max_number:
    color = green
elif orange == max_number:
    color = orange
elif blue == max_number:
    color = blue

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_number} -> {color}")