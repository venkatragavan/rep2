class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
    print("ModifiedVersion")
   
#Use the Person CLASS to create an instance, and then execute the printname method:


<<<<<<< HEAD
p = Person("Sivaprakash", "Venkat")
=======
p = Person("Johnny", "Venkatragavan")
>>>>>>> 0626da22b39164c647e2dca7b3240fc51e8bda04

p.printname()
