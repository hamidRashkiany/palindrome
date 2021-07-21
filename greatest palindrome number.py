#!/usr/bin/env python
# coding: utf-8

def palindrom(n):
    temp=n
    rev=0
    flag=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
        if(temp==rev):
            ##print("The number is a palindrome!")
            flag=True
        else:
            ##print("The number isn't a palindrome!")
            flag=False
    return flag


def find_max(n):
    max=[]
    for i in range(len(n)-1):
        if n[i]>n[i+1]:
            max=n[i]
        else:
            max=n[i+1]
    return max
        
        
result=[]
pal=[]
num1=[]
num2=[]
flag=0
for i in range(100,1000):
    for j in range(100,1000):
        result=i*j
        flag=palindrom(result)
        if flag==True:
            pal.append(result)
            num1.append(i)
            num2.append(j)


max_num1=find_max(num1)
max_num2=find_max(num2)
max_pal=find_max(pal)
print("The first three digit number is:",max_num1)
print("The second three digit number is:",max_num2)
print("The maximum palindrom number which \n obtain from the multiplication of three digit numer is:",max_pal)








