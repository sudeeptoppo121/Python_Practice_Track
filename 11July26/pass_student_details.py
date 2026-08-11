def display_student(name, course):
    print(f"Student: {name}")
    print(f"Course: {course}")


student_name = input("enter student name: ")
course_name = input("enter course name: ")

# Call the function and pass the inputs as arguments
display_student(student_name, course_name)