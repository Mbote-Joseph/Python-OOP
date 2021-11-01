
class Department:
    def __init__(self, name, department_code, courses):
        self.name = name
        self.courses = courses
        self.department_code = department_code


    def __repr__(self):
        return "Department Information : Department Name =  {} \n Department Code = {}\n Department Courses = {}\n".format(self.name, self.department_code, self.courses )

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setCourses(self, courses):
        self.courses = courses

    def getCourses(self):
        return self.courses

    def getDepartment_code(self):
        return self.department_code

    def setDepartment_code(self, department_code):
        self.department_code = department_code


