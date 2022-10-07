# New Deal: Fang Min Chen, Ryan Lau, Anson Wong
# SoftDev
# K08: Serve
# Oct 2022
# time spent: 1 hrs

from flask import Flask
import csv
import random

app = Flask(__name__) #create instance of class Flask

# populate occupations dict
occupations = {}
with open('occupations.csv') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader) # [['Job Class', 'Percentage'], ['Management', '6.1'], ...]
    rows = rows[1:-1] # remove first and last row

for row in rows:
    occupations[row[0]] = float(row[1])

def pick_occupation_with_choices():
    occupation = random.choices(list(occupations.keys()), list(occupations.values()))
    return occupation[0] # random.choices() returns a list

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    occupation = pick_occupation_with_choices()
    list_of_occupations = list(occupations)
    return f"New Deal: Fang Min Chen (Cat), Ryan Lau (T), Anson Wong (Faizem) <br><br> <strong>Random occupation:</strong> {occupation} <br><br> <strong>List of occupations:</strong> <br> <ul> <li>{'</li><li>'.join(list_of_occupations)}"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()



# We predict that if __name__ is not __main__, then nothing will happen
# QCC: When is __name__ not __main__?
