from datetime import datetime

PaymentAmount = input("Cost of Purchase: $")
PaymentMethod = input("Debit Card, Credit Card, or Apple Pay? ")
CardNumber = input("Input your 16 digit card number: ")
CardCVV = input("Input your 3 or 4 digit verification pin or CVV: ")
CardExpiration = input("Input your card expiration date (MM/YY): ")

month, year = CardExpiration.split("/")

#Check Month Validity
if int(month) < 1 or int(month) > 12:
    print("Card Month Invalid")
else:
    print("Month Valid.")

#Check Year Validity
current_year = datetime.now().year % 100

if int(year) > current_year:
    print("Year Valid.")
else:
    print("Card Year Invalid")

#Check Card Number Validity
if len(CardNumber) == 16:
    print("Number Valid.")
else:
    print("Card Number Invalid")

#Check CVV Validity
if len(CardCVV) == 3 or len(CardCVV) == 4:
    print("CVV Valid.")
else:
    print("Card CVV Invalid")

