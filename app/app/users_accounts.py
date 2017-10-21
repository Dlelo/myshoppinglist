""" user accounts management """

class Accounts_for_users(object):
    """ the class for creating a user account and login"""
    def __init__(self):


        self.list_of_accounts = [{'uname':'default',
                                  'email':'default@user.com',
                                  'pswd':'default'}]
    

    def registration(self, uname, email, pswd, pswd_confirm):
        """Method used to creating new accounts."""
        dict_for_each_account = {}

        for account in self.list_of_accounts:
            if email == account['email']:
                return "Your Account is Active. Proceed to login"
        else:
            if len(pswd) < 6:
                return "The Password is too short"
            elif pswd == pswd_confirm:
                dict_for_each_account['uname'] = uname
                dict_for_each_account['email'] = email
                dict_for_each_account['pswd'] = pswd
                self.list_of_accounts.append(dict_for_each_account)
            else:
                return "Your passwords do not match"
        return "Kudos! Your have successfuly registered  your account please proceed to login"

    def login(self, email, pswd):
        """Method used to manage Login """
        for account in self.list_of_accounts:
            if email == account['email'] and uname == account['uname']:
                return "Success!"
            else:
                return "Invalid email, password combination"
        return "Account not registered, sign up"

    def get_uname_by_email(self, email):
        """Returns the username when provided with email"""
        for account in self.list_of_accounts:
            if email == account['email']:
                return account['uname']

    