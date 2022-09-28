"""
Bobem | Ivan Yeung, Anson Wong
SoftDev
K05 -- Krewes/Python dictionary/We are trying to write a python program that randomly selects a devo from a dictionary after parsing
9-28-2022
Time spent:

DISCO:
- You read a textfile in python similarly to how you do so with scanner in java
QCC:
- Why is there an extra '\\n' element?
- How can we get rid of that extra element?
- Is there a way remove the outside [] in our devoList
OPS SUMMARY:

"""

#Ivan Yeung's code from 04_choose
#import random as rng
#krewes = {2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"],
#          7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
#          8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "wanying"]}

#dictionarylist = rng.choice(list(krewes.keys()))

#print("Period: " + str(dictionarylist))
#print("Name: " + str(rng.choice(krewes[dictionarylist])))

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

f = open('krewes.txt')
text = f.readlines()[0] #readlines returns a list of the lines- getting the 0th element is the first line
f.close()
#print("TEXT:")
#print(text)
krewes = {}
devoList = text.split('@@@')
devoList = devoList[:-1] #getting rid of new line
#print(devoList)
for devo in devoList:
    pd0 = devo[:1] #:1 when take out pd
    #print(pd0)
    if (pd0 != pd1):
        keyList.append(pd0)
        pd1 = devo[:1]
