# New Deal: Fang Min Chen, Ryan Lau, Anson Wong
# SoftDev
# K08: Serve
# Oct 2022
# time spent: .2 hrs

from flask import Flask
app = Flask(__name__) # create instance of flask

@app.route("/") # what is '/'?
def hello_world():
    print(__name__) # prints __main__
    return "No hablo queso!"  # shows up in firefox

app.run()  # nothing happens when this line is commented out
                
# We predict that No hablo queso! shows up in firefox when ran