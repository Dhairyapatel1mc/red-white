students = {}

while True:
    print("Welcome to the Student Data Organizer!\n")
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":   
            sid = input("Enter Student ID: ")
            if sid in students:
                print(" Student ID already exists!\n")
                continue
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ")
            dob = input("Enter Date of Birth (YYYY-MM-DD): ")
            subjects = input("Enter Subjects (comma-separated): ").split(",")
            subjects = [s.strip() for s in subjects]

            students[sid] = {
                "Name": name,
                "Age": age,
                "Grade": grade,
                "DOB": dob,
                "Subjects": subjects
            }
            print(" Student added successfully!\n")

        case "2":   
            if not students:
                print("No students found!\n")
                continue
            print("\n--- Display All Students ---")
            for sid, info in students.items():
                print(f"Student ID: {sid} | Name: {info['Name']} | Age: {info['Age']} "
                      f"| Grade: {info['Grade']} | DOB: {info['DOB']} | Subjects: {', '.join(info['Subjects'])}")
            print()

        case "3":   
            sid = input("Enter Student ID to update: ")
            if sid not in students:
                print(" Student not found!\n")
                continue
            print("Leave field empty to keep current value.")
            name = input(f"Enter new Name ({students[sid]['Name']}): ") 
            age = input(f"Enter new Age ({students[sid]['Age']}): ")
            grade = input(f"Enter new Grade ({students[sid]['Grade']}): ") 
            dob = input(f"Enter new DOB ({students[sid]['DOB']}): ") 
            subjects = input(f"Enter new Subjects (comma-separated) ({', '.join(students[sid]['Subjects'])}): ")

            students[sid]['Name'] = name
            students[sid]['Age'] = int(age) if age else students[sid]['Age']
            students[sid]['Grade'] = grade
            students[sid]['DOB'] = dob
            if subjects:
                students[sid]['Subjects'] = [s.strip() for s in subjects.split(",")]

            print(" Student updated successfully!\n")

        case "4":   
            sid = input("Enter Student ID to delete: ")
            if sid in students:
                del students[sid]
                print(" Student deleted successfully!\n")
            else:
                print(" Student not found!\n")

        case "5":   
            all_subjects = set()
            for info in students.values():
                all_subjects.update(info["Subjects"])
            if all_subjects:
                print(" Subjects Offered:", ", ".join(all_subjects), "\n")
            else:
                print("No subjects available yet!\n")

        case "6":   
            print(" Exiting... Goodbye!")
            break

        case _:     
            print(" Invalid choice! Try again.\n")