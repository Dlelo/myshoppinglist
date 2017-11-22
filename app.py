"""my shopping list app"""
import os
from flask import Flask
from flask import flash, request, session
from flask import redirect, render_template, url_for
from users_accounts import Accounts_for_users
from shopping_list import your_shopping_list


app = Flask(__name__)
app.debug = True

app.secret_key = os.urandom(20)
USER_ACCOUNT = Accounts_for_users()
MY_SHOPPING_LIST = your_shopping_list()


# static folder

# homepage
"""user landing page or homepage"""
@app.route('/')
def index():
    '''
    #  session['uname']= 'uname'
    # flash('You are logged in as ','uname')
    '''

    return render_template("index.html")

# register function

LIST_OF_UNAME = []
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """function that registers a user"""
    if request.method == 'POST':
        uname = request.form.get('username')
        email = request.form.get('email')
        pswd = request.form.get('password')
        pswd_confirmed = request.form.get('password_confirm')
        message = USER_ACCOUNT.registration(uname, email, pswd, pswd_confirmed)
        if uname in LIST_OF_UNAME:
            flash("That username is already taken, Use another username")
        elif message == "Kudos! Registration successful, please proceed to login":
            LIST_OF_UNAME .append(uname)
            print(LIST_OF_UNAME)
            return render_template("login.html", response=message)
        elif message == "Your Account is Already Registered. Proceed to login":
            return render_template("login.html", response=message)
        elif message == "That username is already taken. Use another username":
            return flash(message)

        else:
            message = "Your passwords do not match"
            return render_template("signup.html", response=message)

    return render_template("signup.html")

# login page functions

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Manages requests sent by Login Page"""
    error = None
    if request.method == 'POST':
        session.pop('uname', None)
        u_name = request.form['uname']
        pswd = request.form['password']
        message = USER_ACCOUNT.login(u_name, pswd)
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
    """function that logout user"""
    session.pop('uname', None)
    # remove the username from the session if it is there
    return redirect(url_for('index'))

TEXT = []

"""user dashboard page and adds shopping lists and displays them"""
#adding shoppinglist in view template
@app.route("/view", methods=['POST', 'GET'])
def view():
    """function that creates and displays shopping lists"""
    if request.method == 'POST':
        if 'uname' in session:
            the_shopping_list = request.form.get('list_name')
            if the_shopping_list not in TEXT:
                message = MY_SHOPPING_LIST.add_shopping_list(the_shopping_list)
                #initiate list name session to enable list items to be stored in list
                if message == "Shopping list successfully added!":
                    TEXT.append(the_shopping_list)
                    session['list_name'] = the_shopping_list
                    print (TEXT)
            else:
                flash("There is already a shopping list with that name!")
                return redirect(url_for('view'))
        else:
            flash("Login to proceed")
            return redirect(url_for('login'))



    return render_template('view.html', TEXT=TEXT)

#shopping lists
@app.route('/shoppinglists', methods=['POST', 'GET'])
def shoppinglists():
    """function that displays all user shopping lists"""
    if request.method == 'POST':
        if 'uname' in session:
            shoppinglist = request.form.get('list_name')
            if shoppinglist not in TEXT:
                message = MY_SHOPPING_LIST.add_shopping_list(shoppinglist)
                #initiate list name session to enable list items to be stored in list
                if message == "Shopping list successfully added!":
                    TEXT.append(shoppinglist)
                    session['list_name'] = shoppinglist
                    print (TEXT)
            else:
                flash("There is already a shopping list with that name!")
                return redirect(url_for('view'))
        else:
            flash("Login to proceed")
            return redirect(url_for('login'))



    return render_template('shoppinglists.html', TEXT=TEXT)


#single shoppinglist
@app.route('/update_shoppinglist/<int:id>/', methods=['POST', 'GET'])
def update_shoppinglist(id):
    """function that updates user shopping lists"""

    old_listname = session['list_name']
    print (old_listname)

    if request.method == 'POST':
        if 'uname' in session:
            new_shoppinglist = request.form.get('list_name')
            if new_shoppinglist not in TEXT:
                print(new_shoppinglist)
                TEXT.remove(old_listname)
                TEXT.append(new_shoppinglist)
                #initiate list name session to enable list items to be stored in list
                session['list_name'] = new_shoppinglist
                flash("You have successfully updated your shopping list")
                return redirect(url_for('view'))
            else:
                flash("There is already a shopping list with that name")
                return redirect(url_for('view'))
        else:
            flash("Login to proceed")
            return redirect(url_for('login'))


    return render_template('update_shoppinglist.html', id=id, listname=old_listname)

 #delete shoppinglist
@app.route('/delete_shoppinglist/<int:id>/', methods=['GET', 'POST'])
def delete_shoppinglist(id):
    """Function that deletes shopping list"""
    todelete_listname = session['list_name']
    print (todelete_listname)

    if request.method == 'POST':
        if 'uname' in session:
            if todelete_listname in TEXT:
                TEXT.remove(todelete_listname)
                flash("You have successfully deleted the shopping list")
                return redirect(url_for('view'))
            else:
                flash("Unable to delete shoppinglist")
                return redirect(url_for('view'))
        else:
            flash("Login to proceed")
            return redirect(url_for('login'))
    return render_template('delete_shoppinglist.html', id=id, listname=todelete_listname)
#add list_item to shopping list


LISTITEM = []

@app.route('/shoppinglistitems/<int:id>/', methods=['POST', 'GET'])

def shoppinglistitems(id):
    """function that adds shopping list items"""
    if request.method == 'POST':
        if 'uname' in session and 'list_name' in session:
            if session['list_name'] == 'list_name':
                dict_of_list_items = {}
                itemname = request.form.get('item')
                itemquantity = request.form.get('quantity')
                itemprice = request.form.get('price')

                #adding items to dictionary
                dict_of_list_items['item_name'] = itemname
                dict_of_list_items['quantity'] = itemquantity
                dict_of_list_items['price'] = itemprice

                LISTITEM.append(dict_of_list_items)
                print(LISTITEM)
                message = MY_SHOPPING_LIST.add_shopping_list_item(itemname, itemquantity, itemprice)
                if message == "shopping list item successfully added":
                    print(LISTITEM)
        else:
            return "Login to proceed"

    return render_template('shoppinglistitems.html', id=id, LISTITEM=LISTITEM)

@app.route('/getsession')
def getsession():
    """function that detects sessions username and listname are on"""
    if 'uname' in session or 'list_name' in session:
        return session['uname'], session['list_name']

    return 'Not logged in!'


@app.route('/dropsession')
def dropsession():
    """function that detects if user session is deleted"""
    session.pop('uname', None)
    return 'Dropped!'




if __name__ == '__main__':
    port = int(os.environ.get('PORT', 500))
    app.run(host="0.0.0.0", port=port)
