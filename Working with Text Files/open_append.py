# Using with keyword to open the file. The reason is  that once the execution of code 
# moves out of with block, the file closes automatically.

data = """My name is Siddhant Shah
I live in India
I am a Python Developer"""

# To append data in a file we use 'a+' as 2nd parameter of the function open()
with open("test3.txt", 'a+') as append_file:   # open files with name test2.txt. if file doesnot exist then a new file will be created.
    append_file.write(data)       # writing data to the text file.

