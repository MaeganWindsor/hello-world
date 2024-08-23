# CSCI1010: Lab 1, Problem 1
# Filename: hw1pr2.py
# Name: 
# Problem description: Solving the quadratic equation!

from math import *

a = input("Supply a value for a: ")
a = float(a)
print("The value stored by the variable a is",a)
b = input("Supply a value for b: ")
b = float(b)
print("The value stored by the variable b is",b)
c = input("Supply a value for c: ")
c = float(c)
print("The value stored by the variable c is",c)
X = (-b+sqrt(b*b-(4*a*c)))/(2*a)
Y = (-b-sqrt(b*b-(4*a*c)))/(2*a)
print("The solutions for x are ",X," and ", Y)