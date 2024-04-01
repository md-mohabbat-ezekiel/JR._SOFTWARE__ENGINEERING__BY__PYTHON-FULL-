# module two types: a. user_define module  b.build in Module 

# a.user_define
# hello.py
def greet(name=""):
    print(f"Hello! Nice to meet you, {name}")

# main.py
# import hello  # Import the user-defined module

# hello.greet("Jonathan")  # Call the function from the module



# some build_in_module:

#1. math module
import math
print(math.sqrt(16)) #4
print(math.factorial(5)) #120
print(math.cos(math.pi)) #-1.0

# 2.datetime module

# Get current date and time
import datetime
current_datetime=datetime.datetime.now()
print(current_datetime)
# Output: 2024-03-19 12:34:56.789012

# Create a specific date
specific_date = datetime.datetime(2023, 5, 17)
print(specific_date)  # Output: 2023-05-17 00:00:00

# format  a date
formatted_date=current_datetime.strftime("%Y-%m-%d")
# Output: 2024-03-19

# 3. random module
# Generate a random integer between 1 and 100
import random
random_number=random.randint(1,100)
print(random_number)

# shuffle a list
my_list=[1,2,3,4,5,6,7,8,9,10]
random.shuffle(my_list)
print(my_list)

# 4.os module
# used “os” module to fetch the directory path using os.getcwd() method and then print the path
import os
directory=os.getcwd()
print(directory)
# C:\Phitron\MY_SELF

# 5.json module
# convert the Python dictionary into JSON format using “json.dumps()” method of “json” module in Python and finally print the JSON data.
import json  
data = {
    "name": "Jonny",
    "age": 30,
    "is_student": True,
    "courses": ["Web Dev", "CP"]
}
json_string = json.dumps(data, indent=4)
print(json_string)  

# Output
# {
#     "name": "Jonny",
#     "age": 30,
#     "is_student": true,
#     "courses": [
#         "Web Dev",
#         "CP"
#     ]
# }


# 6.Tkinter module
# “tkinter” is the standard GUI (Graphical User Interface) library in Python. “tkinter” module is used to create windows, buttons, text boxes, and other UI elements for desktop applications.

import tkinter as tk 
def on_button_click(): 
	label.config(text="Hello, Geeks!")

root = tk.Tk()
root.title("Tkinter Example") 
label = tk.Label(root, text="Click the button below") 
label.pack(pady=40) 
button = tk.Button(root, text="Click Me", command=on_button_click) 
button.pack(pady=40) 
root.mainloop() 

# 7. sys module 
# access to some variables and functions related to the Python interpreter.
import sys
print("Python version:", sys.version)
# Python version: 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)]
print("Command line arguments:", sys.argv)
# Command line arguments: ['C:/Phitron/MY_SELF/python/module.py']
sys.exit(1)

# 8.calender module
import calendar
cal_october = calendar.month(2023, 10)
print(cal_october)
#     October 2023
# Mo Tu We Th Fr Sa Su
#                    1
#  2  3  4  5  6  7  8
#  9 10 11 12 13 14 15
# 16 17 18 19 20 21 22
# 23 24 25 26 27 28 29
# 30 31

# from websites
# In this chapter we shall discuss some of the frequently used functions from certain built-in modules.

# os module
# random module
# math module
# time module
# sys module
# collections module
# statistics module
# os module
# This module has functions to perform many tasks of operating system.

# mkdir():
# We can create a new directory using mkdir() function from os module.

# >>> import os
# >>> os.mkdir("d:\\tempdir")
# A new directory corresponding to path in string argument in the function will be created. If we open D drive in Windows explorer we should notice tempdir folder created.

# chdir():
# To change current working directory to use chdir() function.

# >>> import os
# >>> os.chdir("d:\\temp")
# getcwd():
# This function in returns name off current working directory.

# >>> os.getcwd()
# 'd:\\temp'
# Directory paths can also be relative. If current directory is set to D drive and then to temp without mentioning preceding path, then also current working directory will be changed to d:\temp

# >>> os.chdir("d:\\")
# >>> os.getcwd()
# 'd:\\'
# >>> os.chdir("temp")
# >>> os.getcwd()
# 'd:\\temp'
# In order to set current directory to parent directory use ".." as the argument to chdir() function.

# >>> os.chdir("d:\\temp")
# >>> os.getcwd()
# 'd:\\temp'
# >>> os.chdir("..")
# >>> os.getcwd()
# 'd:\\'
# rmdir():
# The rmdir() function in os module removes a specified directory either with absolute or relative path. However it should not be the current working directory and it should be empty.

# >>> os.chdir("tempdir")
# >>> os.getcwd()
# 'd:\\tempdir'
# >>> os.rmdir("d:\\temp")
# PermissionError: [WinError 32] The process cannot access the file because it is being used by another process: 'd:\\temp'
# >>> os.chdir("..")
# >>> os.rmdir("temp")
# listdir():
# The os module has listdir() function which returns list of all files in specified directory.

# >>> os.listdir("c:\\Users")
# ['acer', 'All Users', 'Default', 'Default User', 'desktop.ini', 'Public']
# random module
# Python’s standard library contains random module which defines various functions for handling randomization. Python uses a pseudo-random generator based upon Mersenne Twister algorithm that produces 53-bit precision floats. Functions in this module depend on pseudo-random number generator function random() which generates a random float number between 0.0 and 1.0.

# random.random(): Returns a random float number between 0.0 to 1.0. The function doesn’t need any arguments

# >>> import random
# >>> random.random()
# 0.755173688207591
# Other functions in random module are described here:

# random.randint(): Returns a random integer between the specified integers

# >>> import random
# >>> random.randint(1,100)
# 58
# >>> random.randint(1,100)
# 91
# random.randrange(): Returns a random element from the range created by start, stop and step arguments. The start , stop and step parameters behave similar to range() function.

# >>> random.randrange(1,10)
# 2
# >>> random.randrange(1,10,2)
# 3
# >>> random.randrange(0,101,10)
# 40
# random.choice(): Returns a randomly selected element from a sequence object such as string, list or tuple. An empty sequence as argument raises IndexError

# >>> import random
# >>> random.choice('computer')
# 'o'
# >>> random.choice([12,23,45,67,65,43])
# 65
# >>> random.choice((12,23,45,67,65,43))
# 23
# random.shuffle(): This functions randomly reorders elements in a list.

# >>> numbers=[12,23,45,67,65,43]
# >>> random.shuffle(numbers)
# >>> numbers
# [23, 12, 43, 65, 67, 45]
# >>> random.shuffle(numbers)
# >>> numbers
# [23, 43, 65, 45, 12, 67]
# math module
# This module presents commonly required mathematical functions.

# trigonometric functions
# representation functions
# logarithmic functions
# angle conversion functions
# In addition, two mathematical constants are also defined in this module.

# Pie π which is defined as ratio of circumference to diameter of a circle and its value is 3.141592653589793, is available in math module.

# >>> import math
# >>> math.pi
# 3.141592653589793
# Another mathematical constant in this module is e. It is called Euler’s number and is a base of natural logarithm. Its value is 2.718281828459045

# >>> math.e
# 2.718281828459045
# This module contains functions for calculating various trigonometric ratios for a given angle. The functions (sin, cos, tan etc.) need angle in radians as argument. We on the other hand are used to express angle in degrees. The math module presents two angle conversion functions (degrees() and radians()) to convert angle in degrees to radians and vice versa.

# Trigonometric functions:
# radians(): converts angle in degrees to radians.(Note: π radians is equivalent to 180 degrees)

# >>> math.radians(30)
# 0.5235987755982988
# degrees(): converts angle in radians to degree.

# >>> math.degrees(math.pi/6)
# 29.999999999999996
# Following statements show sin, cos and tan ratios for angle of 30 degrees (0.5235987755982988 radians)

# >> math.sin(0.5235987755982988)
# 0.49999999999999994
# >>> math.cos(0.5235987755982988)
# 0.8660254037844387
# >>> math.tan(0.5235987755982988)
# 0.5773502691896257
# sin(30)	0.5	 0.49999999999999994
# cos(30)	3/2  	 0.8660254037844387)
# tan(30)	1/2	 0. 5773502691896257
# math.log(): returns natural logarithm of given number. Natural logarithm is calculated to the base e.

# math.log10(): returns base-10 logarithm or standard logarithm of given number.

# >>> math.log10(10)
# 1.0
# math.exp(): returns a float number after raising e (math.e) to given number. exp(x) is equivalent to e**x

# >>> math.log10(10)
# 1.0
# >>> math.e**10
# 22026.465794806703
# math.pow(): This function receives two float arguments, raises first to second and returns the result. pow(4,4) is equivalent to 4**4

# >>> math.pow(4,4)
# 256.0
# >>> 4**4
# 256
# math.sqrt(): This function computes square root of given number 

# >>> math.sqrt(100)
# 10.0
# >>> math.sqrt(3)
# 1.7320508075688772
# Representation functions:
# The ceil() function approximates given number to smallest integer greater than or equal to given floating point number. The floor() function returns a largest integer less than or equal to given number

# >>> math.ceil(4.5867)
# 5
# >>> math.floor(4.5687)
# 4
# sys module
# This module provides functions and variables used to manipulate different parts of the Python runtime environment.

# sys.argv
# This return list of command line arguments passed to a Python script.  Item at 0th index of this list is always the name of the script. Rest of the arguments are stored at subsequent indices.

# Here is a Python script (test.py) consuming two arguments from command line.

# import sys
# print ("My name is {}. I am {} years old".format(sys.argv[1], sys.argv[2]))
# This script is executed from command line as follows:

# C:\python37>python tmp.py Anil 23
# My name is Anil. I am 23 years old
# sys.exit
# This causes program to end and return to either Python console or command prompt. It is used to safely exit from program in case of exception.

# sys.maxsize
# It returns the largest integer a variable can take.

# >>> import sys
# >>> sys.maxsize
# 9223372036854775807
# sys.path
# This is an environment variable that returns search path for all Python modules.

# >>> sys.path
# ['', 'C:\\python37\\Lib\\idlelib', 'C:\\python37\\python36.zip', 'C:\\python37\\DLLs', 'C:\\python37\\lib', 'C:\\python37', 'C:\\Users\\acer\\AppData\\Roaming\\Python\\Python37\\site-packages', 'C:\\python37\\lib\\site-packages']
# sys.stdin, sys.stdout, sys.stderr
# These are file objects used by the interpreter for standard input, output and errors. stdin is used for all interactive input (Python shell). stdout is used for the output of print() and of input(). The interpreter’s prompts and error messages go to stderr.

# sys.version
# This attribute displays a string containing version number of current Python interpreter.

# collections module
# This module provides alternatives to built-in container data types such as list, tuple and dict.

# namedtuple() function
# This function is a factory function that returns object of  a tuple subclass with named fields. Any valid Python identifier may be used for a field name except for names starting with an underscore.

# collections.namedtuple(typename, field-list)
# The typename parameter is the subclass of tuple. Its object has attributes mentioned in field list. These field attributes can be accessed by lookup as well as by its index.

# Following statement declares a employee namedtuple having name, age and salary as fields

# >>> import collections
# >>> employee=collections.namedtuple('employee', [name, age, salary])
# To create a new object of this namedtuple
# >>> e1=employee("Ravi", 251, 20000)
# Values of the field can be accessible by attribute lookup

# >>> e1.name
# 'Ravi'
# Or by index

# >>> e1[0]
# 'Ravi'
# OrderedDict() function
# Ordered dictionary is similar to a normal dictionary. However, normal dictionary the order of insertion of keys in it whereas ordered dictionary object remembers the same. The key-value pairs in normal dictionary object appear in arbitrary order.

# >>> d1={}
# >>> d1['A']=20
# >>> d1['B']=30
# >>> d1['C']=40
# >>> d1['D']=50
# We then traverse the dictionary by a for loop,

# >>> for k,v in d1.items():
# print (k,v)

# A 20
# B 30
# D 50
# C 40
# But in case of OrderedDict object:

# >>> import collections
# >>> d2=collections.OrderedDict()
# >>> d2['A']=20
# >>> d2['B']=30
# >>> d2['C']=40
# >>> d2['D']=50
# Key-value pairs will appear in the order of their insertion.

# >>> for k,v in d2.items():
# print (k,v)
# A 20
# B 30
# C 40
# D 50
# deque() function
# A deque object supports append and pop operation from both ends of a list. It is more memory efficient than a normal list object because in a normal list, removing one of iem causes all items to its right to be shifted towards left. Hence it is very slow.

# >>> q=collections.deque([10,20,30,40])
# >>> q.appendleft(110)
# >>> q
# deque([110, 10, 20, 30, 40])
# >>> q.append(41)
# >>> q
# deque([0, 10, 20, 30, 40, 41])
# >>> q.pop()
# 40
# >>> q
# deque([0, 10, 20, 30, 40])
# >>> q.popleft()
# 110
# >>> q
# deque([10, 20, 30, 40])
# statistics module
# This module provides following statistical functions :

# mean() : calculate arithmetic mean of numbers in a list

# >>> import statistics
# >>> statistics.mean([2,5,6,9])
# 5.5
# median() : returns middle value of numeric data in a list. For odd items in list, it returns value at (n+1)/2 position. For even values, average of values at n/2 and (n/2)+1 positions is returned.

# >>> import statistics
# >>> statistics.median([1,2,3,8,9])
# 3
# >>> statistics.median([1,2,3,7,8,9])
# 5.0
# mode(): returns most repeated data point in the list.

# >>> import statistics
# >>> statistics.mode([2,5,3,2,8,3,9,4,2,5,6])
# 2
# stdev() : calculates standard deviation on given sample in the form of list.

# >>> import statistics
# >>> statistics.stdev([1,1.5,2,2.5,3,3.5,4,4.5,5])
# 1.3693063937629153
# time module
# This module has many time related functions.

# time():

# This function returns current system time in ticks. The ticks is number of seconds elapsed after epoch time i.e. 12.00 am, January 1, 1970.

# >>> time.time()
# 1544348359.1183174
# localtime():

# This function translates time in ticks in a time tuple notation.

# >>> tk=time.time()
# >>> time.localtime(tk)
# time.struct_time(tm_year=2018, tm_mon=12, tm_mday=9, tm_hour=15, tm_min=11, tm_sec=25, tm_wday=6, tm_yday=343, tm_isdst=0)
# asctime():
# This functions returns a readable format of local time

# >>> tk=time.time()
# >>> tp=time.localtime(tk)
# >>> time.asctime(tp)
# 'Sun Dec  9 15:11:25 2018'
# ctime():
# This function returns string representation of system's current time

# >>> time.ctime()
# 'Sun Dec  9 15:17:40 2018'
# sleep():
# This function halts current program execution for a specified duration in seconds.

# >>> time.ctime()
# 'Sun Dec  9 15:19:14 2018'
# >>> time.sleep(20)
# >>> time.ctime()
# 'Sun Dec  9 15:19:34 2018'