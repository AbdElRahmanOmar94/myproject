class Student:
    nb_of_students=0

    def __init__(abd,name:str,age,courses) -> None:
        abd.name = name
        abd.age=age
        abd.courses=courses
        Student.nb_of_students+=1


s1=Student("abd",29,["math"])
print(s1.age)