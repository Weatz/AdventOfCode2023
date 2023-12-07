strengthOrder = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def ParseInput(lines):
    handBid = []
    for line in lines:
        splittedLine = line.split(" ")
        handBid.append((splittedLine[0], int(splittedLine[1])))
    return handBid


'''
Forces : 
    0 : High card
    1 : One Pair
    2 : Two Pair
    3 : Three of a kind
    4 : Full house
    5 : Four of a kind
    6 : Five of a kind
'''
def FindStrength(hand):
    cards = {}
    for character in hand:
        if(character in cards):
            cards[character] = cards[character] + 1
        else:
            cards[character] = 1
    if(len(cards) == 1):
        return 6
    if(len(cards) == 5):
        return 0
    if(len(cards) == 4):
        return 1
    if(len(cards) == 2):
        if(max(cards.values()) == 4):
            return 5
        return 4
    if(max(cards.values()) == 3):
        return 3
    return 2




def Part1(lines):
    hands = ParseInput(lines)
    handStrenghts = [[] for i in range(7)]
    for hand in hands:
        handStrenghts[FindStrength(hand[0])].append(hand)
    print(handStrenghts)
    sortedHands = []
    for tab in handStrenghts:
        tab.sort(key=lambda hand:[strengthOrder.index(c) for c in hand[0]])
        sortedHands.append(tab)
    print(sortedHands)
    sum = 0
    rank = 1
    for tab in sortedHands:
        for hand in tab:
            print(hand, rank)
            sum += hand[1] * rank
            rank += 1

    print(sum)



f = open("Day7/data7.txt", "r")
lines = f.readlines()
Part1(lines)