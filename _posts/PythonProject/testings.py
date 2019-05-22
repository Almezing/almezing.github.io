import random



players = input("How many players ")
playerHands_dict = {}

deck = []
# hand = []
#deal a card from the deck
# TODO need to say when all cards of the deck have been dealt
def dealCard(dealt_card = 1):
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

# hand.append(dealCard(player_hand = hand))
# hand.append(dealCard(player_hand = hand))
# hand = filter(None, hand)
# print('Hand' , hand)

# try:
#     pass
# except expression as identifier:
#     pass

playerHands_dict = {"Player " + str(i): [] for i in (range(1, players+1))}
playerHands_dict["Dealer"] = []

# TODO dealCard() returns any number of cards, dispite it having a limit
for i in range(1000):
    playerHands_dict["Player 1"].append(dealCard())

# print(playerHands_dict)
playerHands_dict["Player 1"] = filter(None, playerHands_dict["Player 1"])
print(len(playerHands_dict["Player 1"]), playerHands_dict["Player 1"])