

# views.py

from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, escape, make_response

from app import app, users_accounts,shopping_list
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

import os
app.secret_key = os.urandom(20)

usr_account = users_accounts.Accounts_for_users()
my_shopping_list=shopping_list.your_shopping_list()



# static folder


# homepage
@app.route('/')
def index():
    '''
    #  session['uname']= 'uname'
    # flash('You are logged in as ','uname')
    '''

    return render_template("index.html")

# login page functions


@app.route('/login', methods=['GET', 'POST'])
def login():
    
    """Manages requests sent by Login Page"""
    error = None
    if request.method == 'POST':  
        session.pop('uname', None)
        u_name = request.form['uname']
        pswd = request.form['password']
        message = usr_account.login(u_name, pswd)
        if message == "Success!":
            flash('You have successfully logged in')

            session['uname'] = u_name
            #return redirect(url_for('view'))

            return render_template("view.html")
        else:
            error = message
        
    else:
        error = 'Invalid username or password!'
               
    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.pop('uname', None)
    # remove the username from the session if it is there
    return redirect(url_for('index'))


text=[]
#adding shoppinglist in view template
@app.route("/view", methods=['POST','GET'])
def view():
    if request.method == 'POST':
        if 'uname' in session:
            shopping_list=request.form.get('list_name')
            if shopping_list not in text:
                message=my_shopping_list.add_shopping_list(shopping_list)
                #initiate list name session to enable list items to be stored in list
                if message=="Shopping list successfully added!":
                    text.append(shopping_list)
                    session['list_name'] = shopping_list
                    print (text)
            else:
                flash("There is a shopping list with that name. Please choose another shopping list Name") 
                return redirect(url_for('view'))
        else:
            flash("Login to proceed")
            return redirect(url_for('login'))



    return render_template('view.html', text=text)

#shopping lists
@app.route('/shoppinglists',methods=['POST','GET'])
def shoppinglists():
    if request.method == 'POST':
        if 'uname' in session:
            shopping_list=request.form.get('list_name')
            if shopping_list not in text:
                message=my_shopping_list.add_shopping_list(shopping_list)
                #initiate list name session to enable list items to be stored in list
                if message=="Shopping list successfully added!":
                    text.append(shopping_list)
                    session['list_name'] = shopping_list
                    print (text)
            else:
                flash("There is a shopping list with that name. Please choose another shopping list Name") 
                return redirect(url_for('view'))
        else:
            flash("Login to proceed")
            return redirect(url_for('login'))



    return render_template('view.html', text=text)

#single shoppinglist
@app.route('/update_shoppinglist/<listname>/',methods=['POST','GET'])
def update_shoppinglist(listname):
    if request.method == 'POST':
        if 'uname' in session:
            session['list_name']=listname
            new_listname=request.form.get('new_list_name')
            if shopping_list not in text:
                session['new_list_name']=new_listname
            else:
                flash("There is a shopping list with that name. Please choose another shopping list Name") 
                return redirect(url_for('update_shoppinglist', listname=new_listname))



    return render_template('update_shoppinglist.html', listname=listname)

        
        

#add list_item to shopping list
listitems=[]

@app.route('/shoppinglistitems', methods=['POST','GET'])
def shoppinglistitems():
    if request.method == 'POST':
        if 'uname' in session and 'list_name' in session:
            dict_of_list_items={}
            

            itemname=request.form.get('item')
            itemquantity=request.form.get('quantity')
            itemprice=request.form.get('price')

            #adding items to dictionary
            dict_of_list_items['item_name'] = itemname
            dict_of_list_items['quantity'] = itemquantity
            dict_of_list_items['price'] = itemprice

            listitems.append(dict_of_list_items)
            print(listitems)


            message=my_shopping_list.add_shopping_list_item(itemname,itemquantity,itemprice)
            if message=="shopping list item successfully added":

                print (listitems)
        else:
            return "Login to proceed"


    return render_template('shoppinglistitems.html', items=listitems)




@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':
        uname = request.form.get('username')
        email = request.form.get('email')
        pswd = request.form.get('password')
        pswd_confirmed = request.form.get('password_confirm')

        message = usr_account.registration(uname, email, pswd, pswd_confirmed)
        if message == "Kudos! Your have successfully registered  your account please proceed to login":
            return render_template("login.html", response=message)
        elif message == "Your Account is Already Registered. Proceed to login":
            return render_template("login.html", response=message)
        elif message == "That username is already taken. Use another username":
            return flash(message)

        else:
            message = "Your passwords do not match"
            return render_template("signup.html", response=message)

    return render_template("signup.html")



@app.route('/getsession')
def getsession():
    if 'uname' in session or 'list_name' in session:
        return session['uname'] , session['list_name']

    return 'Not logged in!'


@app.route('/dropsession')
def dropsession():
    session.pop('uname', None)
    return 'Dropped!'






   

   
