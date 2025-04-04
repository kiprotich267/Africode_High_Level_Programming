#     read
with open('example.txt', 'r') as file:
    lines = file.readlines()

# This will print the lines of the file
for line in lines:
    print(line)  
    file.close()

    #        WRITE

    with open('example.txt', 'w') as file:
        file.write("This is a write example.")


        #    APPEND

    with open('example2.txt', 'a') as file:
        file.write("This will create another file.")
    with open('example2.txt', 'a') as file:
        file.write("This is will be added to the end of the file")


        #    BINARY

    with open('assgn.jpeg', 'rb') as file:
        content = file.read()  # Reads the entire file as bytes
    print(content)  # Output will be in byte format
# Open the source image in binary read mode
with open('assgn.jpeg', 'rb') as source_file:
    # Read the entire content of the image file
    image_content = source_file.read()

# Open the destination image in binary write mode
with open('copied_assgn.jpeg', 'wb') as dest_file:
    # Write the content to the destination image
    dest_file.write(image_content)




