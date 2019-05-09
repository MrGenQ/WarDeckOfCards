import random

deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']*4
player1 = ' '
player2 = ' '
card = 0


def shuffled_deck(deck):
    random.shuffle(deck)
    return deck


def deal_cards(deck, card):
    player = deck[card]
    return player


##deck = shuffled_deck(deck)
##print (deck)

while len(deck) > 0:
    deck = shuffled_deck(deck)
    player1 = deal_cards(deck, card)
    deck.pop(card)
    player2 = deal_cards(deck, card)
    deck.pop(card)
    print ("Pirmojo žaidėjo korta: ", player1)
    print ("Antrojo žaidėjo korta: ", player2)

    if player1 > player2:
        print (player1, " ", "Laimi pirmasis žaidėjas")
    elif player1 < player2:
        print (player2, " ", "Laimi antrasis žaidėjas")
    elif player1 == player2:
        print ("Lygiosios")

#def Value_of_card(deck, card):