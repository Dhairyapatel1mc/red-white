print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect an option")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    enter = int(input("Enter your choice: "))

    if enter == 1:
        row = int(input("Enter the number of rows for the pattern: "))
    
        col=row
        i = 1
        while i <= row:
            j = 1
            while j <= i and j <= col:
                print("*", end="")
                j += 1
            print()  
            i += 1

    elif enter == 2:
        a = int(input("Enter the start of the range: "))
        b = int(input("Enter the end of the range: "))
        odd_sum = 0
        even_sum = 0

        for number in range(a, b + 1):  
            if number % 2 == 0:
                print(f"Number {number} is even")
                even_sum += number
            else:
                print(f"Number {number} is odd")
                odd_sum += number

        total_sum = even_sum + odd_sum
        print(f"Sum of all numbers from {a} to {b} is: {total_sum}")

    elif enter == 3:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid option! Please select 1, 2, or 3!")