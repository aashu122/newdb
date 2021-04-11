# Variable
#Variable is a name which is used to used to define (represent)
#any type of object like string ,integer,float etc..
"""var = 1234
var1 = 234
var3 = 356
var_ = 256
_var = 256
__var = 2563
var_var = 353"""
"""
#keywords
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
# type specifier
"""
"""
%d ---> integer
%f ---> float
%s ---> string
"""

"""a = 235
b = 23.02
sum = a+b
print(a+b)
print("Value of a is %d" %a)
print("Value of b is %f" %b)
print("The sum of %d and %f is %f"%(a,b,a+b))"""
#format
"""a = 15
b = 20
#print("Value of a is {} and b is {}".format(b,a))
print("Value of {x} and b is {y}".format(x=a,y=b))
print(a)"""
# Method to take string input from the user

"""strg = input("Enter a your name:")
print(strg)
print(type(strg))"""
"""
strg = float(input("Enter a number: "))
print(strg)
print(type(strg))
"""
"""
strg = eval(input("Enter any data type:"))
print(strg)
print(type(strg))"""

# Operators
"""
operators are symbolic representation of operations
#Exaple
a = 12
b = 20
a+b
a and b are operands
+ is operator
Type of operators
1. Arithmetic operator
2. Assignment operator
3. Comparision operator
4. Logical
5. Membership Operator
6. Indentity
7. bitwise
8 ternary



1. Arithmetic Operator
+ , -, *, /, //(floor division), % (remaider), ** (power)
print(23+4)
print(23-4)
print(23*4)
print(23/4)
print(25//4)
print(25%4)
print(25**4)
"""
#2. Assignment operators
# =, +=, -=, *=, /=, //=, %=, **=

"""a = 10
print(a)
#a += 2 # a = a + 2
print(a)
a -= 2
print(a)
a *= 2 # a = a * 2
print(a)

"""

# 3. Comparision Operator
# ==, >, <, <=, >=,!=
b = 21
c = 3

#print(2==2)
# print(a == b == c)
"""print(b<c)
print(b<=c)
print(b>=c)
print(b!=c)
"""
# 4. Logical Operator
# operands for these operator should be boolean

# and ,or, not
# and
"""T and T = T%d
T and F = F
F and T = F
F and F = F
# or
T or  T = T
T or  F = T
F or  T = T%d
F or F = F
# not
not T = Fi
not F = T
"""
#print(2 == 2 and 3 >)
# memebership operator
#a = 2
#print(not 2 == 3)
#print("a" in "raman")
# Identity operators
"""
a = 10
b = 20
b = 3
print(b)
#print(id(a))
list1 = [1,2,3]
list2 = [3,5,4]
print(id(list1))%d
"""
# &, |, ^ ,<<,>>, ~
"""
a = -25
b = 26
print(a, bin(a))
print(b , bin(b))
print(a&b , bin(a&b))
print(a|b,bin(a|b))
print(a<<b,bin(a<<b))
print(a>>b,bin(a>>b))%d
"""
# area of triangle
"""a = float(input("Enter the left side length: "))
b = float(input("Enter the right side length:"))
c = float(input("Enter the other side length: "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))*0.5
print("Area of Triangle is",area)"""


# control Statement
# if , else, elif
if( condition):
    block 
