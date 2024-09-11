new_password = input("Choose your new password (requirements: minimum 12 characters, should include a combination of uppercase and lowercase letters, numbers, and symbols): ")

hasupper = False
haslower = False
hasnumber = False
hassymbol = False

for i in new_password:
    if i.isupper():
        hasupper = True
    elif i.islower():
        haslower = True 
    elif i.isdigit():
        hasnumber = True
    elif not i.isalnum():
        hassymbol = True

if hasupper:
    print("Contains Upper")
elif haslower:
    print("Contains Lower")
elif hasnumber:
    print("Contains Number")
elif hassymbol:
    print("Contains Symbol")

if hasupper and haslower and hasnumber and hassymbol and len(new_password) >= 12:
    print("All checks completed, please proceed")
else:
    print("Check failed. Please recreate your new password following the requirements.")