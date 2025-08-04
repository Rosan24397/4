try:
    print("Reading file content: ")
    with open("sample.txt", "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

# Write to the file
text_to_write = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text_to_write + "\n")
print("Data successfully written to output.txt.")

# Append to the file
text_to_append = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(text_to_append + "\n")
print("Data successfully appended.")

# Read and display final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())
