def count_lines_in_file(filename):
    line_count = 0
    with open(filename, 'r') as f:
        for _ in f:
            line_count += 1
    return line_count

if __name__ == "__main__":
    file_to_check = input("Enter the text file path: ")
    try:
        lines = count_lines_in_file(file_to_check)
        print(f"Number of lines in {file_to_check}: {lines}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)