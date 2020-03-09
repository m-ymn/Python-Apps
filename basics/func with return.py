

def cube(num):
    return num*num*num
# it breaks the loop after return statement
result = cube(3) # not returning without print
print(cube(3))
print(result)
