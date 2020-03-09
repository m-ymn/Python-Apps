
num1 = float(input("enter first num: "))
op = input("enter operator: ")
num2 = float(input("enter 2nd num: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("invalid operator")