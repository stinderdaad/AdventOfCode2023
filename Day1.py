import re

# Part 1:
# with open('./Day1Input.txt') as f:
#     lines = f.readlines()

# number = 0

# for line in lines:
#     list = re.findall(r'\d', line)

#     number += int(list[0]) * 10 + int(list[-1])

# print(number)


# Part 2:
with open('./Day1Input.txt') as f:
    lines = f.readlines()

number = 0


def parseNumberFirst(num):
    numberMap = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                 "six": 6, "seven": 7, "eight": 8, "nine": 9}

    if num.isdigit():
        return int(num)
    else:
        return numberMap.get(num.lower(), None)


def parseNumberLast(num):
    numberMap = {"eno": 1, "owt": 2, "eerht": 3, "ruof": 4, "evif": 5,
                 "xis": 6, "neves": 7, "thgie": 8, "enin": 9}

    if num.isdigit():
        return int(num)
    else:
        return numberMap.get(num.lower(), None)


for line in lines:
    first = re.search(r'(?:one|two|three|four|five|six|seven|eight|nine|\d)',
                      line)
    last = re.search(r'(?:eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d)',
                     line[::-1])

    firstDigit = parseNumberFirst(first.group(0)) * 10
    secondDigit = parseNumberLast(last.group(0))
    number += firstDigit + secondDigit

print(number)
