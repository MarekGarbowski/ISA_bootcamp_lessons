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
        while True:
            quantity = int(input("Ile chcesz wylosować kart: "))
            player_cards = Cards.cards
            drawn_cards = []
            random.shuffle(player_cards)
            for card in range(quantity):
                temp = player_cards.pop()
                drawn_cards.append(temp)
                random.shuffle(player_cards)
            return drawn_cards


cards = Cards()
print(cards.shuffle())
# print(cards.shuffle())
