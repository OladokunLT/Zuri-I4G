####################################### Start next line
# creating my own data type
# Students, Mentors, Cohort, Tasks

# class FourIR:
#     def __init__(self):
#         self.students = ["Maryam", "Layi", "Taopheeq", "Amat'llah"]
#         self.mentors = ["Ridwan", "Lukman", "Buhari", 45]
#         self.cohort = 2022
#         self.Task = ["simple calculator", "Counting word", "html semantics"]
#         self.another = {"level": "difficult"}

#     def get_students(self):
#         return self.students

# result = FourIR()
# print(result.get_students())
######################################## Ends above

################################ --- Section start here ----

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 
#         print("My name is", name, "and I am ", age)
#     # method
#     def speak(self):
#         print ("This is the speak func:", self.name, "and", self.age)
#     def addme(self, school):
#         self.school = school
#         print(school, " is my Institution name" )

# student1 = Person("Maggi", 14)
# student1.speak()
# student1.addme("Unibadan")

################################# ---- Section end here ---------------

################################ ===== start another class below ======

class Vehicle:
    def __init__(self, name, fuel, size):
        self.name = name
        self.fuel = fuel 
        self.size = size
    #method
    def car_capacity(self, speed):
        self.speed = speed
        print ("The automatic speed of vehicle is", self.speed)
#child or subclass
class Truck (Vehicle):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        print("Name of the truck:", self.name)
        print ("The color of the truck:", self.color)
    def car_capacity(self):
        print("This is me overriding the main class")
h = Truck("Ajagbe ejo", "Blue") 
h.car_capacity()  # this override the main class

############################ ====== end the end class here

################## Start here ---------------------
#kwarg behaves like a dictonary
def new(**kwargs):
    print (kwargs)
new (h="hello", b='bye bye', c='cool')  # output {'h': 'hello', 'b': 'bye bye', 'c': 'cool'}

def new(*args):
    print (args)
new ("hello", 'bye bye', 'cool')  # output ('hello', 'bye bye', 'cool')
################## End here ---------------------