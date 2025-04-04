# file input and output

#open() function
#read, write, append
#close() function

#syntax
# open("file", "mode")

#MODES
#r - read
#w - write - create a file if it doe not exist, or overwrite the content if it exists
#a - append - create a file if it does not exist, or add content to the end of the file
#r+ - read and write - read and write to a file 
#b - binary - read or write a file in a binary mode

#     Read 
# f= open("test.txt",  "r")
# # print(f.read())
# print(f.readline())
# f.close()
#     Readlines


#     Write

# f = open("output.txt", "w")
# # f.write("this is a test file/context.")
# f.write("this content will overwrite the existing content")
# f.close()

#    Append

f = open("output.txt", "a")
f.write(" this content will be added to the end of te file.")
f.close()

#     Binary
b = open("download.jpeg", "rb")
# print(b.read())

#  copy image
with open("download.jpeg", "rb") as b:
     for data in b:
       
        with open("copied.jpeg", "wb") as f:
            f.write(data)



