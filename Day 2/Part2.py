sumIds = 0

with open('Day 2/Input.txt') as f:
    lines = f.readlines()


for line in lines:
    minRed = 0
    minGreen = 0
    minBlue = 0

    blocks = line.split(':')

    # hands
    hands = blocks[1].split(';')

    for hand in hands:
        cubes = hand.split(',')

        for cube in cubes:
            cube = cube.split(' ')
            amount = int(cube[1])
            color = cube[2]

            if color == "red" or color == "red\n":
                if amount > minRed:
                    minRed = amount
            elif color == "green" or color == "green\n":
                if amount > minGreen:
                    minGreen = amount
            elif color == "blue" or color == "blue\n":
                if amount > minBlue:
                    minBlue = amount

    power = minRed * minGreen * minBlue
    sumIds += power

print(sumIds)
