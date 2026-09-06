class Bank:
    def __init__(self,name,age,mark):
        self.__name=name
        self.__age=age
        self.__mark=mark

    def setName(self,name):                        # get and setter in python to be private to be accessible only through methods
        self.__name=name
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getMark(self):
        return self.__mark

obj=Bank("Maddy",21,78)
print(obj.getName()," ",obj.getAge()," ",obj.getMark())