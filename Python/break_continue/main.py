# correct_pin = "1234"
# attempts = 0
# max_attempts = 3

# while attempts < max_attempts:
#     pin = input("Enter your M-pesa pin")
#     attempts += 1

#     if pin == "":
#         print("You have not entered any pin")
#         continue
#     if pin == correct_pin:
#         print("Pin accepted! Transaction successful")
#         break
#     remaining_attempts = max_attempts - attempts
#     if remaining_attempts > 0:
#         print(f"Wrong pin entered. you have {remaining_attempts} attempts left")
#     else:
#         print("Account locked! Too many attempts")

num = 0
while num <= 10:
    num += 1 
    if num % 2 == 0:
        continue
    print(f"odd number: {num}")
    