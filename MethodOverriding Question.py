class Robot:

    def __init__(self,name):
        self.name = name

    def say_hi(self):
        print(f"hello im just a {self.name} robot")

class PoliceRobot(Robot):

    def say_hi(self):
        print(f"hello im Police {self.name} robot")


a = Robot("Arbaz")
a.say_hi()
b= PoliceRobot("Vikesh")
b.say_hi()