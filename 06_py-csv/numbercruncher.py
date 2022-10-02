"""
Bobem | Ivan Yeung, Anson Wong
SoftDev
K06 -- numbercruncher/Python dictionary and weighted random/We are trying to write a python program that reads a csv file into a dictionary and randomly choosing one of the keys based on a percentage value
9-29-2022
Time spent: 1.5
DISCO:
- In order to compare quote character, you need to use \" to signify it
- .rfind() method finds the last occurence of an input
- The percentages add up to less than 99.8 calculated in python. Seems to be rounded
- You can add weights to the function random.choices (but not random.choice)
- The weights must be a list of either integers or floats
QCC:
-Why is csv file displayed differently in github
-Are the quotations supposed to be removed from occupation title?
-Is it better to do lines = file.read().spliet('\n') than lines = file.readlines()
HOW THIS SCRIPT WORKS:
1. populate_dict reads the entire csv file and splits it based on newlines.
It removes the first element(heading) and the last 2(total percentage and extra newline) from the list.
The function goes through the list of job/percent pairs and puts them into dictionary.
The method used to populate the dictionary with the pairs depends on whether the occupation contains a \" or not.
2. Made a list of occupations from the populated dictionary.
Made a corresponding list of weights from the populated dictionary.
METHOD USING choose_weighted FUNCTION
3a. choose_weight randomly chooses a number from 0 to 99.8 and continues to aggregate the weights from index 0 until the
sum surpasses the randomly chosen value. When the randomly chosen value is reached, the index of the last added weight
is used to determine the occupation that is choosen.
METHOD USING BUILT-IN WEIGHTS in random.choices()
3b. Each element in the list given in the first parameter of randoms.choices corresponds to the weight of the same index.
Thus the random is weighted.
(ex. random.choices([a, b, c], weights = [10, 20, 30]) a has a weight of 10, b has a weight of 20,...)
"""
import random as rng

def populate_dict(dictionary, filename):
    csv_file  = open(filename)
    #.read() parses everything into a string including white space
    # used .split to seperate the occupation/percentage pair
    data = csv_file.read().split("\n")
    #removes the first line since it doesn't count
    total_percentage = data[len(data) - 2]
    data = data[1:len(data) - 2]
    csv_file.close()
    for line in data:
        occ = line.rsplit(',', 1) #finds the first comma from the right and splits there
        if (occ[0] != 'Job Class'): #first one occ[1] can't be converted to a percentage
            dictionary[occ[0]] = float(occ[1])
        else:
            dictionary[occ[0]] = occ[1]
    return total_percentage.split(",")

def choose_weighted(choices, weights, total): # the choices and weights correspond based on their index in the list
    random_value = rng.random() * total
    #print(random_value)
    value = 0
    index = 0
    while value < random_value:
        value += weights[index]
        index += 1
    return choices[index - 1]


krewes = {} #dictionary holding occupations and percentages
total_percent = populate_dict(krewes, 'occupations.csv')
#print(f'Total Percent: {total_percent}')
#print(krewes)
occupations = list(krewes.keys())
weights = []
#Puts all the percentages into a list
for i in occupations:
    weights.append(krewes[i])
#print(occupations)
#print(weights)


#TESTING WEIGHTED RANDOM
test = {}
test2 = {}
for i in occupations:
    test[i] = 0
    test2[i] = 0
for i in range(100000):
    test[choose_weighted(occupations, weights, 99.8)] += 1.0
    test2[rng.choices(list(krewes.keys()), weights = list(krewes.values()))[0]] += 1.0
for i in occupations:
    test[i] /= 1000
    test2[i] /= 1000

#print(krewes)
#This is the other method just using the dictionary
#print(rng.choices(list(krewes.keys()), weights = list(krewes.values()))[0])
#print()
#print(test)
#print()
#print(test2)
print(choose_weighted(occupations,weights, 99.8))
#print(rng.choices(list(krewes.keys()), weights = list(krewes.values()))[0])
