class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
   
#Use the Person CLASS to create an instance, and then execute the printname method:


p = Person("Johnny", "Venkat")

p.printname()
