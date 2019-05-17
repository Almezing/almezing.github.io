# Black Jack

# Stages
#     Player Count
#     Dealing
#     Playing
#         Players Hit/Staying
#         Dealer Hit/Staying
#     Scoring
#         21 or over
#         Higher/Lower/Equal Dealer
# Deck
#     1-11
#     Track Numbers
#         Ace vs 1
#     Hands
#         *5 Card Charlie


# Gui 

import random

# players = input("Enter number of players: ")

# if not players:
#     print(True)
# else:
#     print(False)
playerHands_dict = {}

# try:
#     pass
# except ValueError: as identifier:
#     pass players :

# for i in range(int(players) + 1):
#     # print(eval(str(i > int(players) - 1)))
#     if i > int(players) - 1:
#         playerHands_dict["Dealer"] = 0
#     else:
#         playerHands_dict["Player " + str(i+1)] = 0
   
#print(eval(str(i+1)))

# print(playerHands_dict)
# TODO 
# print(sorted(playerHands_dict)[-1])


deck = []
hand = []
def deal(player_hand, dealt_card = 1):
    for new_card in range(0, dealt_card):
        no_more_cards = True
        if no_more_cards: 
            card = random.randint(1, 10)
            if deck.count(card) < 4 and len(deck) < 52:
                deck.append(card)
                player_hand.append(card)
                no_more_cards = True
            elif card == 10 and deck.count(card) < 16 and len(deck) < 52:
                deck.append(card)
                player_hand.append(card)
                no_more_cards = True
            else:
                no_more_cards = False
    return

hand.append(deal(player_hand = hand))
hand = hand[0:-1]
print('Hand' , hand, 'Deck', deck)
