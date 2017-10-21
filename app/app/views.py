
# views.py

from flask import Flask, flash, redirect, render_template, request, session, abort

from app import app, users_accounts

usr_account=users_accounts.Accounts_for_users()

#homepage
@app.route('/')
def index():
    return render_template("index.html")

def login_required(f):
    """Restricts access to pages that require user to login before accessing"""
    @wraps(f)
    def wrap(*args, **kwargs):
        """wraps around the f function"""
        if 'username' in session:
            return f(*args, **kwargs)
        else:
            message = "Please login"
            return render_template("login.html", response=message)
    return wrap



#login page functions

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Manages requests sent by Login Page"""
    if request.method == 'POST':
        email = request.form['email']
        pswd = request.form['password']
        message = usr_account.login(email, pswd)
        if message == "Success!":
            session['email'] = email
            session['username'] = usr_account.get_uname_by_email(email)
            table_response = list_table_creator.ItemTable(
                shopn_list.users_list(session['username']))
            return redirect('/view')
                              
        else:
            return redirect('/signup')

    return render_template("login.html")

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return login()


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
        uname = request.form['username']
        email = request.form['email']
        pswd = request.form['password']
        pswd_confirmed = request.form['password_confirm']

        message = usr_account.registration(uname, email, pswd, pswd_confirmed)
        if message == "Kudos! Your have successfuly registered  your account please proceed to login"\
        or message == "Your Account is Active. Proceed to login":
            flash('Kudos! Your have successfuly registered  your account please proceed to login')
            return redirect('/login')
        else:
        	return redirect('/signup')

    return render_template("signup.html")

