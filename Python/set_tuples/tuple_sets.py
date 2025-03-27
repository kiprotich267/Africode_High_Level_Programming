
# import sys
# import timeit

# lst = ["Rop", "Enock", "Dorothy","Kirui", "kipngeno", "Kirui"]
# tup = tuple(lst)
# print("Tuple", sys.getsizeof(tup))
# print("List", sys.getsizeof(lst))

# print("Tuple:", timeit.timeit(stmt="tup = ('Rop', 'Enock', 'Dorothy','Kirui', 'kipngeno', 'Kirui') "))
# print("List:", timeit.timeit(stmt="lst = ['Rop', 'Enock', 'Dorothy','Kirui', 'kipngeno', 'Kirui'] "))
# print (help(tup))
# print(dir(tup))
# methods available in tuple

# print(tup.index("Rop"))
# print(tup.count("Rop"))
# print(len(tup))

# print("Kirui" in tup)

    #Set


my_set = {"Rop", "Enock", "Dorothy","Kirui", "kipngeno", "Kirui"}
another_set = {"Enock", "Ben", "Joan"}
# print(my_set)
# combined_set = my_set.union(another_set)
# print(combined_set)
# my_set.add("Joan")
# my_set.remove("Enock")
# print(my_set)
# print(my_set.intersection(another_set))

print(my_set.issubset(another_set))
print(my_set.issuperset(another_set))
print(my_set.isdisjoint(another_set))