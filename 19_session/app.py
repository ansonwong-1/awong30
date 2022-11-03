from flask import Flask,session,request, redirect, url_for,render_template

# Set the secret key to some random bytes. Keep this really secret!
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('login_attempt'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
@app.route("/login_attempt")
def login_attempt():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.debug = True
    app.run()