def copy_file(source, destination):
    with open(source, 'r') as src:
        contents = src.read()
    with open(destination, 'w') as dst:
        dst.write(contents)

if __name__ == "__main__":
    source_file = input("Enter the source file: ")
    destination_file = input("Enter the destination file: ")
    try:
        copy_file(source_file, destination_file)
        print(f"Copied contents from {source_file} to {destination_file}.")
    except FileNotFoundError:
        print("Source file not found.")
    except Exception as e:
        print("An error occurred:", e)