import unittest
import users_accounts
import shopping_list


users = users_accounts.Accounts_for_users()
shopping = shopping_list.your_shopping_list()

class Test_users_accounts(unittest.TestCase):

    def test_registration(self):
        response = users.registration('donah','donah@gmail.com', '12donah@', '12donah@')
        self.assertEqual(response, ('Your Account is Already Registered. Proceed to login'))
        self.assertNotEqual(response, ('That username is already taken. Use another username'))

    def test_login(self):
        message = users.login("donah", "donah@")
        self.assertEqual(message, "Invalid email, password combination")

class Test_shoppinglist(unittest.TestCase):
    def test_add_shopping_list(self):
        message = shopping.add_shopping_list("kitchen")
        self.assertEqual(message, "Shopping list successfully added!")

    def test_add_shoppinglist_items(self):
        message = shopping.add_shopping_list_item("Mango", "2", "30" )
        self.assertEqual(message, "shopping list item successfully added")










if __name__ == '__main__':
    unittest.main()