#q1
print("Another 6 months of work")
#q2
#2.1
a=5
b=7
print(a+b)
#2.2
s1="My name"
s2=" is Nikhil Sharma"
join=s1+s2
print(join)
#2.3
s="the number is "
n= 42
result=s+str(n)
print(result)
#q3
#3.1
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
#3.2
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
#q4
#4.1
for number in range(1, 11):
    print(number)
#4.2
number = 1
while number <= 10:
    print(number)
    number += 1
#4.3
total_sum = 0
for number in range(1, 101):
    total_sum += number
    print(f"The sum of numbers from 1 to 100 is {total_sum}")
#q5
#5.1
numbers = [12, 45, 7, 89, 23]
largest = max(numbers)
smallest = min(numbers)
print(f"The largest number in the list is {largest}")
print(f"The smallest number in the list is {smallest}")
#5.2
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
key_to_lookup = "age"
if key_to_lookup in my_dict:
    value = my_dict[key_to_lookup]
    print(f"The value for the key '{key_to_lookup}' is: {value}")
else:
    print(f"The key '{key_to_lookup}' does not exist in the dictionary.")
#5.3
numbers = [12, 45, 7, 89, 23, 56]
numbers.sort()
print(f"List in ascending order: {numbers}")
numbers.sort(reverse=True)
print(f"List in descending order: {numbers}")
#5.4
dict1 = {1: 'One', 2: 'Two', 3: 'Three'}
dict2 = {4: 'Four', 5: 'Five', 6: 'Six'}
dict1.update(dict2)
print(dict1)

#q6
#6.1
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in string if char in vowels)
    return count
input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)

print("Number of vowels:", vowel_count)
#6.2
input_string = input("Enter a string: ")
reversed_string = input_string[::-1]
print("Reversed string:", reversed_string)
#6.3
input_string = input("Enter a string: ")
if input_string == input_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
#q7
#7.1
file=open("file.txt","w")

file.write("Cognitive Computing\n")
print("Data written")
file.close()

file=open("file.txt","r")
print(file.read())
file.close()
#7.2
file=open("file.txt","a")
file.write("Semester IV\n")
file.close()

file=open("file.txt","r")
print(file.read())
file.close()
#7.3
file=open("file.txt","r")
print('Number of lines:',len(file.readlines()))
file.close()
#q8
#8.1
a=int(input('Enter a number:'))
b=int(input('Enter a number:'))

try:
    result=a/b
    print('Result:',result)
except:
    print('Zero divison error')
#8.2
try:
    num=int(input('Enter a number:'))
    print('Valid')
except:
    print('You didnt enter a number')
#8.3
try:
    num=int(input('Enter a number to divide 20:'))
    res=20/num
except:
    print('Zero divison error')
else:
    print('Result:',res)
finally:
    print('Completed')
#q9
#9.1
import random
print('Five random numbers')
for i in range(5):
    print(random.randint(1,100))
#9.2
print('\n')
num=random.randint(1,100)
flag=True
for i in range(2,int(num/2) +1):
    if(num%i==0):
        flag=False
        break
if(flag==True):
    print(num,' is prime')
else:
    print(num,' is not prime')
#9.3
print('\n')
choice=int(input('Enter 1 to roll a die:'))
if(choice==1):
    print('You got ',random.randint(1,6))
#9.4
print('\n')
l=[1,2,3,4,5]
random.shuffle(l)
print('Shuffled: ',l)
#9.5
print('\n')
num=random.choice(l)
print('Number randomly chosen: ',num)
#9.6
print('\n')
list_of_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"
length=int(input('Enter the length of password:'))
password=""
for i in range(length):
    password=password+random.choice(list_of_chars)
print("Your password is: ",password)
#9.7
print('\n\n')
cards=["Diamonds","Spades","Hearts","Clubs"]
ranks=[2,3,4,5,6,7,8,9,0,"Jack","Queen","King","Ace"]
card=random.choice(cards)
rank=random.choice(ranks)
print(rank," of ",card)
#q10
#10.1
import sys
n=len(sys.argv)
print("Total parameters in argv:",n)
sum_=0
for i in range(1,n):
    sum_=sum_+int(sys.argv[i])

print('The sum is:',sum_)
#10.2
import sys
length=len(sys.argv[1])
print("Length of ",sys.argv[1]," is: ",length)
#q11
#11.1
import math
from datetime import datetime
print(math.cos(0))
print(math.cos(math.pi))
print(math.fabs(-3))
a=int(input('Enter a number:'))
b=math.pow(a,1/2)
print('Square root of ',a,' is:',b)
#11.2
print('\n')
now=datetime.now()
date=now.strftime("%d/%m/%Y")
time=now.strftime("%H:%M:%S")
print("Current Date:",date)
print("Current time:",time)
#11.3
print('\n')
import os
print('List of files:',os.listdir())





