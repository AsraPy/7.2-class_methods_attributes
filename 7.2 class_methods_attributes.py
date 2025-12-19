class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"نام:{self.name},سن:{self.age}")
    def greet(self):
        print(f"سلام.من{self.name}هستم.")

person1 = Person("Shima",20)
person2 = Person("Ali",25)

person1.show_info()
person1.greet()

person2.show_info()
person2.greet()
    
