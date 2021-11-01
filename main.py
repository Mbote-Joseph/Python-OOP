import Department
import Course
import Student

class Test :
    a1 = Department('Computer Science', 'SWE 321',[])
    k3 = Course('Computer Networks', 'SWE 320', 4.8, a1)
    y2 = Course('Artificial Intelligence', 'SWE 220', 6.0, a1)
    courseList = []
    courseList.append(k3)
    courseList.append(y2)
    
    s1 = Student('John Doe',courseList, '101')

    print(s1)