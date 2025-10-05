def menu():
    persons = []
    employees = []
    managers = []
    developers = []

    while True:
        print("\n=== Employee Management System ===")
        print("1. Create Person")
        print("2. Create Employee")
        print("3. Create Manager")
        print("4. Create Developer")
        print("5. Show Details")
        print("6. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                p = Person(name, age)
                persons.append(p)
                print(f"Person created: {name}, Age: {age}")

            case "2":
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                emp_id = input("Enter Employee ID: ")
                salary = float(input("Enter Salary: "))
                e = Employee(name, age, emp_id, salary)
                employees.append(e)
                print(f"Employee created: {name}, ID: {emp_id}, Salary: ${salary}")

            case "3":
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                emp_id = input("Enter Employee ID: ")
                salary = float(input("Enter Salary: "))
                dept = input("Enter Department: ")
                m = Manager(name, age, emp_id, salary, dept)
                managers.append(m)
                print(f"Manager created: {name}, Department: {dept}")

            case "4":
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                emp_id = input("Enter Employee ID: ")
                salary = float(input("Enter Salary: "))
                lang = input("Enter Programming Language: ")
                d = Developer(name, age, emp_id, salary, lang)
                developers.append(d)
                print(f"Developer created: {name}, Language: {lang}")

            case "5":
                print("\nChoose details to show:")
                print("1. Person")
                print("2. Employee")
                print("3. Manager")
                print("4. Developer")
                sub = input("Enter your choice: ")

                if sub == "1":
                    if persons:
                        for p in persons:
                            print("\n--- Person Info ---")
                            p.display()
                    else:
                        print("No persons found.")

                elif sub == "2":
                    if employees:
                        for e in employees:
                            print("\n--- Employee Info ---")
                            e.display()
                    else:
                        print("No employees found.")

                elif sub == "3":
                    if managers:
                        for m in managers:
                            print("\n--- Manager Info ---")
                            m.display()
                    else:
                        print("No managers found.")

                elif sub == "4":
                    if developers:
                        for d in developers:
                            print("\n--- Developer Info ---")
                            d.display()
                    else:
                        print("No developers found.")

                else:
                    print("Invalid sub-choice.")

            case "6":
                print("Exiting system... Goodbye!")
                break

            case _:
                print("Invalid option! Please select from 1 to 6.")


class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def __del__(self):
        print(f"Person object ({self.name}) destroyed.")


class Employee(Person):
    def __init__(self, name="", age=0, emp_id=None, salary=None):
        super().__init__(name, age)
        self.__emp_id = emp_id
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_emp_id(self):
        return self.__emp_id

    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def display(self):
        super().display()
        print(f"Employee ID: {self.__emp_id}")
        print(f"Salary: ${self.__salary}")

    def __del__(self):
        print(f"Employee ({self.name}) with ID {self.___emp_id} destroyed.")


class Manager(Employee):
    def __init__(self, name="", age=0, emp_id=None, salary=None, dept=""):
        super().__init__(name, age, emp_id, salary)
        self.dept = dept

    def display(self):
        super().display()
        print(f"Department: {self.dept}")

    def __del__(self):
        print(f"Manager ({self.name}) destroyed.")


class Developer(Employee):
    def __init__(self, name="", age=0, emp_id=None, salary=None, language=""):
        super().__init__(name, age, emp_id, salary)
        self.language = language

    def display(self):
        super().display()
        print(f"Programming Language: {self.language}")

    def __del__(self):
        print(f"Developer ({self.name}) destroyed.")


print("Inheritance Check:")
print("Manager is subclass of Employee:", issubclass(Manager, Employee))
print("Developer is subclass of Employee:", issubclass(Developer, Employee))

menu()
