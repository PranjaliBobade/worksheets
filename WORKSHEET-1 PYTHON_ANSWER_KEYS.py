#!/usr/bin/env python
# coding: utf-8

# Q1) Ans - C

# Q2) Ans - B

# Q3) Ans - C

# Q4) Ans - A

# Q5) Ans - D

# Q6) Ans - B

# Q7) Ans - A

# Q8) Ans - C

# Q9) Ans - A , C

# Q10) Ans - A , B


# Q11) Write a python program to find the factorial of a number

num = int(input("Enter a number: "))  
factorial = 1  
if num < 0:  
    print("The factorial does not exist for negative numbers")
    
elif num == 0:  
    print("The factorial of 0 is 1")
    
else:  
    for i in range(1,num + 1):  
        factorial = factorial*i  
    print("The factorial of",num,"is",factorial)  


# Q12) Write a python program to find whether a number is prime or composite

# Prime numbers:-A prime number is a natural number greater than 1 and having no positive divisor other than 1 and itself,e.g. 3, 7, 11 etc.
# Composite number:-Other natural numbers that are not prime numbers are called composite numbers , e.g. 4, 6, 9 etc.   

num = int(input("Enter a number: "))  
  
if num > 1:  
    for i in range(2,num):  
        if (num % i) == 0:  
            print(num,"It is a composite number")  
            print(i,"times",num//i,"is",num)  
            break  
    else:  
        print(num,"is a prime number")  
         
else:  
    print(num,"It is a composite number")  



num = int(input("Enter a number: "))  
  
if num > 1:  
    for i in range(2,num):  
        if (num % i) == 0:  
            print(num,"It is a composite number")  
            print(i,"times",num//i,"is",num)  
            break  
    else:  
        print(num,"is a prime number")  
         
else:  
    print(num,"It is a composite number")  


# Q13) Write a python program to check whether a given string is palindrome or not

# function which return reverse of a string called as palindrome
 
def isPalindrome(s):
    return s == s[::-1]

s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")


# Q14) Write a Python program to get the third side of right-angled triangle from two given sides.


def rightAngleTriangle(opposite_side,adjacent_side,hypotenuse):
        if opposite_side == str("x"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
        elif adjacent_side == str("x"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
        elif hypotenuse == str("x"):
            return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
        else:
            return "we know the answers!"
    
print(pythagoras(3,4,'x'))


# Q15) Write a python program to print the frequency of each of the characters present in a given string.

# collections.Counter() 
from collections import Counter 
  
# initializing string  
my_str = "PythonIsVeryInteresting"

# using collections.Counter() to get count of each element in string  
frq = Counter(my_str)
  
# printing result  
print ("Count of all characters in GeeksforGeeks is :\n "
                                           +  str(frq)) 

