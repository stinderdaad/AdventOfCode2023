# did not work, don't feel like finishing it rn


# list of rows
rows, cols = (141, 141)
grid = [[0]*cols]*rows

total = 0


# checks left, and left diagonals
def checkLeftAndDiagonals(x, y):
    value = x - 1
    if grid[value][y] != '.':
        return True
    elif grid[x - 1][y - 1] != '.':
        return True
    elif grid[x - 1][y + 1] != '.':
        return True
    else:
        return False


# checks right, and right diagonals
def checkRightAndDiagonals(x, y):
    if grid[x + 1][y] != '.':
        return True
    elif grid[x + 1][y - 1] != '.':
        return True
    elif grid[x + 1][y + 1] != '.':
        return True
    else:
        return False


# checks up and down
def checkUpAndDown(x, y):
    if grid[x][y - 1] != '.':
        return True
    elif grid[x][y + 1] != '.':
        return True
    else:
        return False


with open('Day 3/Input.txt') as f:
    lines = f.readlines()

i = 0
for line in lines:
    j = 0
    for character in line:
        grid[i][j] = character
        j += 1
    i += 1

i = 0
for y in grid:
    number = 0
    locations = []
    j = 0
    for x in y:
        if x.isdigit():
            number *= 10
            number += int(x)
            locations.append((j, i))
        else:
            if number != 0:
                frst = locations[0]
                last = locations[-1]
                if checkLeftAndDiagonals(frst[0], frst[1]):
                    total += number
                    number = 0
                elif checkRightAndDiagonals(last[0], last[1]):
                    total += number
                    number = 0
                else:
                    for location in locations:
                        if checkUpAndDown(location[0], location[1]):
                            total += number
                            number = 0
                    number = 0
        j += 1
    i += 1

print(total)
