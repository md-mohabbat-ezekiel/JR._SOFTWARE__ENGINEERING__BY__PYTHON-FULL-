# 1.array
# 2.linked list(singly,doubly,circuler)
# 3.stack(lifo)
# 4.queue(fifo),priority
# 5.hashtable(dictionary)
# 6.tree(bst)
# 7.graph(direct,undirect,edge,value)
# প্রথমেই যে ৭ ধরণের ডাটা স্ট্রাকচার তোমাকে শিখতেই হবে: 
# ১) Arrays এর ইনডেক্স আর length জানতে হবে। Array এর মধ্যে ডাটা কিভাবে Access, insert, delete, এবং update করবে। Array এর উপাদানগুলাকে কিভাবে লুপ করবে। sort, reverse করবে। কোন উপাদানকে খুঁজে বের করবে। array কপি করবে, merge করবে, কেটে ছোট (slice) করবে। ডিফারেন্ট টাইপের ডাটা এর জন্য কিভাবে array ডিক্লেয়ার করবে। এবং কিছু কমন কাজ যেমন, সবচেয়ে ছোট বা সবচেয়ে বড় উপাদান খুঁজে বের করা। আর আরো বেশি জানতে চাইলে two dimensional array সম্পর্কে জানবে। ইত্যাদি। 
# Indexing,Length,Insert, Delete,Update,removing value,pop value by index or last,For two-dimensional arrays
# looping through elements,looping with indeces,sorting and reversing , Finding Elements and Slicing.
# ২) Linked Lists এর কনসেপ্ট টা বুঝতে হবে। বিশেষ করে Singly Linked List, Doubly Linked List এবং Circular Linked List এর কনসেপ্টগুলো জানতে হবে। লিংকডলিস্ট কিভাবে ইমপ্লিমেন্ট করে সেটা জানতে হবে। তারপর Linked List এর মধ্যে কোন একটা নিদৃষ্ট উপাদান আছে কিনা খুঁজে বের করা। নতুন উপাদান যোগ করা, ডিলিট করা, আপডেট করার সিস্টেম বুঝতে হবে। এইটুক হলেও মোটামুটি চলবে। আর যদি আরেকটু বেশি শিখতে চাও তাহলে লিংকডইন রিভার্স করা, মার্জ করা, সাইকেল ডিটেক্ট করা, k-th উপাদান বের করা, শর্ট করার বিষয়গুলো দেখতে পারো। 
# search element,delete,update,reverse,marge,cycle detect,sort,kth
# ৩+৪) Stack এবং Queue:
# LIFO আর FIFO প্রিন্সিপালগুলো বুঝতে হবে। Array দিয়ে কিভাবে স্ট্যাক বানাতে হয় এবং স্ট্যাক এর মধ্যে Push, pop, peek, Size (or Count) বের করা শিখতে হবে। একইভাবে Array দিয়ে কিভাবে কিউ বানাতে হয় এবং কিউ এর মধ্যে Enqueue, dequeue, peek, Size (or Count) কিভাবে করতে হয়। সেটা জানতে হবে। আরেকটু বেশি শিখতে চাইলে-- Linked  List দিয়ে কিভাবে স্ট্যাক এবং কিউ ইমপ্লিমেন্ট করতে হয়। সেটা দেখতে পারো। আরেকটা স্পেশাল কিউ আছে Priority Queue নামে সেটা সম্পর্কে কিছু ধারণা থাকলে অবশ্যই ভালো। 
# .
# ৫)Hash Tables বা Hash Map বা Dictionary: 
# Hash functions বা Hashing জিনিসটা বুঝতে হবে। key-value স্টাইলে ডাটা কখন, কেন এবং কিভাবে স্টোর করতে হয়। রাখার সুবিধা কি জানতে হবে।  তারপর insertion, retrieval, deletion জানার পরে Key-Value ওয়ালা জিনিস লুপ করে কিভাবে একটার পর একটা দেখাবে। কোন  key আছে কিনা। বা কোন ভ্যালু আছে কিনা সেটা কিভাবে চেক করবে। আরো বেশি জানতে চাইলে hashing করার সময় Collision ডিটেক্ট করার সিস্টেম এবং Collision resolve techniques জানলে অনেক ভালো। 
# .
# ৬) Tree: 
# Basic Tree কনসেপ্ট সম্পর্কে জানতে হবে। একটা ট্রি ডাটা স্ট্রাকচার বা Binary Tree, Binary Search Tree (BST), Heap ডাটা স্ট্রাকচার কিভাবে কোড করতে হয় সেটা জানতে হবে। ট্রি এর মধ্যে নোড কিভাবে ইনসার্ট করতে হয়, ডিলিট কোনো হয়, সার্চ করতে হয়। জন্য Breadth-First Search (BFS) আর Depth-First Search (DFS) সম্পর্কে জানতে হবে। আরেকটু ধারণা নিতে চাইলে In-Order Traversal, Pre-Order Traversal, Post-Order Traversal দেখতে পারো।  আর দেখতে চাইলে Balanced Binary Search Tree (যেমন AVL Tree বা Red-Black Tree দেখতে পারো)
# insert, delete, search in Binary Tree, Binary Search Tree (BST),Heap .BFS,DFS for In-Order Traversal, Pre-Order Traversal,Post-Order Traversal  implementaion by python data structure
# ৭) Graphs: non linear 
# গ্রাফ কনসেপ্ট nodes, edges এবং vertices সম্পর্কে জানতে হবে। বিশেষ করে directed, undirected, weighted গ্রাফ আইডিয়াগুলা কি। কিভাবে গ্রাফ এর কোড লিখতে হয়। কিভাবে গ্রাফ traversal এর জন্য (DFS, BFS) কিভাবে ইউজ করা যায়। কম করে এইটুক জানলেও বিগিনার হিসেবে চলবে। তবে আরেকটু জানতে চাইলে Cyclic আর Acyclic গ্রাফ নিয়ে ধারণা নিতে পারো। 


# 1. used of array data structure

# Indexing and Length:
my_array=[1,2,3,4,5]
print("length:",len(my_array)) #5
# accessing elements
print("First element:",my_array[0]) #1
print("First element:",my_array[-1]) #5
#  Insert, Delete, and Update:
# inserting
my_array.append(6)
print("After Insertion:", my_array)  # Output: [1, 2, 3, 4, 5, 6]
# deleting
del my_array[2] #values of index 
print("After Deletion:", my_array)  # Output: [1, 2, 4, 5, 6]
# Updating
my_array[2]=7
print("After Update:", my_array)  # Output: [1, 2, 7, 5, 6]
# removing value 
my_array.remove(2)
print("After removing:", my_array)  # Output: [1, 7, 5, 6]
# pop value by index or last
my_array.pop()
print("After poping:", my_array)  # Output: [1, 7, 5, 6]
# looping through elements
for item in my_array:
    print (item)
# 1
# 2
# 7
# 5
# 6
#looping with indeces
for i in range(len(my_array)):
    print("index",i,"value",my_array[i])  
# index 0 value 1
# index 1 value 2
# index 2 value 7
# index 3 value 5
# index 4 value 6      

# sorting and reversing 
#sorting
print(my_array.sort())     #[1, 2, 5, 6, 7]
print(my_array.reverse())     #[1, 2, 5, 6, 7]

# Finding Elements and Slicing:
# finding value by index
index = my_array.index(5)
print("Index of 5:", index)  # Output: 2
# slicing value list by indexing
sub_array=my_array[1:4]
print("Sliced Array:", sub_array)  # Output: [6, 5, 2]


# In Python, arrays are typically implemented using lists. Although Python has a built-in array module, lists are more commonly used due to their flexibility and built-in methods. Let's go through each of the operations you mentioned with examples:

# Indexing and Length:
my_array = [1, 2, 3, 4, 5]
length = len(my_array)
print("Length:", length)  # Output: 5

# Accessing elements
print("First element:", my_array[0])  # Output: 1
print("Last element:", my_array[-1])  # Output: 5
# Access, Insert, Delete, and Update:
# Accessing
print("Access:", my_array[2])  # Output: 3

# Inserting
my_array.append(6)
print("After Insertion:", my_array)  # Output: [1, 2, 3, 4, 5, 6]

# Deleting
del my_array[2]
print("After Deletion:", my_array)  # Output: [1, 2, 4, 5, 6]

# Updating
my_array[2] = 7
print("After Update:", my_array)  # Output: [1, 2, 7, 5, 6]

# Looping:
# Looping through elements
for item in my_array:
    print(item)

# Looping with indices
for i in range(len(my_array)):
    print("Index:", i, "Value:", my_array[i])

# for i in range(0, len(my_array)):
#     print(my_array[i])
# 1
# 2
# 7
# 5
# 6
for i in range(0, len(my_array)):
    print(my_array[i],end=" ")
print("\n")    
# 1 2 7 5 6


# Sorting and Reversing:
# Sorting
my_array.sort()
print("Sorted Array:", my_array)  # Output: [1, 2, 5, 6, 7]

# Reversing
my_array.reverse()
print("Reversed Array:", my_array)  # Output: [7, 6, 5, 2, 1]

# Finding Elements and Slicing:
# Finding element
index = my_array.index(5)
print("Index of 5:", index)  # Output: 2

# Slicing
sub_array = my_array[1:4]
print("Sliced Array:", sub_array)  # Output: [6, 5, 2]

# Different Data Types:
# Array declaration with different data types
mixed_array = [1, 'hello', 3.14, True]
print("Mixed Array:", mixed_array)

# Finding Minimum and Maximum:
min_value = min(my_array)
max_value = max(my_array)
print("Minimum Value:", min_value)
print("Maximum Value:", max_value)

# For two-dimensional arrays, you can use lists of lists:
two_d_array=[[1,2,3],[4,5,6],[7,8,9]]
# accessing elements
print('elements at (0,0):',two_d_array[0][0]) #1
print('elements at (1,2):',two_d_array[1][2]) #6





# 2.linked list(singly,doubly,circuler):
# singly linked list implementation
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
# creating node
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
# connecting node to form a linked listed
node1.next=node2
node2.next=node3
node3.next=node4
# printing the linked List
current=node1
while current is not None:
    print(current.data,end="->")
    current=current.next
print("None")    
         
# singly
# searching an element, deleting, updating, reversing, merging, detecting cycles, sorting, and finding the k-th element:
# Time Complexities:
# Access: O(n)
# Insertion/Deletion at beginning: O(1)
# Insertion/Deletion at end: O(n) - unless tail pointer is maintained
# Search: O(n)

# Time Complexities (Singly Linked List vs. Array):
# Access: O(n) vs. O(1)
# Insertion (at the end): O(1) vs. O(1) amortized
# Deletion (at arbitrary position): O(n) vs. O(n)
# Search: O(n) vs. O(n)

class Node:
    # empty Node
    def __init__(self,data=None):
        self.data=data
        self.next=None #tail null

class singly_linked_list:
    def __init__(self):
        self.head=None #empty singly node

    #add
    def append(self,data):
        if not self.head: #1.conditon not head value 
            self.head=Node(data) #set value 
        else:
            current=self.head #existing head so set it current value
            while current.next:#tail
                current=current.next #new variable memory_location as current
            current.next=Node(data) #new data
    #print
    def display(self):
        current=self.head
        while current:
            print(current.data,end=" ->")# 1 ->
            current=current.next #1 ->2..
        print("None") #not input value so tail None
    #search 
    def search(self,key):
        current=self.head
        index=0
        found=False
        while current:
            if current.data==key:
                print(f"element {key} found at index {index}") #1st node er  heading search so index 0
                found=True
            current=current.next # current hode tail
            index+=1 #index 1 berlo
        if not found:
            print(f" element {key} not found in the list")
    #delete
    def delete(self,key):
        if not self.head: #empty
            print("empty list")
            return
        if self.head.data==key: #head delete so head ignore then go to next
            self.head=self.head.next
            return
        prev=None #so head jodi key word hoi. tahole privious head ignored means none
        current=self.head #second Node 
        while current: #head nie kaj
            if current.data==key:
                prev.next=current.next # tail = next node
                print(f"element {key} deleted")
                return
            prev=current #prev none = current ignore
            current=current.next # ignore current
        
    #update
    def update(self,old,new):
        current=self.head
        while current:
            if current.data==old:
                current.data=new
                print(f"element {old} update to {new}")
                return
            current=current.next
        print(f"elenment {old} not found in the list")

    #reverse 
    def reverse(self):
        prev=None # prev none for head none like tail none
        current=self.head
        while current:
            next_node=current.next #tail variable set another location
            current.next=prev #tail null
            prev=current #swap
            current=next_node #swap
        self.head=prev

    #merge
    def merge(self,other_list):
        current=self.head
        while current.next:
            current=current.next #this current new node define
        current.next=other_list.head

    #detect_cycle
    def detect_cycle(self):
        if not self.head: #head na thakle cycle exist kore na
            return False
        slow=self.head #head
        fast=self.head.next #tail
        while fast and fast.next: #tail and head of new node 
            if slow == fast :
                return True
            slow=slow.next
            fast=fast.next.next
        return False
    
    def sort(self):
        if not self.head: 
            return
        current=self.head
        min_node=current
        nexa_node=current.next
        while nexa_node:
            if nexa_node.data < min_node.data:
                min_node=nexa_node
            nexa_node=nexa_node.next
        current.data, min_node.data = min_node.data, current.data 
        current=current.next

    #get_kth_element
    def get_kth_element(self,k):
        if not self.head:
            print("List is empty")
            return
        slow=self.head #head
        fast=self.head.next #tail
        for _ in range(k):
            if fast is None: #tail none 
                print(f"List does not have {k} elements")
                return
            fast=fast.next
        while fast:
            slow=slow.next
            fast=fast.next
        print(f"The {k}-th element from the end is: {slow.data}")        


sll=singly_linked_list()
sll.append(3)
sll.append(2)        
sll.append(1)        
sll.append(4)        
sll.append(5) 
sll.display() #3 ->2 ->1 ->4 ->5 ->None    

sll.search(4) #element 4 found at index 3

sll.delete(3)
sll.display() #2 ->1 ->4 ->5 ->None

sll.update(1,6)  #element 1 update to 6
sll.display() #2 ->6 ->4 ->5 ->None

sll.reverse()
sll.display() #5 ->4 ->6 ->2 ->None

other_list=singly_linked_list()
other_list.append(7)
sll.merge(other_list)
sll.display() #5 ->4 ->6 ->2 ->7 ->None

print("cycle detected",sll.detect_cycle) #False
sll.sort()
sll.display() #2 ->4 ->6 ->5 ->7 ->None
sll.get_kth_element(2) #The 2-th element from the end is: 6


#doubly linked list 
#searching an element, deleting, updating, reversing, merging, detecting cycles, sorting, and finding the k-th element:
# Time Complexities:
# Access: O(n)
# Insertion/Deletion at beginning: O(1)
# Insertion/Deletion at end: O(1) if tail pointer is maintained, otherwise O(n)
# Search: O(n)

# Time Complexities (Doubly Linked List vs. Array):
# Access: O(n) vs. O(1)
# Insertion (at the end): O(1) vs. O(1)
# Deletion (at arbitrary position): O(n) vs. O(n)
# Search: O(n) vs. O(n)

class Node:
    def __init__(self,data=None):
        self.data = data
        self.prev=None
        self.next=None

class doubly_linked_list:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node #set the next reference of the last node to the new node (current.next = new_node)
            new_node.prev=current 

    def display_forward(self):
        current=self.head
        while current:
            print(current.data,end=" <-> ")
            current=current.next #The loop continues until current becomes None, which means we have reached the end of the list.
        print("None")

    def display_backward(self):
        current=self.head
        while current.next:
            current=current.next #It first traverses the list to find the last node (the tail node) by moving from the head to the end (current.next).
        while current:
            print(current.data,end=" <-> ")
            current=current.prev #Once it reaches the last node, it starts traversing backward from the tail node.
        print("None")        

    def search(self,key):
        current=self.head
        index=0
        found=False
        while current:
            if current.data==key:
                print(f"Element {key} found at index {index}")
                found= True
            current=current.next
            index+=1
        if not found:
            print(f"Element {key} not found in the list")        
    
    def delete(self,key):
        if not self.head:
            print("List is empty") 
            return
        if self.head.data==key: #If the node is found, it updates the references to remove the node.
            if self.head.next:
                self.head.next.prev=None
            self.head=self.head.next
            print("Element {key} deleted")
            return

        current=self.head
        while current:
            if current.data == key:
                if current.next:
                    current.next.prev=current.prev
                if current.prev:
                    current.prev.next=current.next
                print(f'Element {key} deleted')
                return
            current=current.next
        print(f"Element {key} not found in the list")


    def update(self,old,new):
        current=self.head
        while current:
            if current.data == old:
                current.data=new
                print(f"Element {old} updated to {new}")
                return
            current=current.next
        print(f"Element {old} not found in the list")

    def reverse(self):
        current=self.head
        while current:
            current.prev, current.next=current.next, current.prev # swaps the prev and next references of the current node.
            if not current.next:
                self.head=current
            current=current.prev  #it moves to the previous node  
    
    def merge(self,other_list):
        if not self.head:
            self.head=other_list.head
            return
        if not other_list:
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=other_list.head
        other_list.head.prev=current

    def detect_cycle(self):
        slow=self.head #head
        fast=self.head.next #tail
        while fast and fast.next:
            slow=slow.next #1st node head=tail  (1 step)
            fast=fast.next.next #1st tail=2nd tail (2 steps)
            if slow == fast:
                return True
        return False
        
    def sort(self):
        if not self.head or not self.head.next:
            return
        current=self.head
        min_node=current
        next_node=current.next
        while next_node:
            if next_node.data < min_node.data:
                min_node =next_node
            next_node=next_node.next
        current.data,min_node.data=min_node.data,current.data
        current=current.next  

    def get_kth_elememt(self,k):
        if not self.head:
            print("List is empty")
            return
        current=self.head
        for _ in range(k):
            if not current:
                print(f"List dose not have {k} elements")
                return
            current=current.next
        while current.next:
            current=current.next
        print(f"The {k} element  from the end is: {current.data}")

dll=doubly_linked_list() 
dll.append(3)
dll.append(1)
dll.append(4)
dll.append(2) 
print("Forward display:")
dll.display_forward()  # Output: 3 <-> 1 <-> 4 <-> 2 <-> None
print("Backward display:")
dll.display_backward()  # Output: 2 <-> 4 <-> 1 <-> 3 <-> None              

dll.search(4)  # Output: Element 4 found at index 2
dll.search(5)  # Output: Element 5 not found in the list

dll.delete(4)
print("After deleting 4:")
dll.display_forward()  # Output: 3 <-> 1 <-> 2 <-> None

dll.update(1, 5)
print("After updating 1 to 5:")
dll.display_forward()  # Output: 3 <-> 5 <-> 2 <-> None


dll.reverse()
print("After reversing:")
dll.display_forward()  # Output: 2 <-> 5 <-> 3 <-> None

other_list = doubly_linked_list()
other_list.append(7)
other_list.append(6)
dll.merge(other_list)
print("After merging:")
dll.display_forward()  # Output: 2 <-> 5 <-> 3 <-> 7 <-> 6 <-> None


print("Cycle Detected:", dll.detect_cycle())  # Output: False


dll.sort()
print("After sorting:")
dll.display_forward()  # Output: 2 <-> 3 <-> 5 <-> 6 <-> 7 <-> None

dll.get_kth_elememt(2)  # Output: The 2-th element from the end is: 6


#circuler linked list
# searching an element, deleting, updating, reversing, merging, detecting cycles, sorting, and finding the k-th element:
# Time Complexities:
# Access: O(n)
# Insertion/Deletion at beginning: O(1)
# Insertion/Deletion at end: O(1) if tail pointer is maintained, otherwise O(n)
# Search: O(n)

# Time Complexities (Circular Linked List vs. Array):
# Access: O(n) vs. O(1)
# Insertion (at the end): O(1) vs. O(1) amortized
# Deletion (at arbitrary position): O(n) vs. O(n)
# Search: O(n) vs. O(n)

#better array
class Node:
    def __init__(self,data=None):
        self.data=data
        self.prev=None
        self.next=None

class circular_linked_list:
    def __init__(self):
        self.head=None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node  # Circular reference for the first node
            new_node.prev = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head: #data!=head we stop at the last node (where current.next points back to the head).
                current=current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = self.head
            self.head.prev = new_node

    def display_forward(self):
        if not self.head:
            print("List is empty")
            return
        current=self.head
        while True:
            print(current.data,end=" <->")
            current=current.next
            if current == self.head:
                break
            print(self.head.data)

    def display_backward(self):
        if not self.head:
            print("List is empty")
            return
        current=self.head.prev
        while True:
            print(current.data,end=" <->")
            current=current.prev
            if current == self.head.prev:
                break
        print(self.head.prev.data)

    def search(self,key):
        if not self.head:
            print("List is empty")    
            return
        current=self.head
        index=0
        found=False
        while True:
            if current.data==key:
                print(f"Elements {key} found at index {index}")
                found=True
            current=current.next
            index+=1
            if current == self.head:
                break
        if not found:
            print(f"Element {key} not found in the list")

    def delete(self,key):
        if not self.head:
            print("List is empty")
            return
        current=self.head
        while True:
            if current.data==key:
                if current==self.head:
                    if current.next==self.head:
                        self.head=None
                    else:
                        self.head=current.next
                        current.prev.next=current.next
                        current.next.prev=current.prev
                else:
                    current.prev.next=current.next
                    current.next.prev=current.prev
                print(f"ELement {key} deleted")
                return
            current=current.next
            if current==self.head:
                break
            print(f"Element {key} not found in the list")

    def update(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            current.prev, current.next = current.next, current.prev
            current = current.prev
            if current == self.head:
                break
        self.head = self.head.prev

    def reverse(self):
        if not self.head:
            print("List is empty")
            return

        current = self.head
        while True:
            current.prev, current.next = current.next, current.prev
            current = current.prev
            if current == self.head:
                break
        self.head = self.head.prev    

    def merge(self, other_list):
        if not self.head:
            self.head = other_list.head
            return
        if not other_list.head:
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = other_list.head
        other_list.head.prev = current
        other_list_head = other_list.head
        while other_list_head.next != other_list.head:
            other_list_head = other_list_head.next
        other_list_head.next = self.head
        self.head.prev = other_list_head    

    def detect_cycle(self):
        if not self.head:
            print("List is empty")
            return False
        slow = self.head
        fast = self.head.next
        while fast and fast.next:
            if slow == fast or slow == fast.next:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
    
    def sort(self):
        if not self.head or not self.head.next:
            return
        current = self.head
        while current.next != self.head:
            min_node = current
            next_node = current.next
            while next_node != self.head:
                if next_node.data < min_node.data:
                    min_node = next_node
                next_node = next_node.next
            current.data, min_node.data = min_node.data, current.data
            current = current.next

    def get_kth_element(self, k):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        for _ in range(k):
            current = current.next
            if current == self.head:
                print(f"List does not have {k} elements")
                return
        while current.next != self.head:
            current = current.next
        print(f"The {k}-th element from the end is: {current.data}")

cdll = circular_linked_list()
cdll.append(3)
cdll.append(1)
cdll.append(4)
cdll.display_backward()



# Stack (LIFO - Last-In-First-Out):
# The last element added to the stack is the first one to be removed.
# Elements are added and removed from only one end, known as the top of the stack.

# Implementation using Array:
# Operations
# Push: Adds an element to the top of the stack.
# Pop: Removes and returns the element from the top of the stack.
# Peek: Returns the element at the top of the stack without removing it.
# Size (or Count): Returns the number of elements in the stack.
# Input=[1,2,3,4,5] output=[1,2,3,4,5]
# stack implementation by array:
class stack_array:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")        
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty") #element remove na korei lister nicher element dekha ja onno lister top
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size (self):
        return len(self.stack)

    
# Stack Implementation using Linked List:  
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class StackLinkedList:
    def __init__(self):
        self.head=None

    def push(self,data):
        new_node=self.head
        new_node.next=self.head
        self.head=new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        popped_item=self.head.data
        self.head=self.head.next
        return popped_item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.head.data
    
    def is_empty(self):
        return self.head is None
    
    def size(self):
        count=0
        current=self.head
        while current:
            count+=1
            count=count.next
        return count
    


# FIFO (First-In-First-Out): The first element added to the queue is the first one to be removed.
# Elements are added at the rear (end) and removed from the front of the queue.

# Implementation using Array:
# Operations
# Enqueue: Adds an element to the rear of the queue.
# Dequeue: Removes and returns the element from the front of the queue.
# Peek: Returns the element at the front of the queue without removing it.
# Size (or Count): Returns the number of elements in the queue.
# Input=[1,2,3,4,5] output=[5,4,3,2,1]
class QueueArray:
    def __init__(self):
        self.queue=[]

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue) 
    
# Queue Implementation using Linked List:

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty") #When this line of code is executed, it stops the normal flow of the program and immediately jumps to the nearest exception handler (if one exists).
        dequeued_item = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return dequeued_item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.head.data

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


# PriorityQueue like Dijkstra’s 
# Imagine a system where multiple tasks (such as background jobs, threads, or processes) need to be executed.
# Each task has a priority (e.g., high, medium, low).
# The priority queue ensures that tasks with higher priority are executed before those with lower priority.    
    
class PriorityQueueArray:
    def __init__(self):
        self.queue = []

    def enqueue(self,item,priority):
        self.queue.append((item,priority)) #[(item,numeric value)]=touple in list
        self.queue.sort(key=lambda x: x[1]) #sort base on priority numeric value tuple er 1th index

    def peek(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return self.queue[0][0] # like normal er first elment but operation queue er por
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    

# Priority Queue Implementation using Linked List:
class Node:
    def __init__(self, data=None, priority=None):
        self.data = data
        self.priority = priority
        self.next = None

class PriorityQueueLinkedList:
    def __init__(self):
        self.head = None

    def enqueue(self, item, priority):
        new_node = Node(item, priority)
        if not self.head or priority < self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.priority <= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        dequeued_item = self.head.data
        self.head = self.head.next
        return dequeued_item

    def peek(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return self.head.data

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
# priority que data structure in pythonic way
import queue
# creat a priority queue
pq=queue.PriorityQueue()
#insert elements into the priority queue with priority
pq.put((3,'apple'))
pq.put((1,'banana'))
pq.put((4,'orrange'))
pq.put((2,'mango'))# put tuple in list
#get and remove elements from the priority queue
print(pq.get()) # (1,'banana')
print(pq.get()) # (2,'mango')
print(pq.get()) # (3,'apple')
print(pq.get()) # (4,'orrange')
# If you try to get from an empty priority queue, it will block until an item is available
# Use q.get_nowait() to avoid blocking and raise an Empty exception instead
try:
    print(pq.get_nowait()) 
except queue.Empty:
    print("Priority queue is empty") 
# You can also check if the priority queue is empty
print(pq.empty()) # True 
           
# dictionary : insertion, retrieval, deletion,loop,existing key & value,collision detected system,Collision resolve techniques    with example by python data structure
# build in dictionary 
my_dict={}
#insert:
my_dict['apple']=10
my_dict['banana']=20
my_dict['orrange']=30
#retraival:
print(my_dict['apple']) #10
print(my_dict['banana']) #20
#delete:
del my_dict['orrange']
#loop key and value
for key,value in my_dict.items():
    print(key,"->",value)
#cheak if value exists
if 'apple' in my_dict.values():
    print(" key 'apple' exists")
else:
    print(" key 'orrange' does not exist")

# Collision handling
# Python's dictionary handles collisions internally using open addressing with quadratic probing
# It automatically resolves collisions, users do not need to worry about it

#hash table/ dictionary by implementation
class HashTable:
    def __init__(self,size):
        self.size=size
        self.table=[[] for _ in range(size)]#attribute as a list of empty lists (buckets).

    def _hash(self,key): #The _hash method computes the hash value for a given key.
        return hash(key) % self.size
    
    def insert(self,key,value):
        index=self._hash(key) #numeric key
        for pair in self.table[index]: #value of pair
            if pair[0]==key:
                pair[1]=value
                return
        self.table[index].append([key,value])

    def retrieve(self,key):
        index=self._hash(key)
        for pair in self.table[index]: 
            if pair[0]==key:
                return pair[1]
        return None

    def delete(self,key):
        index=self._hash(key)
        for i,pair in enumerate(self.table[index]):
            if pair[0]==key:
                del self.table[index][i]
                return

    def key_exists(self,key):
        index=self._hash(key)
        for pair in self.table[index]:
            if pair[0]==key:
                return True

    def value_exists(self, value):
        for bucket in self.table:
            for pair in bucket:
                if pair[1] == value:
                    return True
        return False 
                   
# Example usage:
hash_table = HashTable(10)
hash_table.insert('apple', 10)
hash_table.insert('banana', 20)
hash_table.insert('orange', 30)

print(hash_table.retrieve('apple'))  # Output: 10
print(hash_table.retrieve('banana'))  # Output: 20

hash_table.delete('banana')
print(hash_table.retrieve('banana'))  # Output: None

print(hash_table.key_exists('orange'))  # Output: True
print(hash_table.key_exists('banana'))  # Output: False

print(hash_table.value_exists(30))  # Output: True
print(hash_table.value_exists(20))  # Output: False




class TreeNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None

    def insert(self,key):
        if not self.root: #node null so insert key node root
            self.root=TreeNode(key)
        else:
            self._insert_recursive(self.root,key)

    def _insert_recursive(self,node,key):
        if not node: # if node is None, create a new TreeNode with the given key
            return TreeNode(key)
        if key < node.key:
            node.left=self._insert_recursive(node.left,key) #if key< node insert left child
        else:
            node.right=self._insert_recursive(node.right,key) #if key > node insert right child
        return node
    
    def search(self,key): # search just value nabe
        return self._search_recursive(self.root,key) # root given automecticly from befor function

    def _search_recursive(self,node,key):
        if not node or node.key==key:
            return node
        if key < node.key:
            return self._search_recursive(node.left,key) # if search value < root return left child
        return self._search_recursive(node.right,key)# if search value > root return right child 

    def delete(self,key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            if not root.left:
                return root.right #root 6
            elif not root.right:
                return root.left
            temp = self._min_value_node(root.right) #child 7
            root.key = temp.key #root 7 since root 6 < child 7 and delete root 6  so new root 7 
            root.right = self._delete_recursive(root.right, temp.key) # and child 7 delete 
        return root
    
    def _min_value_node(self, node):
        current=node # 7
        while current.left:
            current=current.left
        return current
    
    def inorder_traversal(self): # no value inter
        self._inorder_traversal(self.root)# automaticly input

    def _inorder_traversal(self,node):
        if node:
            self._inorder_traversal(node.left) #5
            print(node.key,end=" ")#6
            self._inorder_traversal(node.right) #7

    def preorder_traversal(self):
        self._preorder_traversal(self.root)

    def _preorder_traversal(self, node):
        if node:
            print(node.key, end=" ")
            self._preorder_traversal(node.left)
            self._preorder_traversal(node.right)

    def postorder_traversal(self):
        self._postorder_traversal(self.root)
        
    def _postorder_traversal(self, node):
        if node:
            self._postorder_traversal(node.left)
            self._postorder_traversal(node.right)
            print(node.key, end=" ")       



# Example usage:
bt = BinaryTree()
bt.insert(50)
bt.insert(30)
bt.insert(70)
bt.insert(20)
bt.insert(40)
bt.insert(60)
bt.insert(80)


print("Inorder Traversal:")
bt.inorder_traversal()  # Output: 20 30 40 50 60 70 80

print("\nPreorder Traversal:")
bt.preorder_traversal()  # Output: 50 30 20 40 70 60 80

print("\nPostorder Traversal:")
bt.postorder_traversal()  # Output: 20 40 30 60 80 70 50


# Delete a node
bt.delete(30)
print("\nBinary tree after deleting key 30:")
bt.inorder_traversal()  # Output: 20 40 50 60 70 80




#heap max insert,delete,search and finding parent ,child(left,ight)
class MaxHeap:
    def __init__(self):
        self.heap = []#null list

    def insert(self,key):
        self.heap.append(key)
        self._heapify_up(len(self.heap)-1)  #index=len-1

    def _heapify_up(self,index): #find parent by given index
        parent=(index-1)//2
        if index > 0 and self.heap[parent] <self.heap[index]:
            self.heap[parent] ,self.heap[index]=self.heap[index],self.heap[parent] #swap between parent and child when parent !>chid
            self._heapify_up(parent)

    def delete(self,key):
        if key in self.heap:
            index=self.heap.index(key) #index of deleting value
            self.heap[index],self.heap[-1]=self.heap[-1],self.heap[index] #swap dlwting value by last value in list
            self.heap.pop() #last means deleting value pop
            if index < len(self.heap): 
                self._heapify_down(index) 
        else:
            print("key not found in heap")
  
  
    def _heapify_down(self,index):
        left_child=2*index+1 
        right_child=2*index+2
        largest =index 
        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child #if parent value small than left child .so swap
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child  
        if largest !=index: #until parent larger than child
            self.heap[largest],self.heap[index]=self.heap[index],self.heap[largest]
            self._heapify_down(largest)
    
    def heapify(self,array):
        self.heap=array
        n=len(array)
        for i in range(n//2-1,-1,-1): # starting:n//2-1  ,end untill o=-1,decrement=-1  
            self._heapify_down(i)

    def get_max(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

    def extract_max(self):
        if self.heap:
            max_val=self.heap[0]
            self.delete(max_val)
            return max_val
        else:
            return None

    def __str__(self):
        return str(self.heap)


# Example usage:
heap = MaxHeap()
heap.insert(10)
heap.insert(20)
heap.insert(15)
heap.insert(30)
heap.insert(40)

print("Max heap after insertions:", heap)

heap.delete(15)
print("Max heap after deletion of key 15:", heap)


print("Maximum element in the heap:", heap.get_max())

print("Extracting maximum element from the heap:", heap.extract_max())
print("Max heap after extraction:", heap)                   




# Bfs Traversal: breadth-first traversal (level order traversal
class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


def bfs_traversal(root):
    if root is None:
        return
    queue=[root] #bsf define by queue
    while queue: #untill queue is empty
        node=queue.pop(0)
        print(node.value,end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
#connecting the bionary tree
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)
print("BFS traversal:")
bfs_traversal(root)

#BFS adjacency treversal:
from collections import deque #You can add elements to both ends of the deque and remove elements from either end.
class Graph:
    def __init__(self):
        self.adj_list={} #constractor empty dictionary: final result

    def add_edge(self,u,v): #addition two nodes by edges
        if u not in self.adj_list: # u not in adjacency dict
            self.adj_list[u]=[] #null in u pair {U: } dictionary
        self.adj_list[u].append(v) # appned doctionary {U:V}

    def bfs(self,start):
        visited=set() #VISITED null SET
        queue=deque([start]) #innner [start] iterable list : QUEUE processing list
        visited.add(start)

        while queue:
            vertex=queue.popleft() # Removes the leftmost element from the queue and assigns it to vertex
            print(vertex,end=" ")

            if vertex in self.adj_list[vertex]: #in final dict
                for neighbor in self.adj_list[vertex]:#key:values  in value defined
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

g=Graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(3,3)

print("Breadth-First Traversal:")
g.bfs(2)  # Starting BFS from vertex 2




# DFS traversal
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def dfs_traversal_inorder(root):
    if not root:
        return []

    result = []

    def dfs_helper(node):
        if node:
            dfs_helper(node.left)
            result.append(node.key)
            dfs_helper(node.right)

    dfs_helper(root)
    return result

def dfs_traversal_preorder(root):
    if not root:
        return []

    result = []

    def dfs_helper(node):
        if node:
            result.append(node.key)
            dfs_helper(node.left)
            dfs_helper(node.right)

    dfs_helper(root)
    return result

def dfs_traversal_postorder(root):
    if not root:
        return []

    result = []

    def dfs_helper(node):
        if node:
            dfs_helper(node.left)
            dfs_helper(node.right)
            result.append(node.key)

    dfs_helper(root)
    return result

# Example usage:
# Constructing a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Performing DFS traversal in inorder, preorder, and postorder
print("Inorder DFS Traversal:", dfs_traversal_inorder(root))
print("Preorder DFS Traversal:", dfs_traversal_preorder(root))
print("Postorder DFS Traversal:", dfs_traversal_postorder(root))



# DFS adjency traversal:
class Graph:
    def __init__(self):
        self.adj_list={} #final result dictionary

    def add_edge(self,u,v):
        if u not in self.adj_list:
            self.adj_list[u] =[] # {key: }
        self.adj_list[u].append(v) #{key:value}]

    def dfs(self,start):
        visited = set()
        self.dfs_util(start,visited) 

    def dfs_util(self,v,visited):
        visited.add(v)
        print(v,end=" ")

        if v in self.adj_list:
            for neighbor in self.adj_list[v]:
                if neighbor not in visited:
                    self.dfs_util(neighbor, visited)        


# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Depth-First Traversal:")
g.dfs(2)  # Starting DFS from vertex 2



#adjacency graph matrix:

class Graph:
    def __init__(self,num_vertices):
        self.num_vertices=num_vertices
        self.adj_matrix=[[0]*num_vertices for _ in range(num_vertices)]
        # Creates a list of num_vertices sublists (rows), each initialized with 0.
        #, _ is used as a conventional placeholder variable name in Python when you don't need to use the loop variable. 


    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1  # Assuming an undirected graph

    def remove_edge(self, u, v):
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0    

    def print_graph(self):
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))

# Example usage:
g = Graph(5)  # Create a graph with 5 vertices
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

print("Adjacency Matrix of the graph:")
g.print_graph() 

# print(" ".join(map(str, row))):
# Inside the loop, this line prints the elements of the current row separated by spaces.
# map(str, row) converts each element of the row to a string. This is necessary because join requires all elements to be strings.
# " ".join(...) joins the elements of the row into a single string, separated by spaces.
# Finally, print(...) prints the resulting string to the console.

  
                 

                             
                

    
