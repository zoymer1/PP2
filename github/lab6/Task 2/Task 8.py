import os

def safe_delete_file(path):
    if os.path.exists(path):
        print(f"Path '{path}' found.")
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File '{path}' has been deleted.")
        else:
            print("You do not have write permission to delete this file.")
    else:
        print(f"Path '{path}' does not exist.")

if __name__ == "__main__":
    file_to_delete = input("Enter the path of the file to delete: ")
    safe_delete_file(file_to_delete)