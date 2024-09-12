import random
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case=upper_case.lower()
digits="0123456789"
symbols="@%&*!"
length=int(input("Enter the desidre length of the password"))
amount=1
upper,lower,digit,symb=True,True,True,True
pasw=""
if length<1:
    print(f"Password length should be of length greater than 6")
else:
    if upper:
        pasw+=upper_case
    if lower:
        pasw+=lower_case
    if digit:
        pasw+=digits
    if symb:
        pasw+=symbols
    for x in range(amount):
        password="".join(random.sample(pasw,length))
        print(password)
