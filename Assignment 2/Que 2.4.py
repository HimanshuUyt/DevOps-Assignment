# Read from a File Program

# Open the file in read mode
file = open("sample.txt", "r")  # "r" mode is for reading

# Read the entire content
content = file.read()

# Print the content
print("File Content:\n")
print(content)

# Close the file
file.close()
