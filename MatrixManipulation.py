import csv
import numpy
from numpy import genfromtxt 
print "----------------------------------------"
print "This program uses the concept of CSV file modification and matrix from numpy\n"
print "Various module used in the program are numpy and CSV\n"
print "----------------------------------------"
f=open("Test.csv","r")
reader=csv.reader(f,delimiter=',')
x=list(reader)
print "Value of entire CSV file in matrix form "
print "----------------------------------------"
result=numpy.array(x).astype('int')
print result
print "----------------------------------------"
print "Dimension of the matrix: \n"
print result.shape
print "----------------------------------------"
print "First column value:  \n"

data = genfromtxt('Test.csv',delimiter=",")

print data[:,0]

print "----------------------------------------"
print "First column value after adding 1 to it: \n"
print data[:,0]+1
print "----------------------------------------"

print "First column multiplication with 2: \n"
print data[:,0]*2
print "----------------------------------------"
print "Sum of first two column: \n"
print data[:,1]+data[:,0]
print "----------------------------------------"
print "First column after skipping the value of first row:  \n"

data1 = genfromtxt('Test.csv',delimiter=",",skiprows=1)
print "----------------------------------------"
print data1[:,1]
print "----------------------------------------"
print "Now you will see some random function that can be used in numpy"
print "----------------------------------------"
print "Arrange function: "
a= numpy.arange(10)
print a