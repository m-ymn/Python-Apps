
def max_num(num1,num2,num3):

    if num1>=num1 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
num1 = input("enter num1:")
num2 = input("enter num2:")
num3 = input("enter num3:")
print(num1 , num2 , num3)
print(max_num(num1,num2,num3))
