import re

with open('Day 1/Input.txt') as f:
    lines = f.readlines()

number = 0

for line in lines:
    list = re.findall(r'\d', line)

    number += int(list[0]) * 10 + int(list[-1])

print(number)
