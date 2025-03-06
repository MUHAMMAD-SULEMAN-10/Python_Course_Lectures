#AGENDA

# Inheritence

"""
  The main concept of OOP os encapsulation, which is achived by class.

  The intent of OOP is incomplete without the concept of Inheritence.

  ==>Inheritence is another key concept of OOP.

  ==>Reuse of code is majro aspect of OOP, and can be achived through
  Inheritence.

"""
# What is Inheritence ?

"""
  Definig a new class by extending the features of an existing class is called Inheritence.

"""

#differnt houses (one class )
#differnt trees
#differt cars , roads and peoples in park in real world and we saw entities

#common noun(tree, person, car, ) (classes)

#proper noun(t1,t2,t3,t4,  Ali  , usman, Ayesha, c1,c2,c3..)(objects)



"""
everthing is a object
but nature is differnt of every entity 
you can easily identify object

"""
"""
suppose we have a person class 

person (name , age)

now we want to make a class student.

1. Definig Student from the scract is rework and increase the cost of development.
2. In real world every student is a person.
3. person is already defined, we can reuse it to define student.
4.by adding attributes like roll no we can make a person student.

==> you may think of adding new attributes to the person class but this will loose identity of a person.

==> The best to do modification in Person to make it student without disturbing
person calss, is inhertence.

"""

#How to extend a class?
"""
class Person: # base class, super class, paent class
    #atribute

class Student(person): #drived class, subclass. child class

    #newatributes
    
"""

# Example:

class Person:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def showName(self):
        print(self.name)
    def showAge(self):
        print(self.age)



p1=Person("Suleman",24)

p1.showName()
p1.showAge()



print(" Person and student class start ==============")  
# student class extend Person class

class Person:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def showName(self):
        print(self.name)
    def showAge(self):
        print(self.age)

class Student(Person):
     def setRollno(self,r):
       self.rollno=r
     def showRollno(self):
      print("student class roll no:",self.rollno)

s1 = Student("Usman",44) #___init__(s1) as an argument implicitly and you can not pass roll no because in person context nothing is roll no

s1.setRollno(55)
s1.showName()
s1.showAge()
s1.showRollno()

#and it is executing person class init but he has not found any init in in Student class also it has only one init ___init__(s1) 
#need arguments for n,a in s1 = Student() 


# lets define ___init__method in Student class 

print("define init method in student class==============")

# class Person:
#     def __init__(self,n,a):
#         self.name = n
#         self.age = a
#     def showName(self):
#         print(self.name)
#     def showAge(self):
#         print(self.age)

class Student(Person):
# lets define ___init__method in Student class 
    #  def __init__(self,r):
    #      self.rollno=r
    #  def setRollno(self,r):
    #    self.rollno=r
    #  def showRollno(self):
    #   print("student class roll no:",self.rollno)

 #___init__(s1) as an argument implicitly and you can not pass roll no because in person context nothing is roll no.




# s1=Student(66)
# #___init__(s1,66) jsut these passed no person class __init__run 

# s1.showRollno()
# s1.showName()
# s1.showAge()
# s1.showAge()


#when instace obj call instace method then implicitly instace pass 

#print("student class init mehtod can call person class init method but How???")
#through class name 


#Person.__init__(self,"ALI KHAN",444) #it will hardcoded

#instace object call through class objectprint



 print("printstudent class init mehtod can call person class init method but How??")

class Person:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def showName(self):
        print(self.name)
    def showAge(self):
        print(self.age)

class Student(Person):
# lets define ___init__method in Student class 
     def __init__(self,r): 
        
         Person.__init__(self,"Ali",44) #instace object call through class object
         self.rollno=r
     
     def setRollno(self,r):
       self.rollno=r
     
     def showRollno(self):
      print("student class roll no:",self.rollno)

 #___init__(s1) as an argument implicitly and you can not pass roll no because in person context nothing is roll no.


s1=Student(66 )
#___init__(s1,66) jsut these passed no person class __init__run 
s1.showRollno()
s1.showName()
s1.showAge()



print("remove the hardcoded values from Person.__init__(self,n,a)")

class Person:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def showName(self):
        print(self.name)
    def showAge(self):
        print(self.age)

class Student(Person):
# lets define ___init__method in Student class 
     def __init__(self,n,a,r): 
        
         Person.__init__(self,n,a) #instace object call through class object
         self.rollno=r
     
     def setRollno(self,r):
       self.rollno=r
     
     def showRollno(self):
      print("student class roll no:",self.rollno)

 #___init__(s1) as an argument implicitly and you can not pass roll no because in person context nothing is roll no.



s1=Student("Usama",44,888 )
#___init__(s1,66) jsut these passed no person class __init__run 
s1.showRollno()
s1.showName()
s1.showAge()


#2nd method using SUPER FUNCTION that represent parent class instace object 

class Person:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def showName(self):
        print(self.name)
    def showAge(self):
        print(self.age)

class Student(Person):
# lets define ___init__method in Student class 
     def __init__(self,n,a,r): 
        
         #Person.__init__(self,n,a) #instace object call through class object

         super().__init__(n,a) #no self need to pass
         self.rollno=r
     
     def setRollno(self,r):
       self.rollno=r
     
     def showRollno(self):
      print("student class roll no:",self.rollno)

 #___init__(s1) as an argument implicitly and you can not pass roll no because in person context nothing is roll no.




s1=Student("Usama",44,888 )
#___init__(s1,66) jsut these passed no person class __init__run 
s1.showRollno()
s1.showName()
s1.showAge()


""""
when an attribute is accessed via derived class objct, if attribute is not found in desired calss, the dearch proceeds to look in the base class.

"""


#Types of Inheritence 

"""
1. Single inheritence

class A:
   code...
   

class B(A):

  code...


  
2. Multilevel inheritence

  class A:
  
  class B(A)

  class C(B)

  
3.Multiple inheritence

  class A1:
  
  class A2:
  
  classB(A1, A2):
  calss b obj access both classes properties/memebers



4.Hierachical INheritence

class A:

class B1(A):

class B2(A)


in which parent class is same


5.Hybrid Inheritence 

class A:

calss B1(A):

class B2(A)

class C(B1,B2)
"""


