
# views.py

from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, escape, make_response

from app import app, users_accounts

usr_account=users_accounts.Accounts_for_users()

#static folder


#homepage
@app.route('/')
def index():
    session['uname']= 'uname'
    flash('You are logged in as ','uname')


    return render_template("index.html")




#login page functions

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    """Manages requests sent by Login Page"""
    error=None
    if request.method == 'POST':  
        session.pop('uname', None)
        session['uname'] = request.form['uname']
        pswd = request.form['password']
        message = usr_account.login(session['uname'], pswd)
        if message == "Success!":
            flash('You have successfully logged in')
            #return redirect(url_for('view'))
            return render_template("shoppinglistitems.html")
        
    else:
        error = 'Invalid username or password!'
               

    return render_template("login.html", error=error)



@app.route("/logout")
def logout():
    session.pop('uname', None)
    # remove the username from the session if it is there
    return redirect(url_for('index'))



@app.route('/view',methods = ['POST', 'GET'])
def view():
    
         return render_template('view.html')



# New user register
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    
   
    if request.method == 'POST':
        uname= request.form.get('uname')
        email = request.form.get('email')
        pswd = request.form.get('password')
        pswd_confirmed = request.form.get('password_confirm')

        message = usr_account.registration(uname, email, pswd, pswd_confirmed)
        if message == "Kudos! Your have successfuly registered  your account please proceed to login":
            return render_template("login.html", response=message)
        elif message == "Your Account is Already Registered. Proceed to login":
            return render_template("login.html", response=message)
        elif message =="That username is already taken. Use another username":
            return flash(message)

        else:
            message="Your passwords do not match"
            return render_template("signup.html", response=message)
    

    return render_template("signup.html")

@app.route('/getsession')
def getsession():
    if 'uname' in session:
        return session['uname']

    return 'Not logged in!'

@app.route('/dropsession')
def dropsession():
    session.pop('uname', None)
    return 'Dropped!'

@app.route('/shoppinglistitems')
def shoppinglistitems():
    
         return render_template('shoppinglistitems.html')
   
