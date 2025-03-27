students = ["Kirui", "Rop", "Dorothy"]

#1. Accessing elements in a list
# print(students[1])
#2 modifying elements in a list
#a. append() method
students.append("Kipngeno")
# print(students)

#b insert()method
students.insert(0, "Enock")
# print(students)

#2 Extend
teachers = ["Mr.Ben", "Mr.Bett"]
students.extend(teachers)
# print(students)

#4 concatenation
combined_list = students + teachers
# print(combined_list)
# **************Removing elements from a list****************
#1 remove()  method
students.remove("Mr.Ben")

#2 pop() method
students.pop()

students.pop(0)

# print(students)

#3 del keyword

del students[1]

#4 clear() method
students.clear()
print(students)
