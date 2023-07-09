from datetime import date
class Student:
    nb_of_students=0

    def __init__(self,name:str,age,courses=[]):
        self.__name = name ## __ for private attribute
        self.__age=age
        self.__courses=courses
        Student.nb_of_students+=1

    ##getter and setter
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name

    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age=age

    def get_courses(self):
        return self.__courses
    def set_courses(self,courses):
        self.__courses=courses

    def describe(self):
        print(f'my name is {self.__name}')
    
    def isOld(self,age1):
        return self.__age>age1
    
    @classmethod # decorator class method 
    #kerml multple constructor
    def initFromBirthYear(cls,name,birthYear):
        return cls(name,date.today().year-birthYear)




class Pizza:
    def __init__(self,ingredients) -> None:
        self.ingredients=ingredients

    @classmethod
    def veg(cls):
        return cls(["onion","mash"])
    
    ## magic functions
    def __str__(self) -> str:
        return f'Pizza ingredients are {self.ingredients}'

    @staticmethod
    def shiTayb():
        print("ktiiiir taybi")

s1=Student("abd",29,["math"])
s1.age=24
s1.describe()
print(s1.isOld(20))
s1.set_name("omar")
s1.name="testtt"
print(s1.get_name())

print(s1.get_age())

s2=Student.initFromBirthYear("ahmad",1993)
print(s2.get_name())
print(type(s2))

p1=Pizza.veg()
print(p1.ingredients)
print(p1)
Pizza.shiTayb()