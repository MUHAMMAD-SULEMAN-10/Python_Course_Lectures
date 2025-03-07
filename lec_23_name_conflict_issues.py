#Agenda
"""
1.Instance object variables name conflict
2.class object varibles name conflict 
3.Instance method name conflict
4.static method name conflict 
5.class method name conflict
6.Instance object variable & class object variable name conflict in single class 

"""

# Instance object variables name conflict

class A:
    def __init__(self):
        self.a=5

class B(A): 
    def __init__(self):
        self.a=4
obj1=B() # __init__(obj1)
print(obj1) 
print(obj1.a)



#use super method
print("Using super () now the value is 5 ============")


class A:
    def __init__(self):
        self.a=5

class B(A): 
    def __init__(self):
        self.a=4
        super().__init__()
obj1=B() # __init__(obj1)

print(obj1.a)



#.class object varibles name conflict 
print("class object varibles name conflict  ============")
class A:
    x=10
class B(A):
    y=20

print(A.x,B.x) #inheritence is occure answer is 10,10


print("class object varibles name conflict  ============")

class A:
    x=10
class B(A):
    x=20

print(A.x,B.x) #no inheritence  is occure answer is 10,20


#Instance method name conflict

print("Instance method (functions) name conflict ============")

#CASE 1 Method Overiding argument same.

#child version override parent class version and when we call child only child will call not parent if we want to call parent then ssuper.f1() inside child class.

class A:
    def f1(self):
        print("A")
class B(A):
    def f1(self):
        print("B")

obj1=B()
obj1.f1() # B will print 



print("Instance method (functions) name conflict ============")

#CASE 2 Method Hiding argument change.
#parent will hide 

class A:
    def f1(self,a):
        print("A")
class B(A):
    def f1(self):
        print("B")

obj1=B()
# obj1.f1(6) # arguemnt pass explicitly // but error


print(" static method name conflict  ============")
#static method name conflict 

#CASE 1


class A:
    @staticmethod
    def f1(a,b): #no self in staticmethod
        print("A")
class B(A):
    @staticmethod
    def f1(a,b):
        print("B")

B.f1(3,5) #no implicitly passed anything in static method 
print(" static method name conflict  ============")
#no child class static method 

class A:
    @staticmethod
    def f1(a,b): #no self in staticmethod
        print("A")
class B(A):
    def f1(a,b):
        print("B")

B.f1(3,5) # it will work but a should be self  but not good practice




#now make the instace object of B class 
print(" static method name conflict  ============")

class A:
    @staticmethod
    def f1(a,b): #no self in staticmethod
        print("A")
class B(A):
    def f1(a,b):
        print("B")
obj=B()
# obj.f1(3,5) #error because we are passing 3 arguemnts 




print(" static method name conflict  ============")



class A:
    @staticmethod
    def f1(a,b): #no self in staticmethod
        print("A")
class B(A):
    def f1(a,b):
        print("B is instace") #no existance
    @staticmethod
    def f1(a,b):
        print("B is static") #will exists

#we make f1() function obj and another we make f1() with same name in one class arguemnts match or not and 2nd one is exists and will execute.

obj=B()
#obj.f1(3) #error
"""
print("class method name conflict   ============")
#class method name conflict 
#same story will happen


class A:
    @classmethod
    def f1(cls,a):
        print("A")
class B:
    @classmethod
    def f1(cls,b,c):
        print("B") """

# B.f1(4) #error due to arguments and first go in child will match the arguments this is rule

print("Insatace object variable and class object variable name conflict in single class.")
#Insatace object variable and class object variable name conflict in single class.

class A: #class obj variables are shareable among all instance objs 
    x = 10 #static variable 
    
obj=A()
obj.x=15 #will create instace obj variable and print it and do no go in class variable static 
print(obj.x)


#if __init__() method came in class then __init__() will execute first 

class A: 
    x = 10 #static variable 
    def __init__(self):
        self.x=15
obj=A()
print(obj.x)