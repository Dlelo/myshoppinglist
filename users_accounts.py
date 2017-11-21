""" user accounts management """


class Accounts_for_users(object):
    """ the class for creating a user account and login"""
    def __init__(self):

        #self.uname=''

        self.dict_for_each_account = {}

        self.all_users_accounts = [{'uname': 'def', 'email': 'def@user.com', 'pswd': 'def'}]

    def registration(self, uname, email, pswd, pswd_confirm):
        """Method used to creating new accounts."""

        for dict_for_each_account in self.all_users_accounts:
            if email == dict_for_each_account['email']:
                return "Your Account is Already Registered. Proceed to login"
            elif uname == dict_for_each_account['uname']:
                return "That username is already taken. Use another username"
            elif len(pswd) < 6:
                return "The Password is too short"
            elif pswd == pswd_confirm:
                dict_for_each_account['uname'] = uname
                dict_for_each_account['email'] = email
                dict_for_each_account['pswd'] = pswd
                self.all_users_accounts.append(dict_for_each_account)
                print(dict_for_each_account)
            else:
                return "Your passwords do not match"
        return "Kudos! Your have successfully registered  your account please proceed to login"

    def login(self, uname, pswd):
        """Method used to manage Login """
        for dict_for_each_account in self.all_users_accounts:
            if uname == dict_for_each_account['uname'] and pswd == dict_for_each_account['pswd']:
                return "Success!"
            else:
                return "Invalid email, password combination"
        return "Account not registered, sign up to proceed"

    """def get_uname_by_email(self, email):
        #Returns the username when provided with email
        for an_account in self.all_users_accounts:
            if email == an_account['email']:
                return an_account['uname']"""





                 