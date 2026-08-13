class StudentProfile:
    pass


name = input("Enter student name: ").strip()

# Create a StudentProfile object
student = StudentProfile()

# Store the name in the object
student.name = name

# Print the stored name
print(f"Student Name: {student.name}")