#range(start, stop, step)

# for i in range(1,11,2):
#     print(i)

#LIST
students = [ 'Dorothy', 'Rop', 'Kirui', 'Enock','Kipngeno' ]
# for student in students:
#     print(student)
    
    #SET
# students = set(students)
# for student in students:
#     print(student)

#**********task**********
# 1 student1
# 2 student2
# 3 student3
# 4 student4

# Method 1: adding another variable count
# count = 1
# for student in students:
#     print(count, student)
#     count += 1

# Method 2: using len() and range()

# for index in range(len(students)):
#     print(index, students[index])

#**********We cannot use the above method in iterating through set(unindexed)**********
set_students = set(students)
# for index in range(len(set_students)):
#     print(index, set_students[index])

# Method 3: using enumarate()

#(a) list

# for num, student in enumerate(students, start=1):
#     print(num,student)

        # Pass

# for student in students:
#     pass

# for student in students:
#     if student == 'Kipngeno':
#         continue
#     print(student)

# else:
#     print("The list ends here.")

    #******************multiplication table***************
num = 1
for num in range(1, 11):
        print("_______________________________")
        num2 = 1
        for  num2 in range(1, 11):
            print(f"{num} x {num2} = {num * num2}")
        num += 1
    