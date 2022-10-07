# New Deal: Fang Min Chen, Ryan Lau, Anson Wong
# SoftDev
# K08: Serve
# Oct 2022
# time spent: .2 hrs

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go? in the terminal
    return "No hablo queso!"

app.run()

# We predict this will do the same thing as v0
# except "about to print __name__..." will also 
# be printed in the terminal
