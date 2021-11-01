class Course:
    def __init__(self, course_desc, course_code, credit, department):
        self.course_desc = course_desc
        self.course_code = course_code
        self.credit = credit
        self.department = department

 
    def __repr__(self):
        return "Course Information : Course Name =  {}\n Course Code = {} \n Course Credit = {} \n Department Name = {} \n".format(
            self.course_desc, self.course_code, self.credit, self.department.name)

    def setCourse_desc(self, name):
        self.name = name

    def getCourse_desc(self):
        return self.name

    def setCourse_code(self, courses):
        self.courses = courses

    def getCourse_code(self):
        return self.courses

    def getCredit(self):
        return self.department_code

    def setCredit(self, department_code):
        self.department_code = department_code

    def getDepartment(self):
        return self.department

    def setDepartment(self, department):
        self.department = department

