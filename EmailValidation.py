# Email Validation 

Email = input("Enter your Email ")

if len(Email) >= 6 and Email.islower():
    print(Email)
else:
    print("Invalid Email")