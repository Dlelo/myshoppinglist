import unittest
from app import users_accounts

class Manage_Accounts_for_users(unittest.TestCase):

	def setUp(self):
		self.an_account = Accounts_for_users()


	# a global variable which is a list that stores all users data which is are dictionaries

	def test_already_existing_user(self):
		"""CHECKING IF USER DETAILS ALREADY EXIST"""

		self.new_user.registration("Donattah", "donattahakinyi@yahoo.com", "donah123", "donah123")
		message = self.new_user.registration("Donattah", "donattahakinyi@yahoo.com", "donah123", "donah123")
		self.assertEqual(message, "Your Account is Already Registered. Proceed to login")


if __name__ == '__main__':
    unittest.main()
