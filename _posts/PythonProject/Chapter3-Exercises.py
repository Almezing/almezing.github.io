# Intro to Python, Chapter 3 exercises 
# 3.1 
# years_list = []

# for year in range(0,6):
#     years_list.append(1992 + year)

# print(years_list)
# # 3.2
# print("Third Birth year: ", years_list[4])
# # 3.3
# print("Oldest year : ", years_list[-1])

# 3.4 

# things = ["mozzarella","cinderalla","salmonella"]
# things[1] = str(things[1].capitalize())
# things[0] = str(things[0].upper())
# things[2] = str(things[2].upper())
# things.pop()
# print(things)

# surprise = ["Groucho","Chico","Harpo"]

# surprise[2] = surprise[2][::-1].lower().capitalize()
# print(surprise)

# e2f = {"dog": "chien", "cat": "chat", "walrus":"morse"}
# words = list(e2f.items())
# f2e = {}
# for item in range(len(words)):
#     f2e[words[item][1]] = words[item][0]

# print(f2e)

# print(f2e["chien"])
# print(set(e2f))

life = {"animals": 
            {
                "cats": 
                    
                       [ "Henri" , "Grumpy", "Lucy"]
                    ,
                "octop": 
                    {}, 
                "emu": 
                    {}
            },
            "plants": 
                {} ,
             "other": 
                {} 
        }
print(life.keys())
print(life["animals"].keys()) 

print(life["animals"]["cats"]) 
