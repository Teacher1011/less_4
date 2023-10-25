class Human:
    height = 170
    gladness = 100

class Student(Human):
    gladness=0

class Worker(Human):
    gladness=50

kira = Student()
evgen = Worker()
print(kira.gladness)
print(evgen.gladness)
