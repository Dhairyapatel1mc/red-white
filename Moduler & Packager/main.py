from toolkit import datetime_utils, math_utils, random_utils, uuid_utils, file_utils, explorer

def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current Date and Time:", datetime_utils.current_datetime())
        elif choice == "2":
            d1 = input("Enter first date (YYYY-MM-DD): ")
            d2 = input("Enter second date (YYYY-MM-DD): ")
            print("Difference:", datetime_utils.date_difference(d1, d2), "days")
        elif choice == "3":
            print("Custom Format:", datetime_utils.custom_format())
        elif choice == "4":
            print("Time elapsed:", datetime_utils.stopwatch(), "seconds")
        elif choice == "5":
            secs = int(input("Enter countdown seconds: "))
            datetime_utils.countdown(secs)
        elif choice == "6":
            break
        else:
            print("Invalid choice!")

def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometry")
        print("4. Area of Shapes")
        print("5. Back to Main Menu")
        ch = input("Enter choice: ")

        if ch == "1":
            n = int(input("Enter number: "))
            print("Factorial:", math_utils.factorial(n))
        elif ch == "2":
            p = float(input("Enter principal: "))
            r = float(input("Enter rate (%): "))
            t = float(input("Enter time (years): "))
            print("Compound Interest:", math_utils.compound_interest(p, r, t))
        elif ch == "3":
            angle = float(input("Enter angle in degrees: "))
            print("Trigonometric Values:", math_utils.trigonometry(angle))
        elif ch == "4":
            print("a) Circle\nb) Rectangle")
            shape = input("Enter shape: ").lower()
            if shape == "a":
                r = float(input("Enter radius: "))
                print("Area of Circle:", math_utils.area_of_circle(r))
            else:
                l = float(input("Enter length: "))
                w = float(input("Enter width: "))
                print("Area of Rectangle:", math_utils.area_of_rectangle(l, w))
        elif ch == "5":
            break
        else:
            print("Invalid choice!")

def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Random Number")
        print("2. Random List")
        print("3. Random Password")
        print("4. Random OTP")
        print("5. Back to Main Menu")
        c = input("Enter choice: ")
        if c == "1":
            a = int(input("Enter start: "))
            b = int(input("Enter end: "))
            print("Random Number:", random_utils.random_number(a, b))
        elif c == "2":
            n = int(input("List size: "))
            print("Random List:", random_utils.random_list(n))
        elif c == "3":
            l = int(input("Password length: "))
            print("Generated Password:", random_utils.random_password(l))
        elif c == "4":
            print("Generated OTP:", random_utils.random_otp())
        elif c == "5":
            break

def uuid_menu():
    print("\nGenerated UUID:", uuid_utils.generate_uuid())

def file_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Back to Main Menu")
        ch = input("Enter choice: ")

        if ch == "1":
            file_utils.create_file(input("Enter filename: "))
        elif ch == "2":
            file_utils.write_file(input("Enter filename: "), input("Enter data: "))
        elif ch == "3":
            file_utils.read_file(input("Enter filename: "))
        elif ch == "4":
            file_utils.append_file(input("Enter filename: "), input("Enter data to append: "))
        elif ch == "5":
            break

def explorer_menu():
    name = input("Enter module name to explore: ")
    explorer.explore_module(name)

def main():
    while True:
        print("\n======================================")
        print(" Welcome to Multi-Utility Toolkit ")
        print("======================================")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            uuid_menu()
        elif choice == "5":
            file_menu()
        elif choice == "6":
            explorer_menu()
        elif choice == "7":
            print("Thank you for using Multi-Utility Toolkit!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
