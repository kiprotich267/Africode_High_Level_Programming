# def sum_num(a, b):
#     return a + b
# results = sum_num(3, 5)
# print(results)

# results2 = sum_num(17, 12)
# print(results2)

# results = sum_num(2, 4)

# Price of an item

# def cart(qty, item, price):
#     print(f"{qty} {item} cost: Ksh{price:.2f}")

# # cart(5, "sugar", 546)
# # cart(2,20, "Banana", )# will throw an error because 3rd argument is float.

# #***************Keyword Arguments***************
# # cart(price=200, qty=3,item="Apple")

# cart(4, item="Bread", price=200)



#********************************************
def cost(qty, price,  item):
    print(f"{qty}kg {item} ksh.{price} Total kshs. {qty*price:.2f}")

    print(cost(4,180,"sugar"))

