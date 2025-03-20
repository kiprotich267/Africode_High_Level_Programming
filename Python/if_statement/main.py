# is_present = False 

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

digit1 = int(input("Enter first digit: "))
operator = input("Enter operator: ")
digit2 = int(input("Enter second digit: "))

if operator == "+":
    print(digit1 + digit2)
elif operator == "-":
        print(digit1 - digit2)
elif operator == "*":
        print(digit1 * digit2)
elif operator == "/":
    print(digit1 / digit2)
else:
    print("invalid input")



