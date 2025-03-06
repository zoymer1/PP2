import os

def check_access(path):
    print(f"Checking access for path: {path}")
    if os.path.exists(path):
        print("  Path exists.")
        print("  Readable?    ", os.access(path, os.R_OK))
        print("  Writable?    ", os.access(path, os.W_OK))
        print("  Executable?  ", os.access(path, os.X_OK))
    else:
        print("  Path does not exist.")

if __name__ == "__main__":
    path_to_check = input("Enter a path to check: ")
    check_access(path_to_check)