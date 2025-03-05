# AGENDA

"""
  1. Procedure Oriented Programming
  2. Pbject Oriented Programming
  3. Mian aspects of OOP
  4. Encapsulation 
  5. calss
  6. object 
"""

# Procedure Oriented Porgramming 

"""
   All the programs we have created so for are around functions, that is block of statements which manipulates data.

   This is called procedure oriented way of programming.

"""
 #book record managment 
def inputbook():
    print("Enter bookid")
    bookid=int(input())
    title=input("Enter book title ")
    price= float(input("Enter book price"))
    mybook=(bookid,title,price)

    return mybook
def main():
    bookid= 1
    title= "Pyhton made easy"
    price= 400.4
    author= "Abc"

#more functions related to this taks

"""
1. searchBook ()
2. updateBookPrice()

"""

# Object Oriented Programming

"""

   There is another way of oraganiizng your program, which is to combone data and functionality and wrap it inside something called an object.

   This is called Object Oriented way of Programming.

   This appraoch is more suitable to large programs.

"""


# Main Aspects of OOP (key modules)

"""
  1. Encapsulation 
  2. Inheritance 
  3. Polymorphism
  4. Abstraction (but python is not strict for abstraction)
"""
# Encapsulation 

"""
  An act of combining properties and methods elated to the same entity is called encapsulation.

"""

# book (entity)
# properties 
"""1.book title
   2.book id
   3.book price
   4.book author
   5.book ediiton
"""

# Methods
"""
   1. inputBook() 
   2. SearchBook() it is a task to access the properties of book.
   2. DisplayBook() 
   4. updateBookPrice()
"""

# object is a real world programming

"""
   1. Common Noun (calss)

   2. Proper Noun (object)

   
# Class (variables and functions)
   
   "in calss we have properties and methods"
    
    and we call them atributes(sort, append)
 
   1. class is a keyword
   2. class name start with capital letter
   3. calss encapsulates data and functions
   4. creating calss is crating a new data type
   5. class is a description of an object.
   6. class is a blue print of abject.

      l1 = [10,20,30]
      l1.append(100)
      l1.sort()
      l1..... 

      All these fun are made in list class and list class  is an description of l1 ,so what to do l1 using? 

"""

# Note:
"""
 int, float, complex, bool,list,range, tuple, set, dict, str, etc are classes.

  x = 5 
  x is an int type object
"""


#Object

"""
   1. object is an instance (example) of a class.
   2. object is a real world entity 
   3. instance = object = instance object (same)
   4. You can create any number of objects of a class.

   x = 5
   y = 4
   z = 7
 x,y,z refer to three differnt objects of int calss.
 thier type will be an object.

"""




#Banking system software

"""
Employee
Class: Employee
Properties: name, salary
Methods: validateData(), checkRecord()
Objects: Sara (an instance of class) (Employee with salary $5000 who can validate data and check records)

Customer
Class: Customer
Properties: name, balance
Methods: payBill(), withdrawBalance()
Objects: Ahmed (Customer with balance of $1000 who can pay bills or withdraw balance)


More Examples:

Human
Properties: name, gender, age
Objects: Ali, Sara (both are instances of the Human class)

Car
Class: Car
Properties: model, speed, color, price
Objects: Honda Civic, Toyota Corolla
General Objects


Class: Mobile, Chair, Pen, Computer
Properties: color, size, weight, price
Objects: Samsung mobile, Office chair, Ballpoint pen

"""

