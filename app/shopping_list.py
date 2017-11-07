class your_shopping_list():

    

    def __init__(self):


        self.list_of_user_shoppinglists = []


        """Method used to create shopping list """
    def add_shopping_list(self,shopping_listname):
        
        if shopping_listname in self.list_of_user_shoppinglists:
            return "Shopping list name already exists, choose another shopping list name"
        else:
            self.list_of_user_shoppinglists.append(shopping_listname)
            for shoppinglists in self.list_of_user_shoppinglists:
                 print(shoppinglists)
            return "Shopping list successfully added!"

   

            
       


