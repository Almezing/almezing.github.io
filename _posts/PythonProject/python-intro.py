# import webbrowser
# import json
# import requests

# print("Let's find an old website.")
# site = input("Type a website URL: ")
# era = input("Type a year, month, and day like 20190101: ")
# url = "http://archive.org/wayback/avaliable?url=%s&timestamp=%s" % (site, era)
# response = requests.get(url)
# data = response.json()
# try:
#     old_site = data["archived_snapshots"]["closests"]["url"]
#     print("Found this copy: ", old_site)
#     print("It should appear in your browser now.")
#     webbrowser.open(old_site)
# except:
#     print("Sorry, no luck finding", site)

#######everything in python is implemented as an object. variables are pointers to those objects, not the objects themselves. so 2 variables can point to the same object

objectA = 'This is the data the object contains'
objectB = objectA
print(objectB)
print(type(objectB))

########ints are assumed to be in base 10, but python can work with binary, octal and hexadecimal

intBase10 = 10
intBaseBinary = 0B10 #also can be 0b10
intBaseOctal = 0O10 #0o10
intBaseHexadecimal = 0X10 # 0X10
print(intBase10, intBaseBinary,  intBaseOctal, intBaseHexadecimal)

#other object types can be convereted into integers. this is called typecasting

intBoolean = int(True)
intFloat = int(10.30)
intScientific = int(1.0e3)
intString = int('-31')
print(intBoolean, intFloat, intScientific, intString)
#mixed data can't be converted ie int('100 Dollars')

#floats are used to represent decimal numbers
numFloat = 313.13
print(numFloat)

######python strings. strings are immutable (changeable). they can be created with either single or double qoutes

#escape with  \
escapeString = 'A man, \nA plan, \nA canal:\n Panama'
print(escapeString)

#combine with +
combineStrings = 'Release the Kraken' + '.'+ 'No, wait!'
print(combineStrings)

#duplicate with *
duplicateString = 'Na ' * 8 + 'Batman!'
print(duplicateString)

#extract charcter in strings
extractString = 'Hello, My dudes'
print(extractString[1])

#slice with [start: end: step]
# [:] - extracts the entire sequence from start to end
# [start :] - specifies from the start offset to the end
# [: end] - specifies from the beginning to the end offset minus 1
# [start: end] - extracts from the start-offset to the end-offset minues 1
# [start : end : step] - extracts from the start-offset to the end-offset minues 1, skipping characters by step
# the end needs to be one more than the actual offset

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[:])
print(letters[20:])
print(letters[12:15])
print(letters[4:20:3]) # returns the characters in between 4 and 19, skip by 3
print(letters[-3]) # returns the last 3 characters from the end, in order
print(letters[18:-3]) # returns the characters that start at 18 and ends just after the 3rd character from the end
print(letters[-6:-2]) # returns the characters that start at 6 chracters to the end to 3 before the end
print(letters[::7]) # return the characters after every 7 characters
print(letters[-1::-1]) # same as print(letters[::-1] - return the entire sequence in reverse

#some functions
print(len(letters)) # len() not specific to strings
print(letters.split('m')) # split the string by a specific delimiter. returns an array/list
#.join() will a list of strings to one string
#.strip(character) returns a string with all instances of character removed
#.capitalize(), capitlaize the first letter of a string.
#.title

######tuples and list = arrays. tuples are immutable, but they both can hold the same data type and elements are be of different types

# list are ordered, and elements don't need to be unique
# empty_list = [] is same as empty_list = list()
#list function can conver other data types to a list, but not floats or ints.  = () is not the same, but creates a tuple

#append(element) adds to a list to the end
#lists can be combined with extend() or +=. added towards the end
#master_list.extend(branch_list)
#master_list += branch_list

#inster(offset, element) add new element at offset position. element can also be a list

#del list[offset] - delete an element at offset

#list.pop(offset) - removes the element at offset. without offset, removes the last element

#.index(element) - returns the index of element

#element in list - test if an element is in list, returns boolean

#.count(element) - returns the number of times an element appears in a list

#.sort(reversed = boolean) - sorts a list, assign to original variable. can be reversed
#sorted(list) = creates a copy of the original list that is sorted

#len(list) returns the nubmer of elements in a list. if an element is another list, it is counted as 1, regards of the elements inside that list.

# var = list.copy(), var = list(list), var =list[:] - copies a list and assigns the new copy to a variable

#emply_tuple = ()
#new_tuple = 'string', creates a tuple with 'string' as the first element in it. comma is followed after each element., but not the last can also be done as  ('string')

#tuple elements can be assiged at once
# new_tuple = ('StringA', 'StringB', StringC)
#a, b, c = new_tuple 

#dictionaries can be created as empty_dict = {}. the se are mutable but are indexed by a key value of any python object

#dict() can convert a sequence into a dictionary, the first element is used as the key.