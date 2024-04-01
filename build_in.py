# 1-abs(x) 
# 1.Using abs() with Integers:
num = -7
absolute_num = abs(num)
print(f"Absolute value of {num} is {absolute_num}")

# Absolute value of -7 is 7

# 2.Using abs() with Complex Numbers:
complex_num = 3 + 4j
magnitude = abs(complex_num)
print(f"Magnitude of {complex_num} is {magnitude}")

# Magnitude of (3+4j) is 5.0

# 2- all(iterable) like list,tuple,dictionary,set -->boolean retuns

# All elements of list are true
l = [4, 5, 1]
print(all(l))

# All elements of list are false
l = [0, 0, False]
print(all(l))

# Some elements of list are
# true while others are false
l = [1, 0, 6, 7, False]
print(all(l))

# Empty List
l = []
print(all(l))

# all() with condition - to check if all elements are greater than 0
l = [1,-3,0,2,4]
print(all(ele > 0 for ele in l))

# Output
# True
# False
# False
# True
# False

# 3.any(iterable) Returns True if any of the items is True.

# All elements of list are True
l = [4, 5, 1]
print(any(l))

# All elements of list are False
l = [0, 0, False]
print(any(l))

# Some elements of list are
# True while others are False
# l = [1, 0, 6, 7, False]
# print(any(l))

# Empty list
l = []
print(any(l))

# Output:
# True
# False
# False

# 4.ascii()->Returns a string as a printable representation of the object passed, escaping the non-ASCII characters.
# Python program to illustrate ascii()
test_str = "G ë ê k s f ? r G ? e k s"
print(ascii(test_str))

# Output
# 'G \xeb \xea k s f ? r G ? e k s'

# 5.bin()->Convert Integer to Binary String
# Python code to demonstrate working of
# bin()

# declare variable
num = 100

# print binary number
print(bin(num))

# output: 0b1100100

# bool() --> is used to return or convert a value to a Boolean value
x = bool(1)
print(x)
y = bool()
print(y)

# Output
# True
# False

# Python code to check whether a number
# is even or odd using bool()

def check(num):
	return(bool(num % 2 == 0))

# Driver Code
num = 8
if(check(num)):
	print("Even")
else:
	print("Odd")

# Output: 
# Even
	
# 6.bytes()-->converts an object to an immutable byte-represented object of a given size and data.
# python code demonstrating 
# int to bytes
str = "Welcome to Geeksforgeeks"

arr = bytes(str, 'utf-8')

print(arr)

# Output:
# b'Welcome to Geeksforgeeks'	

# python code to demonstrate
# int to bytes

number = 12
result = bytes(number)

print(result)
# Output:
# b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# 7.chr()--> returns a string representing a character whose Unicode code point is the integer specified.  
num = 97
print("ASCII Value of 97 is: ", chr(num))

# output: ASCII Value of 97 is:  a

# 8: callable--> if function exist in call given True
def my_function():
    print("Hello from my_function!")

print(callable(my_function))  # Output: True


num = 10
print(callable(num))  # Output: False

# 9:classmethod()
class Cookie:
    @classmethod
    def default_flavor(cls):
        print("Chocolate Chip")

# Call the class method directly (no need for an instance)
Cookie.default_flavor()

# 10.complex()
# 11.