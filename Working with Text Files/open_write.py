# Using with keyword to open the file. The reason is  that once the execution of code 
# moves out of with block, the file closes automatically.

data = """My name is Siddhant Shah
I live in India
I am a Python Developer"""

print(data)

with open("test2.txt", 'w') as write_file:   # open files with name test2.txt. if file doesnot exist then a new file will be created.
    write_file.write(data)       # writing data to the text file.


## READING DATA FROM TEST.TXT AND WRITING TO TEST2.TXT

# reading data from test.txt
with open("test.txt") as read_file:
    data_to_write = read_file.read()

# writing data to test2.txt
with open ("test2.txt", "w") as write_file:
    write_file.write(data_to_write)
