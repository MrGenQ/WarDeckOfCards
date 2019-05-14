import random


def shuffled_deck(deck):
    random.shuffle(deck)
    return deck


def deal_cards(deck, card):
    player = deck[card]
    return player


def main_cycle(deck, win1, win2):
    while len(deck) > 0:
        card = 0
        deck = shuffled_deck(deck)
        player1 = deal_cards(deck, card)
        pl1 = compar.get(player1)
        deck.pop(card)
        player2 = deal_cards(deck, card)
        pl2 = compar.get(player2)
        deck.pop(card)
        print("First player's card: ", player1)
        print("Second player's card: ", player2)

        if pl1 > pl2:
            win1 += 1
            print(player1, " ", "First player wins")
        elif pl1 < pl2:
            win2 += 1
            print(player2, " ", "Second player wins")
        elif pl1 == pl2:
            print("It's a Tie")

    print("First player won - ", win1, " times")
    print("Second player won - ", win2, " times")


def compare_cards(C1, C2, deck, compar):
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


if __name__ == "__main__":

    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']*4
    value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    global compar
    compar = dict(zip(deck, value))
    print(compar)
    player1 = ' '
    player2 = ' '
    win1 = 0
    win2 = 0
    main_cycle(deck, win1, win2