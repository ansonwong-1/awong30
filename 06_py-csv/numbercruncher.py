"""
Bobem | Ivan Yeung, Anson Wong
SoftDev
K06 -- Dictionary & Random with Weights
Time spent: 1
DISCO:
- The function str.rsplit is like str.split but from the right
- You can add an optional value to split and rsplit to say how many times you want to split
- You can add weights to the function random.choices (but not random.choice)
- The weights must be a list of either integers or floats.
- Each element in the list given in the first parameter of random.choices
corresponds to the weight of the same index.
(ex. random.choices([a, b, c], weights = [10, 20, 30]) a has a weight of 10, b has a weight of 20,...)
QCC:
- The .csv file is formatted differently in atom (editor) and on github. Why?
- How can we test for if the weights work correctly?
- Is it better to do lines = file.read().split('\n') than lines = file.readlines()?
- In what cases would we need to read the \n?
OPS SUMMARY:
We read the file and made each line (w 1 occupation & %) an element in a list
Then we split each line once at the first comma from the right
We then used those values to make a dictionary with the format {Occupation: Percentage}
We used random.choices to get a random key (occupation) and the key values as the weights
(excluding the Occupation: Percentage and Total: 99.8)
"""

import random as rng

f = open('occupations.csv')
lines = f.read()
f.close()


lines = lines.split('\n')[:-1] #gets rid of the new lines
occ_dict = {}

for line in lines:
    occ = line.rsplit(',', 1) #finds the first comma from the right and splits there
    if (occ[0] != 'Job Class'): #first one occ[1] can't be converted to a percentage
        occ_dict[occ[0]] = float(occ[1])
    else:
        occ_dict[occ[0]] = occ[1]
#print(occ_dict)

key_list = list(occ_dict.keys())
occ = rng.choices(key_list[1:-1], weights = list(occ_dict.values())[1:-1])[0] #need to add weights
print(occ)
