# Using with keyword to open the file. The reason is  that once the execution of code 
# moves out of with block, the file closes automatically.

# UNDERSTANDING READLINE() METHOD
print("###UNDERSTANDING READLINES() METHOD###\n")
with open('test.txt', 'r') as readFile:     # Opening file with path 'text.txt' in read mode (r)
    print("Readlines()")
    data = readFile.readlines()      # reading 1st line of the file and places cursor at the starting of 2nd line
    print(data)                 # printing data

    print()
    
    print("Using for loop to iterate through each line returned from readlins()")
    for item in data:
        print(item.strip('\n')) 
    