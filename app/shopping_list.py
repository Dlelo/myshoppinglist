class shopping_list(Accounts_for_users):

    def __init__(self):
        self.list_for_user_shoppinglists=[]

        """Method used to create shopping list """
    def add_shopping_list(self,uname,shopping_listname):
        # user should add shopping list

        for dict_for_each_account in self.all_users_accounts:
            if uname == dict_for_each_account['uname']:         

                if shopping_listname not in list_for_user_shoppinglists:
                    list_for_user_shoppinglists.append(shopping_listname)
                else:
                    return "Shopping list name already exists, create a new shopping list"
                
            else:
                return "Account not registered, sign up to proceed"



