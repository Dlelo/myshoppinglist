"""manage shopping lists"""
class Myshoppinlist(object):
	def __init__(self):

		self.allshoppinglists=[];



	def addshoppinglist(self, shopping_list_name):
		#method for creating shopping list
		if shopping_list_name=='':
			return 'Shopping list name cannot be blank'
		for item in allshoppinglists:
			if shopping_list_name == item['name']:
				return "List already exits."
			else:
				self.allshoppinglists.append(shopping_list_name)

	def editshopppinglist(self, new_name, old_name):
	    #method for editing the name of a shopping list
	    for item in allshoppinglists:
			if old_name == item['name']
			#finish editing list

	def deleteshoppinglist(self,list_name):
		#method for deleting a shopping list
		if list_name=='':
			return "Name cannot be blank"
		elif list_name not in [item['name'] for item in self.allshoppinglists]:
			return "Item not found"
		else:
			for item in self.allshoppinglists:
				item_index=self.allshoppinglists.index(item)
				if item['name']==list_name:
					del self.allshoppinglists[item_index]
					return list_name + " has been Deleted"



