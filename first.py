class Details:
	def __init__(self):
		self.roll_no = input("Enter roll_no: ")
		self.name = input("Enter name of the person: ")
		self.age = input("Enter age of the person: ")

	def get_roll(self):
		return self.roll_no	

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

class Department:
	def __init__(self):
		self.name = input("Enter department: ")

	def get_name(self):
		return self.name
