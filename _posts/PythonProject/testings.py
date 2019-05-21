# Black Jack

# Stages
#     Players 
#         Count
#     Dealing
#         Deck 
#             1-10
#             Track cards
#             Ace vs 11
#     Playing
#         Hands
#             5 Card Charlie
#         Players Hit/Staying
#         Dealer Hit/Staying
#     Scoring
#         21 or over
#         Higher/Lower/Equal Dealer
# Gui 

import random

# force user to impot an integer
while True:
    try:
        players = int(input("How many players "))
        break
    except ValueError:
        print("Valid number required. Try again..")

allHands_dict = {}
deck = []

def dealCard(dealt_card = 1):
    """
    docstring here
        :param dealt_card=1: 

        returns a random card to the players hand.
        builds deck to track how many cards were dealt
        all face cards treated as 10
    """
    for new_card in range(0, dealt_card):
        no_more_cards = True
        if no_more_cards: 
            card = random.randint(1, 10)
            if deck.count(card) < 4 and len(deck) < 52:
                deck.append(card)
                # player_hand.append(card)
                no_more_cards = True
                return card
            elif card == 10 and deck.count(card) < 16 and len(deck) < 52:
                deck.append(card)
                # player_hand.append(card)
                no_more_cards = True
                return card
            else:
                no_more_cards = False
                return None
        else:
            return None

allHands_dict = {"Player " + str(i): [] for i in (range(1, players + 1))}
allHands_dict["Dealer"] = []

# TODO dealCard() returns any thing, dispite it having a limit
for i in range(1000):
    allHands_dict["Player 1"].append(dealCard())

allHands_dict["Player 1"] = list(filter(None, allHands_dict["Player 1"]))
# print(type(allHands_dict))
print(len(allHands_dict["Player 1"]), allHands_dict["Player 1"])


selenium
beautifulsoup4
splinter
time
