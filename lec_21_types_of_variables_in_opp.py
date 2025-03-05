# Agenda

"""
   1.Diffrerent types of vriables
   2.Instance object variables
   3.Class object variables
   4.ways to create instance object variables
   5.Ways to create class object variables



"""

# Types of variables 

"""
   1. Global variable
   2. Static variable
   3. Instance object variables
   4. Static variables or class object variables (no static keyword in python)

"""

x = 5 #global variable
def f1():
    a=4 # local variable
class A:
    y = 10 # class object variable
    def __init__(self):
        self.b=6 #instance object variable

# Instance object variables
# instace obj 0 or more

"""
class A:

    code...
    code...

obj1 = A()
obj2 = A()

"""
# class object variables
# one class only has one class obj with the class name we refer
# can have differnt instance objs
"""
calss A:

   code...
   code...

obj1 = A()
obj2 = A()


"""

# ways to create instance object variables
"""
   1. __init__() method
   2. any instance method
   3. Directly through instance object 

   in simple words, if you have a name referring to the instance object, you can create or access instacen object araibles.


"""

"""
# __init__() method

class A:
    def __init__(self,a,b):
        self.a=a # local argumernt variables
        self.b=b


obj1=A(10,20)  #__init__(obj1,10,20)

"""


# any instance method
class A:
    def __init__(self,a,b):
        self.a=a # local argumernt variables
        self.b=b

    def f1(self):
        self.c=7

obj1=A(10,20)  #__init__(obj1,10,20)

obj1.f1() #f1(obj1 as an argument pass ) now the values are a = 10 , b = 30 , c = 7






# Directly through instance object 
class A:
    def __init__(self,a,b):
        self.a=a # local argumernt variables
        self.b=b

    def f1(self):
        self.c=7

obj1=A(10,20)  #__init__(obj1,10,20)

obj1.f1() #f1(obj1)

obj1.d = 55 # create new instace variable through instace obj
print(obj1.a, obj1.b,obj1.c , obj1.d) # Directly through instance object 

"""
  you can create instance obj variables via name use ot refer to instance obj

  kisi b instance method mn , class method mn, static method mn,  in a class , out side of class khein per b function k ander agr apky pass instace obj ko refer krny wala koi name ha to ap is ky ander variables.

"""

# WAYS TO CREATE CLASS OBJECT VARIABLES 

"""
   1. in class body (class obj variable)
   2. in class method
   3. anywhere where you can access class name


"""

#in class method
class A:

    x1 = 4 # calss object variable

    def __init__(self,a,b):
        self.a=a # local argumernt variables
        self.b=b

    def f1(self):
        self.c=7

    @classmethod
    def f2(cls):
        cls.x2=8

obj1=A(10,20) 

obj1.f2() #f2(A) when f2 call the class obj will pass in both now the values are x1= 4, and x2 = 7 
A.f2() #f2(A)




# anywhere where you can access class name

class A:

    x1 = 4 # calss object variable

    def __init__(self,a,b):
        self.a=a # local argumernt variables
        self.b=b

    def f1(self):
        self.c=7

    @classmethod
    def f2(cls):
        cls.x2=8

obj1=A(10,20) 
obj1.f1()
obj1.f2() #f2(A) when f2 call the class obj will pass in both now the values are x1= 4, and x2 = 7 
A.f2() #f2(A)


A.x3= 90 #anywhere where you can access class name
print(A.x3)



print(obj1.__dict__) # check how many instance obj variables have been created in a instace obj

print(A.__dict__) # check the instace obj variables in class obj