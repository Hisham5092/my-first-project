# Minimum value in an array
from os import remove
# from wsgiref.validate import header_re


# import time
# start_time = time.perf_counter()
# my_array = [7, 12, 9, 4, 11]
# min_val = my_array[0]
# for i in range(len(my_array)):
#     if my_array[i] < min_val :
#         min_val = my_array [i]
#
# print(min_val)
#
# end_time = time.perf_counter()
# print(f"Execution time: {end_time - start_time:.6f} seconds")

#Bubble Sort with Improvements
# import time
# start_time = time.perf_counter()
# my_array = [7, 3, 9, 12, 11]
# n = len(my_array)
# for i in range (n-1):
#     swapped = False
#     for j in range (n-i-1):
#         if my_array[j] > my_array[j+1]:
#             my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
#             swapped = True
#
#     if not swapped:
#         break
# print("Sorted array:", my_array)
#
# end_time = time.perf_counter()
# print(f"Execution time: {end_time - start_time:.6f} seconds")

# Selection Sort with Improvements
# my_array = [64, 34, 25, 12, 22, 11, 90, 5]
# n = len(my_array)

# for i in range (n):
#     min_index = i
#     for j in range(i+1, n):
#         if my_array[j] < my_array[min_index]:
#             min_index = j
#     my_array[i], my_array[min_index] = my_array[min_index], my_array[i]
# print("Sorted array:", my_array)

# Insertion Sort with Improvements

# my_array = [64, 34, 25, 12, 22, 11, 90, 5]
# n = len(my_array)
# for i in range (1,n):
#     insert_index = i
#     current_value = my_array[i]
#     for j in range (i-1,-1,-1):
#         if my_array[j] > current_value:
#             my_array[j+1] = my_array[j]
#             insert_index = j
#         else:
#             break
#     my_array[insert_index] = current_value
# print("Sorted array:", my_array)

# Quick Sort
# def partition (arr, left, right):
#     i = left
#     j = right - 1
#     pivot = arr[right]
#
#     while i < j:
#         while i < right and arr[i] < pivot:
#             i += 1
#         while j > left and arr[j] > pivot:
#             j -= 1
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#     if arr[i] > pivot:
#         arr[i], arr[right] = arr[right], arr[i]
#     return i
#
# def quicksort (arr, left, right):
#     if left < right:
#         partition_pos = partition(arr, left, right)
#         quicksort(arr, left, partition_pos - 1)
#         quicksort(arr, partition_pos + 1, right)
#
# arr = [22, 11, 88, 66, 55, 77, 33, 44]
# quicksort(arr, 0, len(arr) - 1)
# print(arr)

# Merge Sort

# def mergeSort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]
#
#     sorted_left = mergeSort(left_half)
#     sorted_right = mergeSort(right_half)
#
#     return merge(sorted_left,sorted_right)
#
# def merge(left, right):
#     result =[]
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right [j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
#
# unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
# sortedArr = mergeSort(unsortedArr)
# print("Sorted array:", sortedArr)


# Binary Search

# def binary_search(arr, target_val):
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if arr[mid] == target_val:
#             return mid
#
#         if arr[mid] < target_val:
#             left = mid + 1
#
#         else:
#             right =  mid - 1
#     return -1
#
# myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# myTarget = 15
#
# result = binary_search(myArray, myTarget)
#
# if result != -1:
#     print("Value",myTarget,"found at index", result)
# else:
#     print("Target not found in array.")


# Linked List Traversal

# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# node1 = Node (3)
# node2 = Node (5)
# node3 = Node (6)
# node4 = Node (9)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
# current_node = node1
#
# def traverseAndPrint(head):
#     current_node = head
#     while current_node:
#         print(current_node.data, end= '->')
#         current_node = current_node.next
#     print("Null")
#
# traverseAndPrint(node1)

# Minimum Value in Linked List

# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# def find_min_val (head):
#     min_val = head.data
#     current = head.next
#     while current:
#         if current.data < min_val:
#             min_val = current.data
#         current = current.next
#     return min_val
#
#
# node1 = Node (8)
# node2 = Node (10)
# node3 = Node (6)
# node4 = Node (9)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
#
# result = find_min_val(node1)
# print("Lowest value is: ", result )


# Deletion in Linked List

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# def traversal_and_print(head):
#     current_node = head
#     while current_node:
#         print(current_node.data, end='->')
#         current_node = current_node.next
#
#     print("null")
#
# def delete_node (head, node_to_delete):
#
#     if head == node_to_delete:
#         return head.next
#
#     current_node = head
#
#     while current_node.next and current_node.next != node_to_delete:
#         current_node =current_node.next
#
#     if current_node.next is None:
#         return head
#     current_node.next =current_node.next.next
#
#     return head
#
# node1 = Node(7)
# node2 = Node(11)
# node3 = Node(3)
# node4 = Node(2)
# node5 = Node(9)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
#
# print("Before deletion:")
# traversal_and_print(node1)
#
# # Delete node4
# node1 = delete_node(node1, node4)
#
# print("\nAfter deletion:")
# traversal_and_print(node1)


# Insertion in Linked List

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# def traversal_and_print(head):
#     current_node = head
#     while current_node:
#         print(current_node.data, end='->')
#         current_node = current_node.next
#
#     print("null")
#
# def insertion (head, new_node, position):
#     if position == 1:
#         new_node.next  = head
#         return new_node
#     current_node = head
#     for i in range (position - 2):
#         if current_node is None:
#             break
#         current_node = current_node.next
#
#     new_node.next = current_node.next
#     current_node.next = new_node
#     return head
#
# node1 = Node(7)
# node2 = Node(3)
# node3 = Node(2)
# node4 = Node(9)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
#
# print("Original list:")
# traversal_and_print(node1)
#
# # Insert a new node with value 97 at position 2
# newNode = Node(97)
# node1 = insertion(node1, newNode, 2)
#
# print("\nAfter insertion:")
# traversal_and_print(node1)


# Stack with Class

# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, element):
#         self.stack.append(element)
#
#     def pop (self):
#         if self.isEmpty():
#             return "Stack is empty"
#         return self.stack.pop()
#
#     def peek (self):
#         if self.isEmpty():
#             return "Stack is empty"
#         return self.stack[-1]
#
#     def isEmpty(self):
#         return len(self.stack) == 0
#
#     def size(self):
#         return len(self.stack)
# myStack = Stack()
#
# myStack.push('A')
# myStack.push('B')
# myStack.push('C')
# print("Stack: ", myStack.stack)
#
# print("Pop: ", myStack.pop())
#
# print("Peek: ", myStack.peek())
#
# print("isEmpty: ", myStack.isEmpty())
#
# print("Size: ", myStack.size())

# Stack with Linked List

# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None
#
# class Stack:
#
#     def __init__(self):
#         self. head = None
#         self.size = 0
#
#     def push(self,value):
#         new_node = Node (value)
#         if self.head:
#             new_node.next = self.head
#         self.head = new_node
#         self.size += 1
#     def pop(self):
#         if self.isEmpty():
#             return "Stack is Empty"
#         popped_value = self.head
#         self.head = self.head.next
#         self.size -= 1
#         return popped_value.value
#
#     def peek(self):
#         if self.isEmpty():
#             return "Stack is Empty"
#         return self.head.value
#
#     def isEmpty(self):
#         return self.size == 0
#     def stack_size(self):
#         return self.size
#
# myStack = Stack()
# myStack.push('A')
# myStack.push('B')
# myStack.push('C')
#
# print("Pop: ", myStack.pop())
# print("Peek: ", myStack.peek())
# print("isEmpty: ", myStack.isEmpty())
# print("Size: ", myStack.stack_size())


# Queue Linked List

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#         self.size = 0
#
#     def enqueue(self,element):
#         new_node = Node(element)
#         if self.rear is None:
#             self.front = self.rear = new_node
#             self.size += 1
#             return
#         self.rear.next = new_node
#         self.rear = new_node
#         self.size += 1
#
#     def dequeue(self):
#         if self.isEmpty():
#             return "Queue is empty"
#         temp = self.front
#         self.front = temp.next
#         self.size -= 1
#         if self.front is None:
#             self.rear = None
#         return temp.data
#
#     def peek(self):
#         if self.isEmpty():
#             return "Queue is empty"
#         return self.front.data
#
#     def isEmpty(self):
#         return self.size == 0
#
#     def queue_size(self):
#         return self.size
#
#     def printQueue(self):
#         temp = self.front
#         while temp:
#             print(temp.data, end=" ")
#             temp = temp.next
#         print()
#
# # Create a queue
# myQueue = Queue()
#
# myQueue.enqueue('A')
# myQueue.enqueue('B')
# myQueue.enqueue('C')
# print("Queue: ", end="")
# myQueue.printQueue()
#
# print("Dequeue: ", myQueue.dequeue())
#
# print("Peek: ", myQueue.peek())
#
# print("isEmpty: ", myQueue.isEmpty())
#
# print("Size: ", myQueue.queue_size())

# Looking up a name using a hash function

# my_hash_set = [None,'Jones',None,'Lisa',None,'Bob',None,'Siri','Pete',None]
#
# def hash (value):
#     sum = 0
#     for char in value:
#         sum = sum + ord(char)
#
#     return sum % 10
#
# def contains(name):
#     index = hash(name)
#     return my_hash_set[index] == name
#
# print("'Pete' is in the Hash Set:",contains('Pete'))


# Handling Collison

# my_hash_set = [
#     [None],
#     ['Jones'],
#     [None],
#     ['Lisa'],
#     [None],
#     ['Bob'],
#     [None],
#     ['Siri'],
#     ['Pete'],
#     [None]
# ]
#
# def hash_function(value):
#     sum = 0
#     for char in value:
#         sum = sum + ord(char)
#
#     return sum % 10
#
# def add(value):
#     index = hash_function(value)
#     bucket = my_hash_set[index]
#     if value not in bucket:
#         bucket.append(value)
#
# def contains(value):
#     index = hash_function(value)
#     bucket = my_hash_set[index]
#     return value in bucket
#
# add('Stuart')
# print(my_hash_set)
# print('Contains Stuart:', contains('Stuart'))


# Hash Sets
# class SimpleHashSet:
#     def __init__(self, size):
#         self.size = size
#         self.buckets = []
#         for i in range (size):
#             self.buckets.append([])
#
#     def hash_function(self,value):
#         sum = 0
#         for char in value:
#             sum = sum + ord(char)
#
#         return sum % 10
#
#     def add(self, value):
#         index = self. hash_function(value)
#         bucket = self.buckets[index]
#         if value not in bucket:
#             bucket.append(value)
#
#     def contains(self, value):
#         index = self.hash_function(value)
#         bucket = self.buckets[index]
#         return value in bucket
#
#     def remove(self, value):
#         index = self.hash_function(value)
#         bucket = self.buckets[index]
#         if value in bucket:
#             bucket.remove(value)
#
#     def print_set(self):
#         print("Hash Set Contents:")
#         for index, bucket in enumerate(self.buckets):
#             print(f"Bucket {index}: {bucket}")
#
# hash_set = SimpleHashSet(size=10)
#
# hash_set.add("Charlotte")
# hash_set.add("Thomas")
# hash_set.add("Jens")
# hash_set.add("Peter")
# hash_set.add("Lisa")
# hash_set.add("Adele")
# hash_set.add("Michaela")
# hash_set.add("Bob")
# hash_set.print_set()
# print("\n'Peter' is in the set:",hash_set.contains('Peter'))
# print("Removing 'Peter'")
# hash_set.remove('Peter')
# print("'Peter' is in the set:",hash_set.contains('Peter'))
# print("'Adele' has hash code:",hash_set.hash_function('Adele'))

# Hash Map

# class SimpleHashMap:
#     def __init__(self, size):
#         self.size = size
#         self.buckets = []
#         for i in range (size):
#             self.buckets.append([])
#
#     def hash_function(self, key):
#         numeric_sum = 0
#         for char in key:
#             if char.isdigit():
#                 numeric_sum = numeric_sum + int(char)
#
#         return numeric_sum % 10
#
#     def put(self, key, value):
#         index = self.hash_function(key)
#         bucket = self.buckets[index]
#         for i, (k,v) in enumerate(bucket):
#             if k == key:
#                 bucket[i] = (key, value)
#                 return
#
#         bucket.append((key, value))
#
#     def get(self, key):
#         index = self.hash_function(key)
#         bucket = self.buckets[index]
#         for k,v in enumerate(bucket):
#             if k == key:
#                 return v
#         return None
#
#     def remove(self, key):
#         index = self.hash_function(key)
#         bucket = self.buckets[index]
#         for i, (k,v) in enumerate(bucket):
#             if k == key:
#                 del bucket[i]
#                 return
#     def print_map(self):
#         print("Hash Map Contents:")
#         for index, bucket in enumerate(self.buckets):
#             print(f"Bucket {index}: {bucket}")
#
# hash_map = SimpleHashMap(size=10)
#
# # Adding some entries
# hash_map.put("123-4567", "Charlotte")
# hash_map.put("123-4568", "Thomas")
# hash_map.put("123-4569", "Jens")
# hash_map.put("123-4570", "Peter")
# hash_map.put("123-4571", "Lisa")
# hash_map.put("123-4672", "Adele")
# hash_map.put("123-4573", "Michaela")
# hash_map.put("123-6574", "Bob")
#
# hash_map.print_map()
#
# print("\nName associated with '123-4570':", hash_map.get("123-4570"))
#
# print("Updating the name for '123-4570' to 'James'")
# hash_map.put("123-4570","James")
#
# print("Name associated with '123-4570':", hash_map.get("123-4570"))

# Binary Tree Pre/In/Post Order

# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.right = None
#         self.left = None

# def pre_order(node):
#     if node is None:
#         return
#     print(node.data, end=',')
#     pre_order(node.left)
#     pre_order(node.right)

# def post_order(node):
#     if node is None:
#         return
#     post_order(node.left)
#     post_order(node.right)
#     print(node.data, end=',')

# def in_order(node):
#     if node is None:
#         return
#     in_order(node.left)
#     print(node.data, end=',')
#     in_order(node.right)
#
# root = TreeNode('R')
# nodeA = TreeNode('A')
# nodeB = TreeNode('B')
# nodeC = TreeNode('C')
# nodeD = TreeNode('D')
# nodeE = TreeNode('E')
# nodeF = TreeNode('F')
# nodeG = TreeNode('G')
#
# root.left = nodeA
# root.right = nodeB
#
# nodeA.left = nodeC
# nodeA.right = nodeD
#
# nodeB.left = nodeE
# nodeB.right = nodeF
#
# nodeF.left = nodeG
#
# in_order(root)

# Binary Tree Array

# binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']
#
# def left_child_index(index):
#     return 2 * index + 1
#
# def right_child_index(index):
#     return 2 * index + 2
#
# def get_data(index):
#     if 0 <= index < len(binary_tree_array):
#         return binary_tree_array[index]
#     return None
#
# right_child = right_child_index(0)
# left_child_of_right_child = left_child_index(right_child)
# data = get_data(left_child_of_right_child)
#
# print("root.right.left.data:", data)


# Binary Tree Array Pre/In/Post Order

# binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']
#
# def left_child_index(index):
#     return 2 * index + 1
#
# def right_child_index(index):
#     return 2 * index + 2
#
# def pre_order(index):
#     if index >= len(binary_tree_array) or binary_tree_array[index] is None:
#         return []
#     return [binary_tree_array[index]] + pre_order(left_child_index(index)) + pre_order(right_child_index(index))
#
# def in_order (index):
#     if index >= len(binary_tree_array) or binary_tree_array[index] is None:
#         return []
#     return pre_order(left_child_index(index)) + [binary_tree_array[index]] +  pre_order(right_child_index(index))
#
# def post_order(index):
#     if index >= len(binary_tree_array) or binary_tree_array[index] is None:
#         return []
#     return pre_order(left_child_index(index)) + pre_order(right_child_index(index)) + [binary_tree_array[index]]
#
# print("Pre-order Traversal:", pre_order(0))
# print("In-order Traversal:", in_order(0))
# print("Post-order Traversal:", post_order(0))


# Finding Value in Binary Search Tree

# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.right = None
#         self.left = None
#
# def search (node, target):
#     if node is None:
#         return None
#     elif node.data == target:
#         return node
#     elif target < node.data:
#         return search(node.left, target)
#     else:
#         return search(node.right, target)
# root = TreeNode(13)
# node7 = TreeNode(7)
# node15 = TreeNode(15)
# node3 = TreeNode(3)
# node8 = TreeNode(8)
#
#
#
# node14 = TreeNode(14)
# node19 = TreeNode(19)
# node18 = TreeNode(18)
#
# root.left = node7
# root.right = node15
# node7.left = node3
# node7.right = node8
#
# node15.left = node14
# node15.right = node19

# Graph

# vertexData = ['A', 'B', 'C', 'D']
#
# adjacency_matrix = [
#     [0, 1, 1, 1],  # Edges for A
#     [1, 0, 1, 0],  # Edges for B
#     [1, 1, 0, 0],  # Edges for C
#     [1, 0, 0, 0]   # Edges for D
# ]
#
# def print_matrix(matrix):
#     print(f"Adjacency Matrix: ")
#     for row in matrix:
#         print(row)
#
# def print_connections(matrix, vertices):
#     for i in range(len(vertices)):
#         print(f"{vertices[i]}: ", end='')
#         for j in range(len(vertices)):
#             if matrix[i][j]:
#                 print(vertices[j], end=' ')
#         print()
#
# print_matrix(adjacency_matrix)
# print_connections(adjacency_matrix, vertexData)


# Graph Class
# class Graph:
#     def __init__(self,size):
#         self.adj_matrix =[]
#         for i in range(size):
#             row = [0] * size
#             self.adj_matrix.append(row)
#         self.size = size
#         self.vertex_data =[''] * size
#
#     def add_edge(self, u, v):
#         if 0 <= u < self.size and 0 <= v < self.size:
#             self.adj_matrix[u][v] = 1
#             self.adj_matrix[v][u] = 1
#     def add_vertex_data(self, vertex, data):
#         if 0 <= vertex < self.size:
#             self.vertex_data[vertex] = data
#
#     def print_graph(self):
#         print("Adjacency Matrix:")
#         for row in self.adj_matrix:
#             print(' '.join(map(str, row)))
#         print("\nVertex Data:")
#         for vertex, data in enumerate(self.vertex_data):
#                 print(f"Vertex {vertex}: {data}")
#
# g = Graph(4)
# g.add_vertex_data(0, 'A')
# g.add_vertex_data(1, 'B')
# g.add_vertex_data(2, 'C')
# g.add_vertex_data(3, 'D')
# g.add_edge(0, 1)  # A - B
# g.add_edge(0, 2)  # A - C
# g.add_edge(0, 3)  # A - D
# g.add_edge(1, 2)  # B - C
#
# g.print_graph()

# Graph Class Weighted
# class Graph:
#     def __init__(self,size):
#         self.adj_matrix = [[0] * size for _ in range (size)]
#         self.size = size
#         self.vertex_data = [''] * size
#
#     def add_edge(self,u,v,weight):
#         if 0 <= u < self.size and 0 <= v < self.size:
#             self.adj_matrix [u][v] = weight
#
#
#     def add_vertex_data (self, vertex, data):
#         if 0 <= vertex < self.size:
#             self.vertex_data [vertex] = data
#
#     def print_graph (self):
#         print("Adjacency Matrix:")
#         for row in self.adj_matrix:
#             print(' '.join(map(str, row)))
#         print("\nVertex Data:")
#         for vertex, data in enumerate (self.vertex_data):
#             print(f"Vertex {vertex}: {data}")
#
# g = Graph(4)
# g.add_vertex_data(0, 'A')
# g.add_vertex_data(1, 'B')
# g.add_vertex_data(2, 'C')
# g.add_vertex_data(3, 'D')
# g.add_edge(0, 1, 3)  # A -> B with weight 3
# g.add_edge(0, 2, 2)  # A -> C with weight 2
# g.add_edge(3, 0, 4)  # D -> A with weight 4
# g.add_edge(2, 1, 1)  # C -> B with weight 1
#
# g.print_graph()