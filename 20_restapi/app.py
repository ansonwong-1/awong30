# TBD: Sam Lubleksy
# Softdev pd02
# k20
# 2022-11-21
# time spent: 0.5hr
import requests
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def display_image():
    with open('key_nasa.txt','r') as f:
        key = f.read().strip('\n')
    BASE_URL = "https://api.nasa.gov/planetary/apod?"
    response = requests.get(BASE_URL, params={
        'api_key': key
    })
    nasa_json = response.content
    nasa_dict = json.loads(nasa_json)
    image_url = nasa_dict["url"]
    nasa_info = nasa_dict['explanation']
    return render_template("main.html", image_url=image_url, info = nasa_info)
if __name__ == "__main__":
    app.debug = True
    app.run()