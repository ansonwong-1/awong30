'''
SS AFK | Anson Wong, Faiza Huda, Kevin Xiao, Truthful Tom, Faizem, FamousMrTable 
Softdev 
K04 -- Dictionaries
2022-09-22
time spent: 0.8
'''
'''
DISCO:
- Typecasting is done with type(<what you're converting>)
- We got a random integer by importing random and using the function random.randint
QCC:
- We found it easier to convert to lists.
- What built-in methods are there for dictionaries?
(especially ones that could shorten what we did)
- Is there a difference in getting a random devo from a list of all devos vs
getting a random key and then a random value?
OPS SUMMARY:
We decided to make a list of the keys and then randomly choose from that list
because they aren't numerically sequential. After that, we got a random index for both 
the list of keys and the list of values. With those, we got a random devo in a random period. 
'''

import random

krewes = {
           2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"], 
           7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "KAREN"],
           8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "WANYING"]
         }


listofkeys= list(krewes.keys()) # for when there are keys - didn't work with original krewes dictionary copied from carepkg
keyIndice = random.randint(0, len(listofkeys)-1)

valueIndice = random.randint(0, len(krewes[listofkeys[keyIndice]])-1)

print(krewes[listofkeys[keyIndice]][valueIndice] + " Of Period " + str(keyIndice))

allDevos = []
for i in krewes:
    for j in krewes[i]:
        allDevos.append(j)
    
#print(allDevos)

indice = random.randint(0,len(allDevos)-1)
period = 2
for i in krewes:
    #print(i)
    if (indice < len(krewes[i])):
        #print(len(krewes[i]))
        period = i

print(allDevos[indice] + " Of Period " + str(period)) #not sure if this works -Anson


# jack and jill, went up the hill, to fetch a pail of water. So they say, the subsequent fall was inevitable, they never stood a chance they were written that way/ 

# original placeholder krewes
#krewes = {2:['1', '2', '3'], 7:['4', '5', '6'], 8:['7', '8', '9']}

#print(listofkeys)

# random indices
#print(keyIndice)
#print(valueIndice)

# key values
#print(krewes[listofkeys[keyIndice]])
# the random value

# checking if it seems random by running it multiple times
#for i in range(100):
#    keyIndice = random.randint(0,2)
#    valueIndice = random.randint(0,2)
#    print(krewes[listofkeys[keyIndice]][valueIndice])