from webbrowser import get


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
    print ("Student's attributes(states)")

    def change_name (self, new_name):
        self.name = new_name
        print("name: ", self.name)

    def change_age (self, new_age):
        self.age = new_age
        print("age: ", self.age)

    def add_track (self, new_tracks):
        self.tracks.append(new_tracks)
        print("track: ", self.tracks)

    def get_score(self):
        print ("score :", self.score) 

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
