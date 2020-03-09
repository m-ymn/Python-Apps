

class Person:
  def __init__(self, name, age,num1,num2):
    self.name = name
    self.age = age
    self.num1 = num1 
    self.num2 = num2 
class Person2:
  def __init__(self, name, age,num1,num2):
    self.name = name
    self.age = age
    self.num1 = num1 
    self.num2 = num2



p1 = Person("ymn",10,20.3,44.765) 
p2 = Person2("tbb",24,10,250.45) 

#l1 = []
l1 = [p1, p2, Person("abb",1.0,0.41,5564)] 

#if isinstance((p1),float) :
#    print("yes it work")

def avg_sum(ln = []):
    sum1 = 0 ;
    for obj1 in ln :
        obj_d = vars(obj1)   # creating dict key value pairs from objects
        l2 = list(obj_d.values())
        print(l2)
        for obj in l2:
            if isinstance(obj,float) or isinstance(obj,int) or isinstance(obj,complex):
                #print(obj)
                sum1 += obj
    print(sum1)

avg_sum(l1) 



