class Course:

    def __init__(self, course_name, course_duration, *books):
        self.course_name = course_name
        self.course_duration = course_duration
        self.books = [self.Book(i) for i in books]

    def show_deitals(self):
        print("Name: ", self.course_name)
        print("Duration: ", self.course_duration)
        print("Suggested Books")
        for i in self.books:
            print(i)

    class Book:
        def __init__(self,title):
            self.title = title

        def __str__(self):
            return self.title

c1 = Course("Python",10, "Learn Python", "Python crash course")
c1.show_deitals()
