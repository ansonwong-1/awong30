'''
SS AFK | Anson Wong, Faiza Huda, Kevin Xiao, Truthful Tom, Faizem, FamousMrTable 
Softdev P2
'''
'''
DISCO:
QCC:
OPS SUMMARY: We decided to make a list of the keys and then randomly choose from that list
because they aren't numerically sequential. After that, we got a random index for both 
the list of keys and the list of values. 
'''

import math
import random

krewes = {2:['1', '2', '3'], 7:['4', '5', '6'], 8:['7', '8', '9']}

listofkeys= []
for i in range(len(krewes)):
    listofkeys.append(krewes.index(i))
keyIndice = random.randint(0,2)
valueIndice = random.randint(0,2)

print(krewes.get(listofkeys[keyIndice])[valueIndice])
print(krewes[2])