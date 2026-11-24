class Student:
    def __init__(self, student_id, name, department, gpa):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.gpa = gpa
        self.courses = []

    def add_course(self, course_name):
        self.courses.append(course_name)
        print(course_name + " added.")

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa

    def get_info(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("GPA:", self.gpa)
        print("Courses:", self.courses)

# Test the class
s1 = Student("20230875", "Sudenur", "Information Systems and Technologies", 3.4)
s1.add_course("AII003")
s1.add_course("AII020")
s1.update_gpa(3.8)
s1.get_info()
