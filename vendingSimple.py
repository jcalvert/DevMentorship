import json

class VendingMachine:
	def __init__(self):
		self.coins = 0
		self.inventory = {
			'item1': 5,
			'item2': 5,
			'item3': 5
		}

	def insert_coin(self):
		self.coins = self.coins + 1

	def return_coins(self):
		self.coins = 0

	def vend(self, item):
		item_stock = self.inventory.get(item, 0)
		if item_stock > 0 and self.coins > 1:
			self.inventory[item] = self.inventory[item] - 1
			self.coins = self.coins - 2
			self.return_coins()

	def get_inventory(self):
		json_object = json.dumps(self.inventory, indent = 4)
		return(json_object)
