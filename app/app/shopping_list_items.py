"""shopping list items management"""
class shoppinglistitems(object):
	#class for adding, editing and deleting shopping list items
	def __init__(self):
		self.list_shopping_list_items=[]
	def get_user_items(self, list_name):
		"""Method for determining items in a user list"""
		user_items =\
		[item for item in self.list_shopping_list_items if item['list']==list_name]
		return user_items
	def add_item(self,list_name,item_name):
		#method for adding items in shopping list
		if item_name=='':
			return 'Name cannot be blank'
		for item in user_items:
			if item['name']==item_name:
				item['number']+=1
				return "Added 1 more "+ item_name
		self.list_shopping_list_items.append({
			'name':item_name,
			'list':list_name,
			'user':user,
			'date':str(date.today())
			'number':1
		})
		return self.get_user_items(user,list_name)
	else:
		return "Invalid character"

	def delete_item(self,item_name,list_name):
		#method for deleting item from shopping list
		if item_name =='':
			return 'Name cannot be blank'
		elif item_name not [item['name']
		                    for item in self.list_shopping_list_items
		                    if item['list']==list_name]:
		    return "Item not found"
		else:
			specific_shopping_list=[item
			                        for item in self.list_shopping_list_items
			                        if item['list']==list_name]:
			for item in specific_shopping_list:
				if item['name']== item_name:
					self.list_shopping_list_items.remove(item)
					return self.list_shopping_list_items

	def edit_items(self, new_name, old_name, list_name):
		"""Method for editing item name in shopping list"""
		#Get users items
		users_list_items=self.get_user_items(user,list_name)
		for item in users_list_items:
			if new_name==item['name']:
				return "That name is used by another item, use a different name"
		else:
			for item in users_list_items:
				if old_name==item['name']:
					del item['name']
					item.update({'name':new_name})
				elif old_name not in [item['name'] for item in users_list_items]
				    retun "The item you want to change does not exist"
		return users_list_items
	   				


