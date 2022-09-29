"""
Bobem | Ivan Yeung, Anson Wong
SoftDev
K06 -- Dictionary & Random with Weights
Time spent:
DISCO:
- The function str.rsplit is like str.split but from the right
- You can add an optional value to split and rsplit to say how many times you want to split
QCC:
- The .csv file is formatted differently in atom (editor) and on github
OPS SUMMARY:
We read the file and made each line (w 1 occupation & %) a element in a list

"""

import random as rng

f = open('occupations.csv')
lines = f.read()
f.close()

#testing out find
#test_string = '"Education, training", 6.1'
#print(test_string.find('"', 1))
#print(test_string[1:test_string.find('"', 1)])
#print(test_string[test_string.find('"', 1) + 3:])
lines = lines.split('\n')[:-1] #gets rid of the new lines
labor_force_list = []
count = 0
occ_dict = {}

for line in lines:
    occ = line.rsplit(',', 1) #finds the first comma from the right and splits there
    if (occ[0] != 'Job Class'): #first one occ[1] can't be converted to a percentage
        occ_dict[occ[0]] = float(occ[1])
    else:
        occ_dict[occ[0]] = occ[1]
#print(occ_dict)

occ_list = list(occ_dict.keys())
print(occ_list)
print(occ_list[1:-1])
occ = rng.choices(occ_list[1:-1]) #need to add weights
