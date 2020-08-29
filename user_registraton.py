import re


def first_caps_three_letter(first_name):
    count = '^.{3,}$'
    if re.match("^[A-Z]", first_name) and re.match(count, first_name):
        return True
    return False


def valid_email(mail):
    email = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|org|net)"
    if re.search(email, mail):
        return True
    return False


firstname = input("Enter first Name : ")
if first_caps_three_letter(firstname):
    print("First Name is", firstname)
else:
    print("First Name not in correct format")

lastname = input("Enter Last Name : ")
if first_caps_three_letter(lastname):
    print("Last Name is", lastname)
else:
    print("Last Name not in correct format")

email_id = input("Enter your E-mail : ")
if valid_email(email_id):
    print("Email_id is", email_id)
else:
    print("Invalid E-mail ID")
