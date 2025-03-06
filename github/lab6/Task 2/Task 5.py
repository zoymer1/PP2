def write_list_to_file(my_list, filename):
    with open(filename, 'w') as f:
        for item in my_list:
            f.write(str(item) + "\n")

if __name__ == "__main__":
    my_list = ["Apple", "Banana", "Cherry"]
    filename = "my_list.txt"
    write_list_to_file(my_list, filename)
    print(f"Wrote {len(my_list)} items to {filename}")