# Student Grades Program

students = {}

while True:
    print("\n1. Add Student")
    print("2. Update Student Grade")
    print("3. Print All Student Grades")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        students[name] = grade
        print("Student added successfully!")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Grade updated successfully!")
        else:
            print("Student not found!")

    elif choice == "3":
        if students:
            print("\nStudent Grades:")
            for name, grade in students.items():
                print(name, ":", grade)
        else:
            print("No students in the record.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please select 1-4.")
