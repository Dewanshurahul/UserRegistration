import re


def first_caps_three_letter(first_name):
    count = '^.{3,}$'
    if re.match("^[A-Z]", first_name) and re.match(count, first_name):
        return True
    return False


firstname = input("Enter first Name : ")
if first_caps_three_letter(firstname):
    print(firstname)
else:
    print("First Name not in correct format")

lastname = input("Enter Last Name : ")
if first_caps_three_letter(lastname):
    print(lastname)
else:
    print("Last Name not in correct format")
