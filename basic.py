# 1.data type,input,output
# 2.condition lop,nested loop,for,while,do,if,else if,else
# 3.array
# 4.string
# 5.function,pointer 
# 6.2D array,recurtion
# 7.min,max,swap,sort,reverse,delete,push,pop,remove,insert,remove



# Deta types

#1: numerical Deta types

#type checking
# integer
a=5
print(type(a))

# float
b=5.5
print(type(b))

# complex 
c=2+4j
print(type(c))


# type conversion

d=int(5.5)
print(d)

e=float(5)
print(e)

f=complex(2,3)
print(f)


# 2.sequence Type:

# a. string
# immutable(unchangable):any selected position word doesn't change by another value

g="hello"
# a[0]="g"
print(g) 
# given result error for immutable
# But tangible working
for ch in g:
    print(ch)

for ch in g:
    print(ch,end=" ")
    # Hell    

# capitalize
h="phitron"    
print(h.capitalize())
# Hello
print(h.upper()) 
# HELLO
print(h.lower())
# hello

# find
text="Hello,world"
src="world"
index=text.find(src)

if index !=-1:
    print(f"The result '{src}' was found at index '{index}' ")
else:
    print("Not found")


# count
print(text.count('o'))    
# 2



# modules
from collections import Counter as ctr
print(ctr(text))
# count all single words uniquely


# replace with limitation
txt = "one one was a race horse, two two was one too."
new_txt = txt.replace("one", "three", 2)
print(new_txt)  # Output: "three three was a race horse, two two was one too."


# b.List:(mutable and iterable)
# like array but not needed to same type [int,float,complex,string]

# converting a list
i="gabriel"
print(list(i))
# ['g', 'a', 'b', 'r', 'i', 'e', 'l']  

# print list
j=["abed"]
print(j)
# ["abed"]

#print list value using point means address's value
print(*j)
# abed  

# iterable
print(j[0])
# abed

k=['a', 'b', 'r', 'i']
print(*k)

# print list in list
l=[['a','b'],['c']]
print(l)
# [['a', 'b'], ['c']]

print(l[0][1])
# b

# nested loops
for prs in l:
    for val in prs:
        print(val)
#a
#b
#c

# append //push
m=[]
m.append(5)
m.append('a')
print(m)
# [5, 'a']

print("before clear ",m)
# [5, 'a']

# clear //pop
print(m.clear())
# None
print("after clear ",m)

n=['a','b','c']
o=n.copy()
print(o)

# count
message = 'python is a popular programming language'
p_count = message.count('p')
print(f"Number of occurrences of 'p': {p_count}")

# insert
my_list=[1,2,3,4,5]
my_list.insert(2,10) 
print(my_list)

# pop
my_list=[1,2,3,4,5]
my_list.pop()
print(my_list)
# position
deleted_value=my_list.pop(2)
print(deleted_value)
# sort
my_list.sort()
print(my_list)
my_list.reverse()
my_list[: : -1]
print(my_list)

# 2.c tuple(immutable) (first Bracket)
# not modified like retsult 
myList=(1,2,3,4) 


# 3.d Set {unordered,unindexed,but iterable,mutable,no duplicate elements}
st1=set("phitronic")
print(st1)
# {'h', 'n', 'o', 'p', 't', 'r', 'c', 'i'}
st2=set([1,2,3,4,5])
print(st2)
# {1, 2, 3, 4, 5}

st3={1,2,3,4,5}
st3.add(7)
print(st3)
# {1, 2, 3, 4, 5, 7}
# clear
# copy
# pop position
# remove value
# update


# 2.e. dictionary
dic={}
dic1={1:'name',2:'roll',3:'class'}
dic1.clear()  
# keys
dic3={1:'name',2:'roll',3:'class'}
key=dic3.keys()
val=dic3.values()
itm=dic3.items()
print(key)
# dict_keys([1, 2, 3])
print(val)
#dict_values(['name', 'roll', 'class'])
print(itm)
# dict_items([(1, 'name'), (2, 'roll'), (3, 'class')])


# text and red as a .txt in a file 
with open('message.txt','a') as file:
    file.write('I love you,python!')

with open('message.txt','r') as file:
   text=file.red()
   print(text) 


# *args (Non-Keyword Arguments):
# The *args syntax allows a function to accept a variable number of non-keyworded arguments.
# When you use *args in a function definition, it collects all the positional arguments passed to the function into a tuple
# You can then iterate over this tuple or perform other operations on it.  

def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3, "hello")

# 1
# 2
# 3
# hello
 

# **kwargs (Keyword Arguments):
# The **kwargs syntax allows a function to accept a variable number of keyword arguments (i.e., named arguments).
# When you use **kwargs in a function definition, it collects all the keyword arguments passed to the function into a dictionary.

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=30, city="Wonderland")
# name: Alice
# age: 30
# city: Wonderland

#lamda
# def doubled(x):
#     return x*2
# lamda input:operation
doubled=lambda num:num*2
add=lambda x,y:x+y
sum=add(11,33)
result=doubled(44)
print(result)
print(sum)

add=lambda a,b: a/b
print(add(4,5))

# map operaton ,number 
numbers=[12,56,98,78,12,6,98]
doubled_nums=map(doubled,numbers)
double_num=map(lambda x:x*2,numbers)
print(numbers)
print(list(doubled_nums))

num=[1,2,3,4]
addd=map(lambda a: a*2,num)

# actors=[
#         {'name':'nabana','age':5}
#         {'name':'kabana','age':15}
#         {'name':'rabana','age':45}
#         {'name':'pabana','age':65}
#        ]

# juniors=filter(lambda actor: actor['age']<40,actors)
# print(list(juniors))

# j=filter(lambda actor:actor['age']<50,actors )
# print(list(j))


#set mutable but unodered index
numbers=[12,56,98,78,12,6,98]
numbers.add(55)
print(numbers)
 
numbers.remove(6)
print(numbers)

A={1,3,5,7}
B={1,2,3,4,5}
print(A&B) #common
print(A|B) #AUB all number

# list odered and changeable means mutable -->list=[],list1=list(1,2,3) for transform
# tuple odered but unchangeable means immutable --> tuple=(),tuple1=tuple([1,2]) for transform
# set unodered but changeable means mutable --> set={1,2}, set1=set(1,2) for transform
# dictionary odered but changeable means mutable--> dic={"keys":"values"}

# filter()
# An iterable (such as a list, tuple, or set) containing the elements to be filtered.
ages = [5, 12, 17, 18, 24, 32]
def is_adult(age):
    return age >= 18
# filter(operation,ages)
adults = filter(is_adult, ages)
print(list(adults))  # Convert the iterator to a list
# [18, 24, 32]
# Lambda Function with filter():
# We can also use a lambda function for filtering:
# Python

adults = filter(lambda age: age >= 18, ages)
print(list(adults))
                

# input 2 integer with between spcace each other
case = [int(i) for i in input().split(" ")]

k = case[0]
s = case[1]
# Input:
# The user provides input in the form of two integers separated by a space.
# The first integer (k) represents the maximum value for each of the three variables (x, y, and z).
# The second integer (s) represents the sum of x, y, and z.

cnt = 0
for x in range(k + 1):
    for y in range(k + 1):
        z = s - x - y
        if(0 <= z and z <= k):
            cnt += 1

# condition if,elif,else
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")



#loop
#for 
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# while 
count = 0
while count < 5:
    print(count)
    count += 1

#range
for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)


#function()
x = 10

def my_function():
    x = 5
    print(x)  # Prints 5

my_function()
print(x)  # Prints 10


# 2D array or list :element = arr[row][col]
rows, cols = 5, 5
arr = [[0] * cols for _ in range(rows)]
print(arr)

# [[0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0]]




#pythonic 
#list ,tuple,set,dictionary,string

# list--->[ ] -->mutable
# tuple--->() -->immutable
# string ---> immutable

#tuple ---> immutable
a=(1,3,5,[2,4,5],{1:23,3:56})
# innner list ->mutable 
a[3][0]=100
print(a)
# (1, 3, 5, [100, 4, 5], {1: 23, 3: 56})
# but tuple ->immutable
# a[3]=100
# error


# print the value of key "histroy" from the below dict
sampleDict={
    "class":{
        "student":{
            "name":"Mike",
            "marks":{
                "physices":70,
                "history":80
            }                                      
        }  
    } 
}
print(sampleDict["class"]["student"]["marks"]["history"])
#80 o(n)

# len("string")
# len([1,2,3])

a=10
b=10
print(id(a))
print(id(b))
# id means address value same so address same
# 140721703871560
# 140721703871560

# a=input() # string formate a data nibe
# a=int(input()) # integer formate nibe
# a=float(input()) # float formate nibe

#one line e multiple input
#multiple line r multiple input

# lst=[]
#1
# for i in range(0,a):
#     x=int(input())
#     lst.append(x)
# print(lst)
# [1,2,3]

# split=string to list
# join=list to string 
# lst=map(func,datastructure)#input hote value gula integer e convert korbe
# lst=list(map(int,input().split()))
# print(lst)
# # 1 2 3 =[1, 2, 3]

lst1=[1,2,3,4]
for i in range(0,len(lst1)):
    lst1[i] = lst1[i]*lst1[i]
print(lst1)    

# another way
def sq(i):
    return i*i
result=map(sq,lst1)
print(list(result))

# another way
result=map(lambda i:i*i,lst1)
print(list(result))
# map not given human readable so list or tuple needed

# list() --> ds+function
# lst=[ ] --> list data structure
# s=list("hello") --> string to list  conversion  function
s="h e l l o"
print(list(s))
print(s.split(' '))

# problem solve reverse 
# 4
# 121 
# 39
# 123456
# 1200
# range(end) -->0,end-1
# range(start,end) --> start,end-1--> 1 step forward
# range(start,end,step)--> start,end-1, 1 step forward

t=int(input())
for i in range(0,t):
    a=list(input())
    a.reverse()
    result=' '.join(a)
    print(result)

# another way to
    # result=""
    #   for i in a:
    #     result += i + ""
    #   print(result)  
    
# 1 2 1
# 9 3
# 6 5 4 3 2 1
# 0 0 2 1

# join--> list to string convert
lst3=[1,2,3,4] # 1 2 3 4
lst4=['h','i','l'] #h-i-l

res="-".join(lst4)
print(res)
# h-i-l

# lst3 er element gula join korbo
# 1. lst4 te jodi int value thakle map die shegula string e convert kore nebo
# 2. er por join function chalabo

lst=list(map(lambda i:str(i),lst3))
print(lst)
# ['1','2','3','4']

# sum of consecutive odd numbers
# sum of odd number between given two numbers
# 3
# 5 6
# 10 4
# 4 9

# 0
# 21
# 12

t=int(input())
for i in range(t):
    x,y=input().split()
    x=int(x)
    y=int(y)
    #  1 swap
    if x>y:
        y,x=x,y 
    res=0
    for i in range(x+1,y):
        if i % 2 != 0:
            res+=i
    print(res)

# interesting swap
    # a=13
    # b=20
    # a,b=b,a


#  f.Equation problem solving
# 5 5

# 650

x,y =input().split()
x=int(x)
y=int(y)
sum=0

# 5^0++5^2+5^4--> 5^Y-1
for i in range(0,y,2):
    sum+=x**(i)
sum-=1
print(sum)    











     






