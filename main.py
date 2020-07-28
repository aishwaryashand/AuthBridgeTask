from first import Details,Department
from second import AllDetails
class A:
	def __init__(self):
		print("Hey there!")
		global detail,department
		detail = Details()
		department = Department()

	def show(self):
		a = AllDetails(detail.get_roll(),detail.get_name(),detail.get_age(),department.get_name())
		a.show()
p1 = A()
p1.show()

