# is_present = True

# if is_present:
#     print("start the lesson")
# else:
#     print("skip the lesson")

# age = 18
# is_citizen = False
# has_passport = True

# if age >= 18 and is_citizen:
#     print("you are eligible to vote")
# elif not is_citizen and has_passport:
#     print("you can vote but you are not a citizen")
# else :
#     print("you are not eligible to vote")

# monthly_income = int(input("Enter your monthly income: "))
# rent = int(input("enter your monthly rent: "))
# takeout_budget = int(input("enter your monthly takeout"))
# actual_takeout = int(input("enter your actual takeout: "))
# savings_goal = int(input("enter your savings goal: "))

# if rent > monthly_income * 0.3:
#     print("your rent is eating your paycheck like a hungry hippo")
#     if takeout_budget < actual_takeout:
#         print(f"you have blown your takeout budget by Ksh.{actual_takeout - takeout_budget}")

# elif monthly_income - rent - actual_takeout < savings_goal:
#     print("your savings goal is more of a saving fantasy at this rate")
#     print(f"your savings goal is {savings_goal} but you are only saving {monthly_income - rent - actual_takeout}")

# else:
#     print("your budget is actualy balanced! Are you a wizard?")



#*****************************shopping cart decission tree************************************
# cart_total = 78
# distance_to_free_shipping = 22
# items_in_cart = ["sensible shoes",  "questianable fashion choice", "items you dont need"]
# bank_account_status = "crying"

# if cart_total < 100 and distance_to_free_shipping > 0:
#     print(f"only Ksh.{distance_to_free_shipping}")

#***********Calculator****************

# digit1 = int(input("Enter first digit: "))
# operator = input("Enter operator: ")
# digit2 = int(input("Enter second digit: "))

# if operator == "+":
#     print(digit1 + digit2)
# elif operator == "-":
#         print(digit1 - digit2)
# elif operator == "*":
#         print(digit1 * digit2)
# elif operator == "/":
#     print(digit1 / digit2)
# else:
#     print("invalid input")


# a = 10
# b = 5
# c = 10
# text = "Hello"
# list_x = ["1", "2", "3", "4", "5"]
# list_y = ["1", "2", "3", "4", "5"]
# list_2 = list_x 

# if a > b and c >= a:
#     print("a is greater than b and c is greater than or equal to a")
# elif a <= b or c != b:
#     print("Eithera is less OR equal to b or c is not equal to b")
# else:
#     print("None of the conditions were met")

# if list_x == list_y and list_x is not list_y:
#     print("list_x and list_y have the same values but are different objects")
# elif not(a==b):
#     print("a is not equal to b")
# else:
#     print("None of the conditions were met")

#     if "e" in text and 6 not in list_x:
#         print("The letter 'e' is in the text variable and the number 6 is not in the list_x")
#     elif "x" not in text and 3 not in list_x:
#         print("Either letter 'x' is not in the text variable OR the number 3 is in the list_x")
#     else:
#         print("None of the membership conditions were met")

#     if a > b and (3 in list_x or text is not None):
#         print("complex condition met: a is greater than b AND 3 is in list_x OR is not None")
#     elif list_x is list_2 and len(text) > 0:
#         print("list_x and list_z are the same object AND the lenght of text is greater than 0")
#     else:
#         print("none of the complex were met")

#**************leap years*************
# for year in range(2000, 2026):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(f"{year} is a leap year")
    # else:
    #     print(f"{year} is not a leap year")

    #*************while********
# while True:
#     print("hello")
# count = 0
# while count < 1000:
#     print(count)
#     count += 1  



