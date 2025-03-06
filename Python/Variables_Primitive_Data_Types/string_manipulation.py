# **********String Slicing**********
# greeting = "Hello"
# name = "John Doe"

# x = greeting + " " + name[0:4]
# print(x)

# **********Concatenation*********
# greeting = "Hello "
# name = "Jane Doe"

# x = greeting + name
# print(x)

# **********string method*********
name = "john doe"
new_name = "DOE"

# print(help(str))

#**********1 capitalize() method********
# cap_name =name.capitalize()
# print(cap_name)

#**********2 upper() method********
# upper_name = name.upper()
# print(upper_name)

#**********3 lower() method********
# lower_name = new_name.lower()
# print(lower_name)

#**********4 count() method********
# print(name.count('o'))
phone = "0726","123","456"

#**********5 split() method********
# new_list = name.split()
# print(new_list)

# new_phone = phone.split('-')
# print(new_phone)

#**********6 join() method********

# joined_phone = ''.join(phone)
# print(joined_phone)

# print(type(phone))
# print(type(joined_phone))

#**********7 isalnum() method********

python3 = "python3"

# print(python3.isalnum())

# print(python3.isalpha())

#**********9. isdigit) method********

# text = "python123"
# text2 ="123"

# print(text.isdigit())

#**********10. isspace() method********
# text = " "
# print(text.isspace())

#**********11. startswith() method********
python = "python3" 
# print(python.startswith("p"))

#**********12. endswith() method********
# print(python.endswith("3"))

#**********13. replace()******
# my_string = "I love python"
# new_string = my_string.replace("python", "javascript")
# print(new_string)

#**********14. strip()******

text = "  python   "
print(text)
new_text = text.strip()
print(new_text)


#**********15. f-string********

    #old way of formatting strings
string = "John"
age = 23
height = 5.6
# print("Hello,{} you are {} years old and {} tall ".format(string, age, height))

#     #f-string
# print(f"Hello, {string.upper()} you are {age + 1} years old and {height} tall")


