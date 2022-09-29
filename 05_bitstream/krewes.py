"""
Bobem | Ivan Yeung, Anson Wong
SoftDev
K05 -- Krewes/Python dictionary/We are trying to write a python program that randomly selects a devo from a dictionary after parsing
9-28-2022
Time spent: 2
DISCO:
- You have to open and close a textfile to read it
- split() method: string.split(separator [white space is default], maxsplit [all occurences is default]) returns a list of the seperated strings
- You can check if a dictionary has a key by calling [ {key} in {dictionary} ]
QCC:
- Why is there an extra '\\n' element?
- We can get rid of that extra element through list splicing
- File.readlines() doesn't return a string it returns a list of the lines
OPS SUMMARY:
We started off by printing a string structured in the way given, but made each devo and ducky name unique.
That string went into our krewes.txt file and we read that and took the first (and only) line of it as the string we worked on.
We made a list of each devo (including period, name, and ducky) and added each one to the dictionary with the keys being the period and values being a list with the name then ducky.
Then, we chose a random devo by using random.choice from the keys (periods) and then random.choice again to choose a devo and their ducky.
"""

import random as rng

#printing out placeholder string for textfile
txtString = ""
for i in range(20):
    txtString+="2$$$devo" + str(i) + "$$$ducky" + str(i) + "@@@"
for i in range(20):
    txtString+="7$$$devoa" + str(i) + "$$$duckya" + str(i) + "@@@"
for i in range(20):
    txtString+="8$$$devob" + str(i) + "$$$duckyb" + str(i) + "@@@"
#print(txtString)

#f = open('krewes.txt') #don't need path bc same directory
def has_key(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False

f = open('krewes.txt')
text = f.readlines()[0] #readlines returns a list of the lines- getting the 0th element is the first line
f.close()
krewes = {}
devoList = text.split('@@@')
#print("Before: " + str(devoList))
devoList = devoList[:-1] #getting rid of new line element
#print("After: " + str(devoList))
#print(devoList)
for devo in devoList:
    pd = devo.split("$$$")[0]
    if (has_key(krewes, pd) == False):
        krewes[pd] = []
    krewes[pd].append(devo.split("$$$")[1:]) # appending elements 1 and 2 will create a collection of 2 element lists with devo and ducky pair
#print(krewes)
period = rng.choice(list(krewes.keys()))
devoduck = rng.choice(krewes[period])
print("Period: " + str(period))
print("Devo: " + str(devoduck[0]))
print("Ducky: " + str(devoduck[1]))
print()
#Testing formated strings
print(f'Period: {period}')
print(f'Devo: {devoduck[0]}')
print(f'Ducky: {devoduck[1]}')
