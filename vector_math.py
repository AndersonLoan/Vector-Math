# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anderson Wayne Loan 
# Section: 574
# Assignment: 7-2
# Date: 1 10 22
#

from math import *

a = input("Enter the elements for vector A:\n")#takes in first vector
a = a.split()
vectA = []
vectB = []
for i in range(len(a)):
    vectA.append(float(a[i]))#covnerts vector to a flaot points
add = []
sub =[]
dot = 0
mA = 0
mB = 0
b = input("Enter the elements for vector B:\n")#takes in 2nd vector
b = b.split()
for i in range(len(b)):
    vectB.append(float(b[i]))#converts vector to float points
for i in range(len(vectA)):
    mA += vectA[i]**2
mA = sqrt(mA)
print(f"The magnitude of vector A is {mA:.5f}")
for i in range(len(vectB)):
    mB += vectB[i]**2
mB = sqrt(mB)
print(f"The magnitude of vector B is {mB:.5f}")
for i in range(len(vectA)):#adds onto a new list, each iteration being point A and B added
    add.append(vectA[i] + vectB[i])
print(f"A + B is {add}")
for i in range(len(vectA)):#adds onto a new list, each iteration being point A-B
    sub.append(vectA[i] - vectB[i])
print(f"A - B is {sub}")
for i in range(len(vectA)):#
    dot +=vectA[i] * vectB[i]
print(f"The dot product is {dot:.2f}")
