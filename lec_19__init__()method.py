

# __init__() method


class Test:
       def __init__(self): # automatically called 
          
          print("Hello")

t1 = Test() 
t2 = Test()
t3 = Test()

"""
   1. you can define __init__() method in the class (that is, it is optional)

   2. Similar to the concept of constructor in c++ or java.

   In Python, constructors are always called automatically — you cannot call them manually.

   3. __init__() method invokes (call) implicity (by default) everytime 
   when an instance object is created.

   4. Therefor ,__init__() method is the first method runs for an 
   object, just after the object creation.

"""


# Defining __init__() method

"""
   class Test:
   
       def__init__(self):

         print("Hello")
         .......
         a = 5 // local variable lide time only in the function differnt memory assign 

         self.a=4 // it is an instace object variable and it will create in object where self pointing to the object.


         self.a = 4 is an instance variable, which means it belongs to the object created from the class. The self keyword refers to the current object  t1 = Test() , so this line creates a variable a inside that object and assigns it the value 4.



   t1 = Test() 
   t2 = Test()

    1. it is mandatory to take at least one (or more) positional argument in __init__() method.

    2. You can givve any name to the dirst arguemnt of __init__() methos but self is 
    recommended.

"""
#Note:
"""

 t1 = Test() // empty at begining 

 actual t1 refer to this object () and when this instance object is called then __init__(t1) automatically called and t1 pass as an arguemnt automatically and t1 hold the id of test () object and will pass in self. and self will refer to test obj () due to same id and both refer to same instance object. object has no new copy just is passed. 

2nd instance object:

t2 = Test() // empty at begining 

 and now here slef refer to this object and now in this object will new value hold 
 which is a = 4.

 self work a like this keyword. 

"""


# Job if ___init__()

"""
   jsut because you are definig __init__() method, you can write any code in it, 

   but 

      1. you should write code in __init__() which you want to run immediately 
      after object creation.

      2. idealy you should initalize instance object variables.

"""


# Prividing Arguemnts to __init__() method 

"""
   class Test:

      def ___init___(self,a b): # formal arguments and local variables 

 instace object variable <-- self.a = a --> local varaibl
  
instace object variable <-- self.b = b -->  local varaible 

  t1 = Test()  # automatically called __init__(t1) wrong(error) during __init__() call by default one argument is necessary as instace object.

  t1 = Test(3,4) #  automatically called __init__(t1,3,4) 3,4 will be gone in a,b and in instance object the value store a = 3 and b = 4 in one object. 



   t2 = Test(6,8) will refer to new object as instance object variables

"""


   