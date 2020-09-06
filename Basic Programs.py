# Add two numbers
#def add(a,b):
#    sum=a+b
#    return(sum)


#x=int(input("Enter your first choice: "))
#y=int(input("Enter your second choice: "))
#print("The sum of two numbers is: ",add(x,y))

#Print all prime numbers in an interval
#def prime(num):
#    c=0
#    for i in range (1,num+1):
#        if num%i==0:
#            c=c+1
#    return(c)

#n=int(input("Enter a range: "))
#print("The prime numbers are:")
#for i in range(1,n+1):
#    if prime(i)==2:
#        print(i,end=" ")

#Check a number is prime or not

#def prime(num):
#    c=0
#    for i in range (1,num+1):
#        if num%i==0:
#            c=c+1
#    return(c)

#x=int(input("Enter your choice: "))
#if prime(x)==2:
#    print("The number is a prime number")
#else:
#    print("The number is not a prime number")

#Area of a circle
#import math
#def area(c):
#    i=math.pi
#    a=i*(c*c)
#    return(a)

#r=int(input("Enter the radious of the circle: "))
#print("Area of the circle is: ",area(r))

# Simple interest

#def simple_interest(a,b,c):
#    si=(a*b*c)/100
#    return(si)

#p=int(input("Enter the Principal: "))
#r=int(input("Enter the rate of interest: "))
#t=int(input("Enter the time period: "))
#print("The simple interest is: ",simple_interest(p,r,t))

# Compound interest

def compound_interest(principal,rate,time):
    result=principal*(pow((1+rate/100),time))
    return(result)

p=float(input("Enter the principal amount: "))
r=float(input("Enter the interest rate: "))
t=float(input("Enter the time in years: "))
amount=compound_interest(p,r,t)
interest=amount-p
print("Compound amount: %.3f"%amount)
print("Compound interest: %.3f"%interest)
      
