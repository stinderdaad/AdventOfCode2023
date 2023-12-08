product = 1

with open('Day 6/Input.txt') as f:
    input = f.readlines()

timesTemp = input[0].split(':')[-1].strip().split(' ')
distancesTemp = input[1].split(':')[-1].strip().split(' ')
times = [x for x in timesTemp if x != '']
distances = [x for x in distancesTemp if x != '']

amountOfGames = 0
if len(times) == len(distances):
    amountOfGames = len(times)

games = []
for gameNumber in range(amountOfGames):
    games.append((times[gameNumber], distances[gameNumber]))

for game in games:
    time = int(game[0])
    distance = int(game[1])
    possibleWins = 0
    buttonHoldTime = 0
    speed = 0

    while buttonHoldTime < time:
        if speed * (time - buttonHoldTime) > distance:
            possibleWins += 1
            print('Win with ' + str(buttonHoldTime) + ' holdtime and ' + str(speed) + ' speed, distance: ' + str(speed * (time - buttonHoldTime)))
        buttonHoldTime += 1
        speed += 1

    print('Possible wins: ' + str(possibleWins))
    product *= possibleWins

print(product)
