def create_file(filename):
    with open(filename, 'w') as f:
        pass
    print("File created successfully!")

def write_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)
    print("Data written successfully!")

def read_file(filename):
    with open(filename, 'r') as f:
        print(f.read())

def append_file(filename, data):
    with open(filename, 'a') as f:
        f.write(data + "\n")
    print("Data appended successfully!")
