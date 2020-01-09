# Using with keyword to open the file. The reason is  that once the execution of code 
# moves out of with block, the file closes automatically.

with open('test.txt', 'r') as readFile:     # Opening file with path 'text.txt' in read mode (r)
    pass


# Testing few Attributes
print("File is closed? {0}".format(readFile.closed))   # attribute to check if file is closed
print("Name of file: {0}".format(readFile.name))   # attribute to know the name of the file
print("Mode in which file is opened: {0}".format(readFile.mode))   # attribute to know the mode in which file is opened
