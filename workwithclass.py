class Bank:

    def __init__(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark
    def show(self):
        print("Name :",self.name)
        print("Age:",self.age)
        print("Mark:",self.mark)

obj=Bank("Maddy",25,98)
# obj.show()
print(obj.name)
print(obj.age)
print(obj.mark)