# Agenda 

"""
   types of functions in class

   Tpyes of methods in the class

   1. instance method
   2. static method(no static keyword in python)
   3. class method
  


"""
#  instance method (run for an object):

"""
   class A:
     
      def f1(self): # by default self arguemnt is necessary in instace method
         self.a=5
       
      def f2(self,x,y):
          self.b=x
          self.c=y


   obj1 = A() # A class object an initialy empty object but when we access varaibles/attributes through self then the object store these a = 5 

   obj2 = A() 

   ob2.f1() run for an obj2 # f1(obj2) and atore value a = 5

   ob1.f1() # impicity 1 argument pass f1(obj1) same as __init_() and store value a = 5 now b  = 5, c= 6

   obj1.f2(5,6) # f2(obj1,5,6)

"""



class A:
     
      def f1(self): # by default self arguemnt is necessary in instace method
         self.a=10
       
      def f2(self,x,y):
          self.b=x
          self.c=y


obj1 = A() 
obj2 = A() 

obj2.f1()
obj1.f1() 

obj1.f2(5,6) 

print(obj1.a, obj2.a)

print( obj1.b, obj1.c)



# is any class object (A) call a instace method f1()

""" 
A.f1()  # error not anything implicity pass

A.f1(6) # also an error

A.f1(obj) # we need to pass an obj as an arguemnt
"""

class A:
    def f1(self):
        self.a=5 # will create instance variable

obj1=A()
A.f1(obj1) #This line is equal to obj1.f1().
#It means the method is called by passing the object manually.

# print(obj1.a) will print 5 because the method f1() set the value of a to 5.


# print(obj1.a) # to print value

# This is just another way to call instance methods by passing the object directly to the class method.
#  This method works the same as obj1.f1() but is rarely used in practice.



# Static Method: (not work for instace object work for class object)


# not ideal for instace object 
# not anything implicity not passed in static method.
#here through class obj calling the method


"""
   class A:

     @staticmethod # no space 
     def f1(): #for instance method one arguemnt is necessary 
     
     print("Hello")
    
      @staticmethod
      def f2(a,b):
        print(a,b)
A.f1()
A.f2(5,6) # not anything implicity jsut value passed as actual arguemnt into a,b

obj1=A()
obj1.f1()

"""


class A:

     @staticmethod # no space 
     def f1(): #for instance method one arguemnt is necessary 
     
      print("Hello")
    
     @staticmethod
     def f2(a,b):
      print(a,b)

# A.f1()
# A.f2(10,6) # not anything implicity jsut value passed as actual arguemnt into a,b
# through class obj calling the method

obj1=A()
obj1.f1() 
obj1.f2(88,90) # no implicity pass anything

print("======================")


# class method:

# minimum one arguement is necessary for class method like instance method
# not work for instace obj
# it will work for class obj 
# @classmethod required 


"""
@classmethod
calss A:
   def f1(cls):
     cls.x=10 # 


A.f1() # f1(A) implicity class obj pass 
obj1=A()
obj1.f1() 


"""
class B:
 @classmethod
 def f1(cls):
     cls.x=10 # 


B.f1() # f1(B) implicity class obj pass 

print(B.x)

obj1=B()

obj1.f1() # implicity pass class object / may be instace obj ? find 

print(obj1.x) # 10 will print 

print(obj1.__dict__)

print(B.__dict__) # it has been created in calss object with the key value pair 


# Instace method not any decorator required 

"""
can call through both


classObect. (not implicitly instace obj pass)

instaceObject. (implicitly instace obj pass)

"""



# static method any decorator required 

"""
can call but not implicitly passed anything in both cases

classObect. 
instaceObject. 


"""
# class method any decorator required 

"""
can call but implicitly class obj pass in both cases

classObect. 
instaceObject. 


"""