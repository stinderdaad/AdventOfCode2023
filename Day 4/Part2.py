copies = [1]*208

with open('Day 4/Input.txt') as f:
    cards = f.readlines()

for card in cards:
    blocks = card.split(':')
    cardID = blocks[0].split(' ')[-1]
    cardPosition = int(cardID) - 1
    numberOfCopies = copies[cardPosition]
    numbers = blocks[1].split('|')
    winningNumbers = numbers[0].split(' ')
    cardNumbers = numbers[1].strip().split(' ')

    winningCardNumbers = [number for number in cardNumbers if number in winningNumbers and number != '']

    if len(winningCardNumbers) > 0:
        i = 0
        for copy in copies[cardPosition:cardPosition + len(winningCardNumbers)]:
            copies[cardPosition + i] += 1 * numberOfCopies
            i += 1

print(copies)

print(sum(copies))
