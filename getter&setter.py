class Dog:
    def __init__(self) -> None:
        self.__ownernames = "default name"
    
    def get_name(self):
        return self.__ownernames
    
    def set_name(self, name):
        self.__ownernames = name

myDog = Dog()
myDog.set_name("Happy")
print(myDog.get_name())