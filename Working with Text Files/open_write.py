# Using with keyword to open the file. The reason is  that once the execution of code 
# moves out of with block, the file closes automatically.

data = """My name is Siddhant Shah
I live in India
I am a Python Developer"""

# To write data in a file we use 'w' as 2nd parameter of the function open()
with open("test2.txt", 'w') as write_file:   # open files with name test2.txt. If file doesnot exist then a new file will be created.
    write_file.write(data)       # writing data to the text file.


## READING DATA FROM TEST.TXT AND WRITING TO TEST2.TXT
with open("test.txt") as read_file:         # reading data from test.txt
    with open ("test2.txt", "w") as write_file:     # writing data to test2.txt
        write_file.write(read_file.read())
