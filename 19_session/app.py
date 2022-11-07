#Flying Turtles | Anson Wong, Nicholas Tarsis
#SoftDev
#K19 -- Login
#2022-11-03
#time spent: 1
from flask import Flask,session,request, redirect, url_for,render_template
import os

# Set the secret key to some random bytes. Keep this really secret!
app = Flask(__name__)
app.secret_key = os.urandom(32)

USER = "user"
PASS = "pass"

@app.route('/', methods=['GET', 'POST'])
def login():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.headers ***")
    print(request.headers)
    print("***DIAG: request.method ***")
    print(request.method)
    if request.method == "GET":
        if 'username' in session:
            try:
                return render_template('response.html', response="You are logged in as " + session['username'])
            except IOError:
                print("EXCEPTION: No response.html file")
        try:
            return render_template("login.html")
        except IOError:
            print("EXCEPTION: No login.html file")
    print("***DIAG: request.form['username'] ***")
    print(request.form['username'])
    try:
        username = request.form['username']
    except:
        print("EXCEPTION: No username in form")
    print("***DIAG: request.form['password'] ***")
    print(request.form['password'])
    try:
        password = request.form['password']
    except:
        print("EXCEPTION: No password in form")
    if username != USER:
        try:
            return render_template('login.html', error='Bad username')
        except IOError:
            print("EXCEPTION: No login.html file")
    if password != PASS:
        try:
            return render_template('login.html', error='Bad password')
        except IOError:
            print("EXCEPTION: No login.html file")
    session['username'] = username
    return redirect(url_for('login'))

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if 'username' in session:
        session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run()
