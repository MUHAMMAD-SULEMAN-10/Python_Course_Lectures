# Syntax of class 

"""
class className:
   varables 
   functions

   calss definition must be executed before its use.

"""

class Test: # class object with name Test 

    x1=5
    x2=6
    def f1(self):
        print("Hello")

t1= Test() # instace object created 
t2= Test()
t3= Test()
t1.f1()  # instance method is call 
print(t1) 
print(type(t1))



# <class '_main_.Test'> main file name like lec_18_classes_objects.py which is our main module and main file in moudle and the test class is the data type of t1.


# Object 

"""
   Three types of objects 

   1. Instace Object = object 
   2. class object 
   3. function object 

"""

# Creating instance Object 
   
"""
class Test:

   varables 
   functions

t1=  Test() t1 contain the id of test class object
t2 = Test()
t3 = Test()

"""

# Differnce between instance object vs class object
"""
   class object

   1.if we created the class then class object is created
   2.a variable with same name of calss refer to this class 
   3.a class name is a refrence variable which store the id of class object.
   4.for one class only one class object will be created 
   5. class object also has varaible name & may be fulfield at begining it depends 

"""
"""
   instance object

   t3 = Test()
   instace object at begining are empty or always empty ?  no after creating these the variable data come.

   1. instace object refer to the class name
   2. for one calss instance object will be 0 and more 
   3. instnce object also has variable name 

"""
"""
self is required in instance methods to access the object’s properties or methods.
Without self, Python considers the method as a static method.
To call f1(), use the instance object like t1.f1().

"""


# static method 

class Test:
    x1 = 5
    x2 = 6
    
    @staticmethod
    def f1():
        print("static method")

Test.f1()  # Directly call without self



# Note:
"""
   1. test  is only a calss object 
   2. Test () is a fucnction call to create instance object
     t1=  Test()
"""