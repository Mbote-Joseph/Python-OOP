

class Student:

    def __init__(self, name, student_number, courses):
        self.name = name
        self.courses = courses
        self.student_number = student_number

   
    def __repr__(self):
        return "Student Information : Student Name = {}\n Student Number = {}\n Courses Joined = {}\n".format(self.name, self.student_number, self.courses)

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setCourses(self, courses):
            self.courses = courses

    def getCourses(self):
        return self.courses

    def getStudent_number(self):
        return self.student_number

    def setStudent_number(self, student_number):
        self.student_number = student_number

