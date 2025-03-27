# 1 With initial items

# students = ['Enock', 'Kirui', 'Kipngeno', 'Dorothy', 'Rop']
# print(students)

#2 using list constructor

# fruits = list()
# print(fruits)

#3 convertinga string to a list
# string = "Hello World"
# print(string)
# string_list = list(string)
# print(string_list)

#4 empty list
# attendance = []
# print(attendance)

#5 pattern

# print(pattern)

#6 list comprehension

# numbers = [ x for x in range(1, 11)]
# print(numbers)

# square = [i**2 for i in range(1, 11)]
# print(square)

#***********list comprehension***********

# students = ['Enock', 'Kirui', 'Kipngeno', 'Dorothy', 'Rop']
# students_present = []

# for x in students:
#     if "i" in x:
#         students_present.append(x)
# print(students_present)

students = ['Enock', 'Kirui', 'Kipngeno', 'Dorothy', 'Rop']
students_present = [x for x in students if "i" in x]
print(students_present)
   