import os

def list_contents(path):
    print("Directories in the path:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print("  ", item)
    print("\nFiles in the path:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print("  ", item)
    print("\nAll directories and files in the path:")
    for item in os.listdir(path):
        print("  ", item)

if __name__ == "__main__":
    path_to_check = input("Enter the path to list: ")
    if os.path.exists(path_to_check):
        list_contents(path_to_check)
    else:
        print("The specified path does not exist.")