# Flying Turtles | Anson Wong, Nicholas Tarsis
# SoftDev
# K14 -- Serving K13 by a Live Flask Web Server
# 2022-10-19
# time spent: 0.5

from flask import Flask, render_template

app = Flask(__name__)    #create Flask object

@app.route("/")
def serve_looks():
    # check if the Flask obj is running correctly in terminal
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    return render_template('index.html')

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
