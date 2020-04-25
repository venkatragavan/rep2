class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
    print("ModifiedVersion")
   
#Use the Person CLASS to create an instance, and then execute the printname method:


p = Person("Sivaprakash", "Venkat")

p.printname()
