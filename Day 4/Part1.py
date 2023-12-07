sumPoints = 0

with open('Day 4/Input.txt') as f:
    cards = f.readlines()

for card in cards:
    blocks = card.split(':')
    numbers = blocks[1].split('|')
    winningNumbers = numbers[0].split(' ')
    cardNumbers = numbers[1].strip().split(' ')

    winningCardNumbers = [number for number in cardNumbers if number in winningNumbers and number != '']

    points = 0
    if len(winningCardNumbers) > 0:
        points = 1
        for number in winningCardNumbers[1:]:
            points *= 2

    print(points)
    sumPoints += points

print(sumPoints)
