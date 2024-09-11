Method = str(input("Would you like encryption or decryption? "))
Shift = int(input("List your given value for shift: "))
CodeWord = str(input("Input your secret message: "))

def encrypt():
    Resulting_CodeWord = ""
    for i in CodeWord:
        if i.isalpha():
            unicode = ord(i)
            temp_let = unicode + Shift
            new_let = chr(temp_let)
            Resulting_CodeWord += new_let
        else:
            Resulting_CodeWord += i
    return Resulting_CodeWord

def decrypt():
    Resulting_CodeWord = ""
    for i in CodeWord:
        if i.isalpha():
            unicode = ord(i)
            temp_let = unicode - Shift
            new_let = chr(temp_let)
            Resulting_CodeWord += new_let
        else:
            Resulting_CodeWord += i
    return Resulting_CodeWord

if Method == "encryption":
    print("Message Encrypted: ", encrypt())
elif Method == "decryption":
    print("Message Decrytpted: ", decrypt())
else:
    print("Error: Please choose either encryption or decryption!!")