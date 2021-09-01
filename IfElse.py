"""Registering a user"""

fname = str(input("Enter your first name"))
lname = str(input("Enter your last name"))
emailID = str(input("Enter your emailID"))
username = str(input("Enter your username"))
pswd = str(input("Enter your password"))
if len(pswd) >= 4:
    rePswd = str(input("Re-enter your password"))
else:
    print("Enter a password with 4 characters")
    exit()
