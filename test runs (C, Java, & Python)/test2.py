# define the Vehicle class
class Vehicle:
  name = ""
  kind = "car"
  color = ""w
  value = 100.00
  def description(self):
    desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
    return desc_str

# test code
car1 = Vehicle()
car2 = Vehicle()
car1.name = "Fer"
car2.name = "Jump"
car1.color = "red"
car2.color = "blue"
print(car1.description())
print(car2.description())


phonebook = {
  "John" : 938477566,
  "Jack" : 938377264
}

for name, number in phonebook.items():
  print(name,"'s phone number is ", number, sep="")


def spam(eggs):
  eggs.append(1)
  eggs = [2, 3]

ham = [0]
print("ham:", ham)
spam(ham)
print("ham:", ham)