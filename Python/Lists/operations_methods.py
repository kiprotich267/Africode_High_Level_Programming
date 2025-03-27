# 1. Slicing in list
# fruits = ["apples","banana","cherry","date","elderberry","fig","grape"]
#print(fruits[1:4])
#omitting indices
#print(fruits[:4])

#negative indices
#print(fruits[:-2])

# step value:start:stop:step
#print(fruits[::3])
fruits =  ["apples","banana","jerry","date","elderberry","fig","fig","grape"]
# 2, changing items
fruits[2] = 'cherry'
#print(fruits)

#changing multiple items
#fruits[2:3] = ['orange','pineapple']
#print(fruits)


# 3.sort()
#sorting in ascending order
fruits.sort()
#print(fruits)

#sorting in descending order

fruits.sort(reverse=True)
#print(fruits)

# 4.sorted()
sorted_fruits = sorted(fruits)
#print(sorted_fruits)

# 5.reverse()

# fruits.reverse()
#print(fruits)

#6 counts()

#counts = fruits.count('banana)

#7 index()

# banana_index = fruits.index('fig')
# print(banana_index)

# print(fruits)
thislist = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
x = sum(thislist)
print(x)



lowest = min(thislist)
print(lowest)

highest = max(thislist)
print(highest)