import random
import logging
import logging.config



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
        logger.info("First player's card: %s", player1)
        logger.info("Second player's card: %s", player2)

        if pl1 > pl2:
            win1 += 1
            logger.info("First player wins with a card: %s", player1)
        elif pl1 < pl2:
            win2 += 1
            logger.info("Second player wins with a card: %s", player2)
        elif pl1 == pl2:
            logger.info("It's a Tie")

    logger.info("First player won - %s", win1)
    logger.info("Second player won - %s", win2)


def compare_cards(C1, C2, deck, compar):
    if C1 not in deck:
        raise ValueError("The card doesn't exist")
    C1 = compar.get(C1)
    C2 = compar.get(C2)
    if C1 < C2:
        return 1
    elif C1 > C2:
        return 0
    elif C1 == C2:
        return -1  


if __name__ == "__main__":

    logging.basicConfig(level = logging.INFO, filename='logging', filemode='w')
    logger = logging.getLogger(" ")
    admin_handler = logging.FileHandler('logging')
    admin_handler.setLevel(logging.INFO)
    logger.addHandler(admin_handler)
    logger.warning(f'{admin_handler} started the program')
    logger.info('The GAME has started')


    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']*4
    value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    global compar
    compar = dict(zip(deck, value))
    player1 = ' '
    player2 = ' '
    win1 = 0
    win2 = 0
    main_cycle(deck, win1, win2)
    logger.info('The GAME has ended')

