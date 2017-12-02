"""Class used to add, edit, delete shopping list and list items"""
class your_shopping_list():
    """Class to create, add, edit and delete shopping lists"""
    def __init__(self):


        self.list_of_user_shoppinglists = []
        self.list_of_shoppinglist_items = []
        self.dict_of_list_items = {'item': 'default', 'quantity': 'default', 'price': 'default'}

    def add_shopping_list(self, shopping_listname):
        """Method used to create shopping list """
        if shopping_listname in self.list_of_user_shoppinglists:
            return "Shopping list name already exists, choose another shopping list name"
        else:
            self.list_of_user_shoppinglists.append(shopping_listname)
            for shoppinglists in self.list_of_user_shoppinglists:
                print(shoppinglists)
            return "Shopping list successfully added!"


    def add_shopping_list_item(self, item_name, item_quantity, item_price):
        """Method used to add shopping list item """
        if item_name == self.dict_of_list_items['item']:

            return "That shopping item Already Exists in this shopping list!"
        else:
            self.dict_of_list_items['item'] = item_name
            self.dict_of_list_items['quantity'] = item_quantity
            self.dict_of_list_items['price'] = item_price
            self.list_of_shoppinglist_items.append(self.dict_of_list_items)
            print(self.dict_of_list_items)
            return "shopping list item successfully added"
        