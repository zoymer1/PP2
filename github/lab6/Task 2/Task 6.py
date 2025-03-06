import string

def create_alphabet_files():
    for letter in string.ascii_uppercase:
        filename = f"{letter}.txt"
        with open(filename, 'w') as f:
            f.write(f"This is file {filename}")

if __name__ == "__main__":
    create_alphabet_files()
    print("Created files A.txt through Z.txt.")