

#empl= open("emp.txt", "r") # read a file
#open("emp.txt", "r+")  # read & write to a file
#empl= open("emp.txt", "a")  # append to a file

empl= open("emp1.txt", "w")
print(empl.readable())

empl.write("\ntoby is HR")
#for emplo in empl.readlines():
#    print(emplo)

#print(empl.readline())


#print(empl.readline())

empl.close()