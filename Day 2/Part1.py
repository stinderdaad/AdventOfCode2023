redCubes = 12
greenCubes = 13
blueCubes = 14

sumIds = 0

with open('Day 2/Input.txt') as f:
    lines = f.readlines()

for line in lines:
    possible = True
    blocks = line.split(':')

    # gameid
    idBlock = blocks[0].split(' ')
    gameID = int(idBlock[1])

    # hands
    hands = blocks[1].split(';')

    for hand in hands:
        cubes = hand.split(',')

        for cube in cubes:
            cube = cube.split(' ')
            amount = int(cube[1])
            color = cube[2]

            if color == "red" or color == "red\n":
                if amount > redCubes:
                    possible = False
            elif color == "green" or color == "green\n":
                if amount > greenCubes:
                    possible = False
            elif color == "blue" or color == "blue\n":
                if amount > blueCubes:
                    possible = False

    if possible:
        sumIds += gameID

print(sumIds)
