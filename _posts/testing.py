# sum all numbers that factorable by 3 and 5
# NumResult = []

# for i in range(1000):
#     if i % 3 == 0 or i % 5 == 0:
#         NumResult.append(i)

# print(sum(NumResult))

# find the fib sequence
# x = 1
# y = 2
# z = 0
# NumResult = []
# for i in range(10):
#     if z < 2:  
#         z += 1
#     else:
#         z = x + y
#         x = y
#         y = z    
#     if z % 2 == 0:
#         NumResult.append(z)
# print(sum(NumResult))

# def largestPrimeFactor():
#     print("yo")

# largestPrimeFactor()

# a_list = ( 1 , "crap", 2, "poop")

# for i , val in enumerate(a_list):
#     print(i, val)
# print(list(enumerate(a_list)))

# a, b , c ,d = a_list

# print(a, b, c, d,)
players = input("Enter number of players: ")

# if not players:
#     print(True)
# else:
#     print(False)
playerHands_dict = {}

try:
    pass
except ValueError: as identifier:
    pass players :

    for i in range(int(players) + 1):
        # print(eval(str(i > int(players) - 1)))
        if i > int(players) - 1:
            playerHands_dict["Dealer"] = 0
        else:
            playerHands_dict["Player " + str(i+1)] = 0
else:
    print('no number')
   
#print(eval(str(i+1)))

# print(playerHands_dict)

# print(sorted(playerHands_dict)[-1])



import random


deck = {
    1 : 0,
    2 : 4,
    3 : 4,
    4 : 4,
    5 : 4,
    6 : 4,
    7 : 4,
    8 : 4,
    9 : 4,
    10 : 16,
    11: 4
}

#for keys, vals in deck.items():
#keys = random.shuffle(deck)

#keys = random.randint(1,10)
keys = 1
print(keys)

def deal():
    if deck[keys] > 0:
        deck[keys] = deck[keys] - 1
    else:
       pass
        #deal()
deal()
print(deck[keys])
deal()
print(deck[keys])
