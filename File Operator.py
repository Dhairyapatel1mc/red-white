
import os
from datetime import datetime

def main():
    x = JournalManager()
    while True:
        print("\nPersonal Journal Manager")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        match choice:
            case "1":
                print("Enter your journal entry (press Enter twice to finish):")
                lines = []
                while True:
                    line = input()
                    if line == "":
                        break
                    lines.append(line)
                entry = "\n".join(lines)
                x.add_entry(entry)

            case "2":
                x.view_entries()

            case "3":
                keyword = input("Enter keyword or date to search: ")
                x.search_entries(keyword)

            case "4":
                x.delete_all_entries()

            case "5":
                print("Goodbye!")
                break

            case _:
                print("Invalid choice. Try again.")

class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self, text):
       
        if text.strip() == "":
            print("Entry cannot be empty")
            return
        try:
            with open(self.filename, "a") as f:
                f.write(f"[{datetime.now()}]\n{text}\n\n")
            print("Entry added successfully!")
        except Exception as e:
            print("Error while adding entry:", e)

    def view_entries(self):
        
        try:
            with open(self.filename, "r") as f:
                data = f.read().strip()
                if data:
                    print("\nYour Journal Entries:\n")
                    print(data)
                else:
                    print("No entries found. Try adding one first.")
        except FileNotFoundError:
            print("Journal file not found. Add an entry first.")
        except Exception as e:
            print("Error reading file:", e)

    def search_entries(self, keyword):
        
        if keyword.strip() == "":
            print("Please enter a keyword to search.")
            return
        try:
            with open(self.filename, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("File not found. Add an entry first.")
            return
        results = []
        entry = ""
        for line in lines:
            if line.strip() == "":
                if keyword.lower() in entry.lower():
                    results.append(entry.strip())
                entry = ""
            else:
                entry += line
        if keyword.lower() in entry.lower():
            results.append(entry.strip())
        if results:
            print("\nMatching Entries:\n")
            for r in results:
                print(r)
                print()
        else:
            print(f"No entries found for: {keyword}")

    def delete_all_entries(self):
        
        if not os.path.exists(self.filename):
            print("No file to delete.")
            return
        ans = input("Are you sure you want to delete all entries? (yes/no): ").lower()
        if ans == "yes":
            try:
                os.remove(self.filename)
                print("All entries deleted.")
            except Exception as e:
                print("Error deleting file:", e)
        else:
            print("Deletion cancelled.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram stopped.")
    except Exception as e:
        print("Error:", e)

