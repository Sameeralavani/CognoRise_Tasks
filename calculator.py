def calculator():
    print("Simple calculator")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
calculator()
Operation=int(input("Enter the coice"))

if Operation>4:
    print("Invalid operation")
num1=float(input("Enter the First number"))
num2=float(input("Enter the second number"))
if Operation==1:
    result=num1+num2
    operation_name="Addition"
elif Operation==2:
    result=num1-num2
    operation_name="Subtraction"

elif Operation==3:
    result=num1*num2
    operation_name="Multiplication"
elif Operation==4:
    result=num1/num2
    operation_name="Division"

print("The result of ",Operation, "is",result)

