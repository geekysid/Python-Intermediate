# Using with keyword to open the file. The reason is  that once the execution of code 
# moves out of with block, the file closes automatically.

# UNDERSTANDING READ() METHOD
print("###UNDERSTANDING READ() METHOD###\n")
with open('test.txt', 'r') as readFile:     # Opening file with path 'text.txt' in read mode (r)
    print("read()")
    data = readFile.read()      # reading entire file at once
    print(data)                 # printing data

print()

with open('test.txt', 'r') as readFile:     # Opening file with path 'text.txt' in read mode (r)
    print('read(50)')
    data = readFile.read(50)      # reading and returning 1st 50 characters from the file
    print(data)                 # printing data
    
    print('\nnext read(50)')
    data = readFile.read(50)      # reading and returning next 50 characters from the file
    print(data)                 # printing data
        
    print("Current position of cursor: {}".format(readFile.tell()))  # using tell function to get position of cursor
    readFile.seek(0)        # cursor moves back to the 0th position (index) of the file
    print("Position of cursor after seek(0): {}".format(readFile.tell()))  # using tell function to get position of cursor
    
    print('\nnext read(50) from the 0th position')
    data = readFile.read(50)      # reading and returning 50 characters from 0th position of the file
    print(data)                 # printing data

    readFile.seek(0)
    
    print()
    print("using while loop and looping through each line of file using read(charSize)")
    # Looping through the file with specific number of characters each time
    read_size = 20      # number of characters returned after each iterations
    text = readFile.read(read_size)     # reads and returns 1st set of characters from file
    line_num = 1

    while len(text) > 0:        # looping only if size of text returned from the read() is greater the 0
        print("Text for iteration # {0}".format(line_num))
        print(text)
        text = readFile.read(read_size)
        line_num += 1
