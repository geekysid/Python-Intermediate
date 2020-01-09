# Using with keyword to open the file. The reason is  that once the execution of code 
# moves out of with block, the file closes automatically.
 
# UNDERSTANDING READLINE() METHOD
print("###UNDERSTANDING READLINE() METHOD###\n")

with open('test.txt', 'r') as readFile:     # Opening file with path 'text.txt' in read mode (r)
    print("1st readline()")
    data = readFile.readline()      # reading 1st line of the file and places cursor at the starting of 2nd line
    print(data)                 # printing data
    
    print("2nd readline()")
    data = readFile.readline()      # reading entire next lineand places cursor at the starting of 3rd line
    print(data)                 # printing data
    
    print("Current position of cursor: {}".format(readFile.tell()))  # using tell function to get position of cursor
    readFile.seek(10)        # cursor moves back to the 10th position (index) of the file
    print("Position of cursor after seek(10): {}".format(readFile.tell()))  # using tell function to get position of cursor
    
    print("\n2nd readline()")
    data = readFile.readline()      # reading from 10th index of the file upto the end of that line and moves cursor to starting of next line
    print(data)                 # printing data

print()

# another way of reading each line from a file
print("Using for loop to loop through each line of file")
with open('test.txt', 'r') as readFile:     # Opening file with path 'text.txt' in read mode (r)
    for line in readFile:
        print(line.strip('\n'))

print()

# another way of reading each line from a file
print("Using while loop and looping through each line of file using readline()")
with open('test.txt', 'r') as readFile:     # Opening file with path 'text.txt' in read mode (r)
    data = readFile.readline()

    while len(data) > 0:
        print(data.strip('\n'))
        data = readFile.readline()