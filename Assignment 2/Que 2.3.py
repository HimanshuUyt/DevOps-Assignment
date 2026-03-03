# Write to a File Program

file = open("sample.txt", "w")  # "w" mode creates the file (or overwrites if it exists)

file.write("Hello, this is a sample text file.\n")
file.write("This file was created using Python.\n")
file.write("We are learning file handling.\n")

file.close()  # Always close the file

print("Content written successfully to sample.txt")
