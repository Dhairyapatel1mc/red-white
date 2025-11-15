import numpy as np

class DataAnalytics:
    def __init__(self):
        self.array = None

    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            elements = input("Enter elements separated by space: ")
            data = list(map(int, elements.split()))
            self.array = np.array(data, dtype=int)

        elif choice == 2:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            elements = list(map(int, input(f"Enter {rows*cols} elements separated by space: ").split()))
            self.array = np.array(elements, dtype=int).reshape(rows, cols)

        elif choice == 3:
            x = int(input("Enter number of matrices: "))
            y = int(input("Enter number of rows: "))
            z = int(input("Enter number of columns: "))
            elements = list(map(int, input(f"Enter {x*y*z} elements separated by space: ").split()))
            self.array = np.array(elements, dtype=int).reshape(x, y, z)
        else:
            print("Invalid choice!")
            return

        print("\nArray created successfully:")
        print(self.array)

        
        print("\nChoose an operation:")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Go Back")
        op = int(input("Enter your choice: "))

        if op == 1:
            idx_input = input("Enter index (comma separated for multi-dim): ")
            idx = tuple(map(int, idx_input.split(",")))
            print("Element:", self.array[idx])

        elif op == 2:
            if self.array.ndim == 1:
                s = input("Enter slice (start:end): ")
                start, end = map(int, s.split(":"))
                print("Sliced Array:", self.array[start:end])

            elif self.array.ndim >= 2:
                r = input("Enter row slice (start:end): ")
                c = input("Enter column slice (start:end): ")

                r_start, r_end = map(int, r.split(":"))
                c_start, c_end = map(int, c.split(":"))

                print("Sliced Array:\n", self.array[r_start:r_end, c_start:c_end])

        else:
            print("Returning to main menu...")

    
    def combine_or_split(self):
        if self.array is None:
            print("No array available!")
            return

        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            elements = list(map(int, input("Enter elements of another array separated by space: ").split()))
            try:
                new_array = np.array(elements, dtype=int).reshape(self.array.shape)
                combined = np.vstack((self.array, new_array))
                print("\nCombined Array (Vertical Stack):")
                print(combined)
            except:
                print("Shape mismatch! Cannot combine arrays.")

        elif choice == 2:
            parts = int(input("Enter number of parts to split: "))
            try:
                split_arrays = np.array_split(self.array, parts)
                print("\nSplit Arrays:")
                for arr in split_arrays:
                    print(arr)
            except Exception as e:
                print("Error splitting array:", e)

    
    def math_operations(self):
        if self.array is None:
            print("No array available!")
            return

        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = int(input("Enter your choice: "))

        elements = list(map(int, input(f"Enter {self.array.size} elements separated by space: ").split()))
        new_array = np.array(elements, dtype=int).reshape(self.array.shape)

        if choice == 1:
            result = self.array + new_array
        elif choice == 2:
            result = self.array - new_array
        elif choice == 3:
            result = self.array * new_array
        elif choice == 4:
            result = self.array / new_array
        else:
            print("Invalid choice!")
            return

        print("\nOriginal Array:\n", self.array)
        print("Second Array:\n", new_array)
        print("Result:\n", result)

    
    def search_sort_filter(self):
        if self.array is None:
            print("No array available!")
            return

        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            val = int(input("Enter value to search: "))
            indices = np.where(self.array == val)
            print("Value found at positions:", indices)

        elif choice == 2:
            sorted_arr = np.sort(self.array, axis=None).reshape(self.array.shape)
            print("\nSorted Array:\n", sorted_arr)

        elif choice == 3:
            condition = int(input("Show values greater than: "))
            filtered = self.array[self.array > condition]
            print("\nFiltered Array:\n", filtered)

    
    
    def aggregate_statistics(self):
        if self.array is None:
            print("No array available!")
            return

        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Sum of Array:", np.sum(self.array))
        elif choice == 2:
            print("Mean of Array:", np.mean(self.array))
        elif choice == 3:
            print("Median of Array:", np.median(self.array))
        elif choice == 4:
            print("Standard Deviation:", np.std(self.array))
        elif choice == 5:
            print("Variance:", np.var(self.array))
        else:
            print("Invalid choice!")

def main():
    analyzer = DataAnalytics()

    while True:
        print("\nWelcome to the NumPy Analyzer!")
        print("====================================")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            analyzer.create_array()
        elif choice == 2:
            analyzer.math_operations()
        elif choice == 3:
            analyzer.combine_or_split()
        elif choice == 4:
            analyzer.search_sort_filter()
        elif choice == 5:
            analyzer.aggregate_statistics()
        elif choice == 6:
            print("Thank you for using the NumPy Analyzer! Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()