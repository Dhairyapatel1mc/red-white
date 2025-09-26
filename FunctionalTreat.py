dataset = []

def main_menu():
    
    while True:
        print("\nWelcome to the Data Analyzer and Transformer Program")
        print("\nMain Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")

        choice = input("Please enter your choice: ")

        if choice == '1':
            input_data()
        elif choice == '2':
            display_summary()
        elif choice == '3':
            calculate_factorial()
        elif choice == '4':
            filter_data()
        elif choice == '5':
            sort_data()
        elif choice == '6':
            display_statistics()
        elif choice == '7':
            print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

def input_data():
    
    global dataset
    data = input("Enter data for a 1D array (separated by spaces): ")
    dataset = list(map(int, data.split()))
    print("Data has been stored successfully!")


def display_summary():
    
    global dataset
    if not dataset:
        print("No data available. Please input data first.")
        return
    print("\nData Summary:")
    print(f"- Total elements: {len(dataset)}")
    print(f"- Minimum value: {min(dataset)}")
    print(f"- Maximum value: {max(dataset)}")
    print(f"- Sum of all values: {sum(dataset)}")
    print(f"- Average value: {round(sum(dataset)/len(dataset), 2)}")


def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


def calculate_factorial():
    
    no = int(input("Enter a number to calculate its factorial: "))
    print(f"Factorial of {no} is: {factorial(no)}")


def filter_data():
    
    global dataset
    if not dataset:
        print("No data available. Please input data first.")
        return
    threshold = int(input("Enter a threshold value: "))
    filtered = list(filter(lambda x: x >= threshold, dataset))
    print(f"Filtered Data (values >= {threshold}): {', '.join(map(str, filtered))}")


def sort_data():
    
    global dataset
    if not dataset:
        print("No data available. Please input data first.")
        return
    print("Choose sorting option:\n1. Ascending\n2. Descending")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        dataset.sort()
        print("Sorted Data in Ascending Order:", dataset)
    elif choice == 2:
        dataset.sort()
        dataset.reverse()
        print("Sorted Data in Descending Order:", dataset)
    else:
        print("Invalid choice!")




def display_statistics():
    global dataset
    if not dataset:
        print("No data available. Please input data first.")
        return
    
    print(f"- Minimum value: {min(dataset)}")
    print(f"- Maximum value: {max(dataset)}")
    print(f"- Sum of all values: {sum(dataset)}")
    print(f"- Average value: {round(sum(dataset)/len(dataset), 2)}")

        
main_menu()