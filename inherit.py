from datetime import date
class Person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    
    def display(self):
        return "description:"+ self.name

    @classmethod
    def anotherConstructor(cls,name,birthYear,extra):
        return cls(name,date.today().year-birthYear,extra)

class Man(Person):
    gender="Male"
    nb_of_men=0

    def __init__(self, name, age,voice) -> None:
        super().__init__(name, age)
        self.voice=voice
        Man.nb_of_men+=1

    def display(self):
        s1= super().display()
        return s1 + self.voice
    
m1=Man("abd",54,"hard")
print(m1.display())
print(Man.nb_of_men)

m2=Man.anotherConstructor("m",2000,"soft")
print(m2.voice)
print(isinstance(m2,Person))
print(7)