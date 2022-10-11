# New Deal: Fang Min Chen, Ryan Lau, Anson Wong
# SoftDev
# K08: Serve
# Oct 2022
# time spent: 1 hrs

from flask import Flask
import csv
import random

app = Flask(__name__)  # create instance of class Flask

# create and populate occupations dict
occupations = {}
with open("occupations.csv") as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)  # [['Job Class', 'Percentage'], ['Management', '6.1'], ...]
    rows = rows[1:-1]  # remove first and last row

for row in rows:
    occupations[row[0]] = float(row[1])

def pick_occupation_with_choices():
    occupation = random.choices(list(occupations.keys()), list(occupations.values()))
    return occupation[0]  # random.choices() returns a list


def occupations_to_html_list():
    html = "<ul>" # <ul> = unordered list
    for occupation in list(occupations):
        html += f"<li>{occupation}</li>" # <li> = list item
    html += "</ul>" # close unordered list 
    return html


@app.route("/")  # assign fxn to route
def hello_world():
    occupation = pick_occupation_with_choices()
    html_list_of_occupations = occupations_to_html_list()
    return f"""
    <strong>New Deal: Fang Min Chen (Cat), Ryan Lau (&lt;T&gt;), Anson Wong (Faizem)</strong>
    <br><br>
    <strong>Random occupation:</strong> {occupation} 
    <br><br>
    <strong>Possible occupations:</strong> 
    {html_list_of_occupations}
    """


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True  # enable auto-reload upon code change
    app.run()