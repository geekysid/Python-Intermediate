# reading binary data from image file using 'rb' as operation mode
with open("sid.png", 'rb') as read_image:
    data = read_image.read()

# writing binary data to a new image file using 'wb' as operation mode
with open("sid_copy.png", "wb") as write_image:
    write_image.write(data)