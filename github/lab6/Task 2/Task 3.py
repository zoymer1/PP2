import os

def path_info(path):
    if os.path.exists(path):
        print(f"Path exists: {path}")
        print("  Filename portion:", os.path.basename(path))
        print("  Directory portion:", os.path.dirname(path))
    else:
        print(f"Path does not exist: {path}")

if __name__ == "__main__":
    path_to_check = input("Enter a path: ")
    path_info(path_to_check)