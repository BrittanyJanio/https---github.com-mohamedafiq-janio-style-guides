Python Style Reference for Janio Asia 

Introduction
=============
This document gives coding conventions for the Python code comprising the standard library in the main Python distribution. 
This document will be used as a reference for Janio backend developers. Your python code style must be based on this document. 
The python version we used is python3 series. 


Code Lay-out
=============
-Indentation 
Indentation is 2 spaces
Indentation style for multiple parameters in one function just according to the example. The multiple parameters generally means the number of parameters is greater than or equal to 3:  
for example
def long_function_name(
	    var_one,var_two,var_three,
	    var_four):
	pass 

Indentation style for long ‘if’ statement just according to the example:
for example
if (this_is_one_thing and 
	that_is_another_thing):
	do_something

Indentation style for long lines in list/set/tuple(the long lines here means the multidimensional data):
for example
my_list = [1,2,3,
           4,5,6]

         
-Maximum Line Length
Maximum line length is 120 characters 

-A Line Break Before or After a Binary Operator 
for example
income = (gross_wages
	    + taxable_interest
	    + (dividends - qualified_dividends)
	    - iro_deduction
	    - student_loan_interest)
           
-Blank Lines
Blank line for surround top-level function and class definitions is Two Lines
for example
class Student(object):
	pass


class Teacher(object):
	pass

def function_name(parameters):
	pass


def function_name_2(parameters):
	pass


Blank line for method definitions inside a class are surrounded is One Line 
for example
class Student(object):

	def __init__(self,name,score):
		self.name = name
		self.score = score

	def print_score(self):
		print(self.name)


class Teacher(object):
	pass
-Imports 
Import as two separate lines 
for example
import os
import sys

The import order should be as:
Standard library imports, related third party imports, local apps/librarys 

Import multiple class from single lib:
for example
from django.db.models import Model, Q, F

Use relative import if same package 
for example
from .models import Something         


-String Quotes 
The string quotes should be single quote


-Whitespace in Expressions and Statements 
Assignment value 
for example
x = 1
y = 2
long_variable = 3  

Index and slice 
for example
dct['key'] = lst[index] 

Invoke function with parameters 
for example
spam(1)          

Comma in slice 
for example
ham[1:9], ham[1:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fin(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]
           
Before comma,semicolon or colon 
for example
if x == 4: print x, y; x, y = y,x 
           
After square brackets,parathess 
for example
spam(ham[1], {eggs: 2})
 

-Naming Conventions 
Class name conventions：CapitalizedWords 

Function name conventions: lower_case_with_underscores 

Variable name conventions: lower_case_with_underscores

Global variable name conventions: UPPER_CASE_WITH_UNDERSCORES

Method name conventions:  lower_case_with_underscores

Instance variable name conventions: lower_case_with_underscores

Constants name conventions: UPPER_CASE_WITH_UNDERSCORES


-Comments 
Inline comment: 2 spaces after statement, and start with ‘#’ and a single space 

For example: x = 10  # comment


Other Rules 
=============
Queryset and objects should end with _queryset and _obj respectively. Such as order_queryset and order_obj. list and set should be order_list, and order_set.
