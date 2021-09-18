import random


class Cards:
    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"]
    values = ["2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]
    cards = []
    for color in suits:
        for card in values:
            cards.append((color, card))

    def shuffle(self):
        quantity = int(input("Ile chcesz wylosować kart: "))
        cards = Cards.cards
        drawned_cards = []
        random.shuffle(cards)
        for card in range(quantity):
            temp = cards.pop()
            drawned_cards.append(temp)
            random.shuffle(cards)
        print(cards)
        return drawned_cards


cards = Cards()
print(cards.shuffle())
print(cards.shuffle())
