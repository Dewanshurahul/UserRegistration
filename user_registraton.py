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


def mobile_format(mobile_number):
    mobile = "^((\+)?(\d{2}[-]))?(\d{10}){1}?$"
    if (re.search(mobile, mobile_number)):
        return True
    return False


def valid_password(password):
    count = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    if re.match(count, password):
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

# email_id = input("Enter your E-mail : ")
# if valid_email(email_id):
#     print("Email_id is", email_id)
# else:
#     print("Invalid E-mail ID")
#
# mobile_number = input("Enter Mobile Number as XX-XXXXXXXXXX")
# if mobile_format(mobile_number):
#     print("Mobile Number is", mobile_number)
# else:
#     print("Invalid Mobile Number Format")
#
# password = input("Enter Password : ")
# if valid_password(password):
#     print("Passowrd is", password)
# else:
#     print("Enter atleast 8 digit Password with atleast one Numeric digit and Upper Case in it")


def select_validation(case):
    if case == 1:
        print(valid_email(input("Enter your E-mail: ")))
    elif case == 2:
        print(mobile_format(input("Enter Mobile Number as XX-XXXXXXXXXX: ")))
    elif case == 3:
        print(valid_password(input("Enter Password : ")))
    else:
        print("Invalid Input Enter value between 1-3",)


choice = int(input("Enter 1: for e-Mail Validation\nEnter 2: for Mobile Number Validation\nEnter 3: for Password Validation: "))
select_validation(choice)
