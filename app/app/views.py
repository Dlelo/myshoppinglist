
# views.py

from flask import Flask, flash, redirect, render_template, request, session, abort

from app import app, users_accounts

usr_account=users_accounts.Accounts_for_users()

#homepage
@app.route('/')
def index():
    return render_template("index.html")

#login page functions

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Manages requests sent by Login Page"""
    if request.method == 'POST':
        session['email'] = request.form['email']
        session['username'] = usr_account.get_uname_by_email(request.form['email'])
        #email = request.form['email']
        #pswd = request.form['password']
        #message = usr_account.login(email, pswd)
        #if message == "Success!":
            
            
        return redirect(url_for('view'))

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('username', None)
    # remove the username from the session if it is there
    return redirect(url_for('index'))


@app.route('/view')
def view():
    return render_template("view.html")

@app.route('/recover')
def recover():
    return render_template("recover.html")

@app.route('/confirm')
def confirm():
    return render_template("confirm.html")

# New user register
@app.route('/signup', methods=['GET', 'POST'])
def signup():
   
    if request.method == 'POST':
        uname = request.form.get('username')
        email = request.form.get('email')
        pswd = request.form.get('password')
        pswd_confirmed = request.form.get('password_confirm')

        message = usr_account.registration(uname, email, pswd, pswd_confirmed)
        if message == "Kudos! Your have successfuly registered  your account please proceed to login":
            return render_template("login.html", response=message)
        elif message == "Your Account is Already Registered. Proceed to login":
            return render_template("login.html", response=message)
        elif message == "Your Account is Already Registered. Proceed to login":
            return render_template("signup.html", response=message)
        else:
            message="Your passwords do not match"
            return render_template("signup.html", response=message)

    return render_template("signup.html")

