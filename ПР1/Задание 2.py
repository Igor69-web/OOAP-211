class Dante:
	name = "Dante"
	entity = "Nefilim"
	def who(self):
		print(self.name + " " "is a" " "+ self.entity)
	def descendant(self):
		print(self.name + " ""descendant Sparda")
obj= Dante()
obj.who()
obj.descendant()
class Vergily:
	name = "Vergily"
	entity = "Nefilim"
	def who(self):
		print(self.name + " ""brother Dante")
	def owner(self):
		print(self.name + " ""owner Ymato")
obj = Vergily()
obj.who()
obj.owner()