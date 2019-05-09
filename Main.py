import random

deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']*4
value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
compar = dict (zip(deck, value))
print (compar)
player1 = ' '
player2 = ' '


def shuffled_deck(deck):
    random.shuffle(deck)
    return deck


def deal_cards(deck, card):
    player = deck[card]
    return player

while len(deck) > 0:
    card = 0
    deck = shuffled_deck(deck)
    player1 = deal_cards(deck, card)
    pl1 = compar.get(player1)
    deck.pop(card)
    player2 = deal_cards(deck, card)
    pl2 = compar.get(player2)
    deck.pop(card)
    print ("Pirmojo žaidėjo korta: ", player1)
    print ("Antrojo žaidėjo korta: ", player2)

    if pl1 > pl2:
        print (player1, " ", "Laimi pirmasis žaidėjas")
    elif pl1 < pl2:
        print (player2, " ", "Laimi antrasis žaidėjas")
    elif pl1 == pl2:
        print ("Lygiosios")


def test_compare_cards():
    assert compare_cards('J', 'A') == 1
    assert compare_cards('8', '10') == 1
    assert compare_cards('J', '2') == 0
    assert compare_cards('K', 'K') == -1


def compare_cards(C1, C2):
    if C1 not in deck:
        raise ValueError("Netinkama korta")
    C1 = compar.get(C1)
    C2 = compar.get(C2)
    if C1 < C2:
        return 1
    elif C1 > C2:
        return 0
    elif C1 == C2:
        return -1 

    
test_compare_cards()


