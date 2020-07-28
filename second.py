class AllDetails:
	def __init__(self,roll_no,name,age,department):
		self.roll_no = roll_no
		self.name = name
		self.age = age
		self.department = department

	def show(self):
		print("{}'s roll number is {} and is {} years old. Works with {} department.".format(self.name.capitalize(),self.roll_no,self.age,self.department.upper()))
