class student_profile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

#read input
student_id = input("Enter student ID: ")
name = input("Enter student name: ")
course = input("Enter student course: ")

#create student profile object
student = student_profile(student_id, name, course)

#print student profile
print(f"Student ID: {student.student_id}")
print(f"Name: {student.name}")
print(f"Course: {student.course}")