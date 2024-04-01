# 1.search algorithom(linear,binary,)
# 2.sorting(buble,selection,insertion,marge,quick)
# 3.time complexecity(big o notation,space complexecity)
# 4.divided and Qonqure(merge sort)
# 5.dynamic programming(knapsack,lcs,unbounded)
# 6.tree(Bfs,Dfs)
# 7.graph(node,edge,graph traversal 2D matrix)
# 8.shortest path graph(dijkstra,bellmen Ford->positive edge and cycle,floidwarshal->posi & negi edge, but cycle posi only)

# যে ৭ ধরনের এলগরিদম তোমাকে শিখতে হবে: 
# ১) Searching Algorithms এর মধ্যে Linear Search আর Binary Search কিভাবে কাজ করে কোনটার কি রকম টাইম কমপ্লেক্সিটি সেটা জানতে হবে। 
# ২) Sorting Algorithms এর মধ্যে Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort কিভাবে কাজ করে। প্রত্যেকটার টাইম কমপ্লেক্সিটি এর মধ্যে বেস্ট কেইস, worst case আর অ্যাভারেজ কেইস কখন কেন হয় সেটা জানতে হবে। 
# ৩) কখন বুঝবে কোনটা Dynamic programming (DP) এর প্রব্লেম। সেটার মধ্যে base কেইস কিভাবে ঠিক করবে। বা sub প্রব্লেম এ কিভাবে ভাগ করবে। Recurrence কিভাবে করবে। শুরুটা Fibonacci Sequence, Longest Common Subsequence (LCS), বা Coin Change Problem গুলো দিয়ে করতে পারো। 
# ৪) Tree রিলেটেড এলগরিদম এর মধ্যে BFS আর DFS তো তোমাকে জানতেই হবে। এর বাইরে Binary Search Tree  এর মধ্যে নতুন উপাদান যোগ করা রিমুভ করার সিস্টেম তোমাকে জানতে হবে। 
# ৫) বিভিন্ন ধরনের graph এর জন্য আবার Shortest path বের করার সিস্টেম দেখতে পারো। এর মধ্যে Dijkstra's বা Bellman-Ford দেখতে পারো।
# ৬)  Divide and Conquer Algorithms এর মধ্যে বাইনারি সার্চ, মার্জ শর্ট অন্যতম। 
# ৭) টাইম আর স্পেস কমপ্লেক্সিটি ছাড়া ডাটা স্ট্রাকচার, এলগরিদম এর মর্ম বুঝবে না। তাই Big O Notation সম্পর্কে জানতে হবে। Constant Time O(1), Linear Time O(n), Logarithmic Time O(log n), Linearithmic Time O(n log n), Quadratic Time O(n^2), Exponential Time O(2^n) এইগুলা কখন হয়। সেটা বুঝতে হবে। 
# -----
# এইটা শুরু করার লিষ্ট। এইগুলা বেসিক আর ইন্টারমেডিয়েট লেভেল মিলিয়ে। তবে কারো প্রব্লেম সলভিং বা কম্পিটিটিভ প্রোগ্রামিংয়ে ইচ্ছা থাকলে সে এইগুলা দিয়ে শুরু করে আরো ভিতরে ঢুকতে পারে। 
# -----
# এই জিনিসগুলো তুমি চাইলে my code school, Kunal Kushwaha, freeCodeCamp, Abdul Bari এর মতো প্রচুর ইউটিউব চ্যানেল আছে। সেগুলা থেকে শিখতে পারো। অথবা শাফায়েত এর ব্লগ বা programiz এর Learn DS & Algorithms দেখতে পারো। 

#1. search algorithom
# linerar search: normaly in loops index's value compare to key
# Linear Search:
# Best Case Time Complexity: O(1) begain list
# Average Case Time Complexity: O(n) half
# Worst Case Time Complexity: O(n) last

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr=[3,4,5,6,3,4,5]
target=3
result=linear_search(arr,target)
if result !=-1:
    print(f"Linear search: target {target} found at index {result}")
else:
    print(f"Linear search: target {target} not found at index {result}")


#Bionary search: 1.sort 2.mid 3.data>mid ->l=mid+1 4.data<mid ->r=mid-1 5.mid
# Binary Search:
# Best Case Time Complexity: O(1) target middle
# Average Case Time Complexity: O(log n) divides the search space in half at each step.
# Worst Case Time Complexity: O(log n) the ends of the sorted array.

def binary_search(arr,target):
    arr.sort() #sort
    low,high=0,len(arr)-1 #low=0 & high=len()-1
    while low<= high:
        mid =(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

# Example usage:
arr = [9, 4, 2, 7, 1, 5]
target = 7
result = binary_search(arr, target)
if result != -1:
    print(f"Binary search: Found target {target} at index {result}.")
else:
    print(f"Binary search: Target {target} not found in the array.")            


#bouble sort
# Best Case Time Complexity: O(n) - When the array is already sorted.
# Worst Case Time Complexity: O(n^2) - When the array is sorted in reverse order.
# Average Case Time Complexity: O(n^2).
# see the picture

def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1): #last vlue sorted so neglect last index
            if arr[j] > arr[j+1]: #compare 1st > 2nd
                arr[j],arr[j+1] = arr[j+1],arr[j] #then swap
                swapped = True
            if not swapped:
                break
    return arr

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Bubble Sort:", sorted_arr)


#selection sort:
# Best Case Time Complexity: O(n^2)
# Worst Case Time Complexity: O(n^2)
# Average Case Time Complexity: O(n^2)
# see the pic

def selection_sort(arr):
    n=len(arr)
    for i in range(n): #iteration
        min_index=i #for initialize minimum and supposed sorted portion
        for j in range(i+1,n): #suppossed another unsorted portion
            if arr[j] < arr[min_index]:#unsorted portion every elements compare to single another sorted portion
                min_index=j    # j < i update i=j
        arr[i],arr[min_index] = arr[min_index],arr[i] #swap 
    return arr     

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = selection_sort(arr.copy())
print("Selection Sort:", sorted_arr)


# Insertion Sort:
# Best Case Time Complexity: O(n) - When the array is already sorted.
# Worst Case Time Complexity: O(n^2) - When the array is sorted in reverse order.
# Average Case Time Complexity: O(n^2)
# see the pic

def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n): #neglect first means single sorted portion
        key=arr[i] #vlue of unsorted portion loop
        j=i-1 #define before unsorted value sometime means single sorted portion 
        while j>=0 and arr[j] > key: #sorted index > 0 ,j>i=sort>unsorted
            arr[j+1]=arr[j] #set new unsorted value= sorted value 
            j-=1 # sorted before element comprare in loop
        arr[j+1] =key #like loop
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = insertion_sort(arr.copy())
print("Insertion Sort:", sorted_arr)


# Quick Sort
# Best Case Time Complexity: O(n log n)
# Worst Case Time Complexity: O(n^2) - When the pivot is always the smallest or largest element.
# Average Case Time Complexity: O(n log n).
# see the picture that is largest conception greater than python quick_sort

def quick_sort(arr):
    if len(arr)<=1: # 1 element always sorted
        return arr
    pivot=arr[len(arr)//2] #pivot set middle index
    left=[x for x in arr if x < pivot]
    middle=[x for x in arr if x == pivot]
    right=[x for x in arr if x > pivot]
    return quick_sort(left) + quick_sort(middle) + quick_sort(right)

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr.copy())
print("Quick Sort:", sorted_arr)


# marge sort for divide conquer 
# Best Case Time Complexity: O(n log n)
# Worst Case Time Complexity: O(n log n)
# Average Case Time Complexity: O(n log n).
# see the picture that is largest conception greater than python marge sort

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2 #mid 
    left_half=merge_sort(arr[:mid]) #left list
    right_half=merge_sort(arr[mid:]) #right list
    return merge(left_half, right_half) #left list,right list

def merge(left, right):
    result=[] #Null list
    i=j=0 #initialize zero
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr.copy())
print("Merge Sort:", sorted_arr)     




#Dijkstar: directed & undirected and positive edges but not any cycle
# n(u)+c(u,v)<n(v)

import heapq
def dijkstra(graph,start):
    #initialize distance dictionary
    distance={vertex: float('infinity') for vertex in graph} #every edge distance infinity like A distance={A:{B:INF,B:INF}}
    distance[start]=0 #initial A distance={A:0}

    # Priority queue for vertices to explore
    priority_queue=[(0,start)] # start er priority 0 means sober agee [(0,A),(1,B)]

    while priority_queue:
        current_distance,current_vertex=heapq.heappop(priority_queue) # pop from start point and kept it this two variable location [(0,A)]
        # Skip if already found a shorter path
        if current_distance > distance[current_vertex]:
            continue # present is larger  than next edge vertex A>B  
        
        for neighbor,weight in graph[current_vertex].items():
            calculated_distance = current_distance + weight #B=A+d
            if calculated_distance < distance[neighbor]: # B<A
                distance[neighbor] = calculated_distance
                heapq.heappush(priority_queue,(calculated_distance, neighbor))
    return distance           


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
print("Shortest distances from vertex", start_vertex, ":", dijkstra(graph, start_vertex))
# Shortest distances from vertex A : {'A': 0, 'B': 1, 'C': 3, 'D': 4}



# Bellman_ford: edge positive & negetive but not negetive cycle
def bellman_ford(graph,start):
    #initialize distance list
    distance={vertex: float('infinity') for vertex in graph}#every edge distance infinity like A distance={A:{B:INF,B:INF}}
    distance[start]=0 #initial A distance={A:0}

    # relex edges repeatedly
    for _ in range(len(graph)-1): #  define like 1. 'A': {'B': -1, 'C': 4},  2.'B': {'C': 3, 'D': 2, 'E': 2},  3.'C': {},  4.'D': {'B': 1, 'C': 5},  5.'E': {'D': -3}
        for u in graph:# Main edges 1. 'A': {1.1 ('B': -1), 1.2 ('C': 4)}
            for v,weight in graph[u].items(): # 1. 'A':{1.1(1.1.1 'B' : 1.1.2 '-1')}
                if distance[u] + weight < distance[v]:
                    distance[v]= distance[u] + weight

    #check for negetive cycles
    for u in graph:
        for v ,weight in graph[u].items():
            if distance[u] + weight < distance[v]:
                print ("Graph contains negetive weight cycles")
                return
    return distance
                        

graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}
start_vertex = 'A'
print("Shortest distances from vertex", start_vertex, ":", bellman_ford(graph, start_vertex))
# Shortest distances from vertex A : {'A': 0, 'B': -1, 'C': 2, 'D': -2, 'E': 1}



#Floyd_Forshal:pair edge positive & negetive but not negetive cycle and all pair path also
def floyed_warshal(graph):
    n=len(graph)
    distance=[[float('inf')]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                distance[i][j]=0 #diagonal value 0
            elif (i,j) in graph:
                distance[i][j]=graph[(i,j)]  

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j],distance[i][k]+distance[k][j])
    return distance              

# Example graph
graph = {
    (0, 1): 3,
    (0, 2): 6,
    (1, 2): 2,
    (1, 3): 1,
    (2, 1): 4,
    (2, 3): 2,
    (3, 0): 3,
    (3, 2): 1
}

result=floyed_warshal(graph)
for row in result:
    print(row)




# 0/1 knapsack
# max_profit, fraction weight alowed,0 or 1 time any items exist
def knapsack_01(values,weights,capacity):
    n=len(values) # item numbers define row in 2D
    dp=[[0] * (capacity+1) for _ in range(n+1)]#initialy all value or profit set 0 #capacity define colum
    
    for i in range(1,n+1): #row up to down like colom 1 to end+1
        for w in range(1,capacity+1): #colum left to right like in any row start to end
            if weights[i-1]<=w: # in befor selected row weight < selected weight 
                dp[i][w]=max(values[i-1]+dp[i-1][w-weights[i-1]],dp[i-1][w])
            else:
                dp[i][w]=dp[i-1][w] 
    return dp[n][capacity] #item e gie value 

values=[60,100,120] #profite input
weights=[10,20,30] #weight input
capacity= 50 # maximum weight capable in bag
print("Maximum value:", knapsack_01(values, weights, capacity))


# unbound knapsack
#  max_profit, fraction weight not  alowed ,more than 1 time item also alowed
def unbounded_knapsack(values, weights, capacity):
    n=len(values) # number of items #up to down in 
    dp=[0]*(capacity+1)
    for w in range(1,capacity+1):
        for i in range(n):
            if weights[i] <= w:
                dp[w]=max(dp[w],values[i]+dp[w-weights[i]])
    return dp[capacity]

# Example usage
values = [10, 30, 20]
weights = [5, 10, 15]
capacity = 100
print("Maximum value (unbounded):", unbounded_knapsack(values, weights, capacity))


#LCS
def longest_common_subsequence(s1, s2):
    m,n=len(s1),len(s2) #length number
    dp=[[0] * (n+1) for _ in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]: #diagonal same
                dp[i][j]=1+dp[i-1][j-1] #new value= 1+befor diagonal
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1]) #new value form befor or left side which larger
    return dp[m][n]
                
s1="AGGTAB"
s2="GXTXAYB"
print("length of common subsequence:",longest_common_subsequence(s1,s2))    













