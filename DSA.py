# Stack
# stack = []
# stack.append(1)
# stack.append(2)
# stack.append(3)
# print("Stack: ", stack)
#
# topElement = stack[-1]
# print("Top Element:" , topElement)
#
# popElement = stack.pop()
# print("Stack after pop:", stack)
#
# isEmpty = not bool (stack)
# print("Empty?: ", isEmpty)
#
# print("Size of the stack:", len(stack))
from operator import index

#Stack Using Class

# class stack:
#     def __init__(self):
#         self.stack = []
#
#     def push (self, elements):
#         self.stack.append(elements)
#
#     def pop (self):
#         if self.isEmpty():
#             return "Stack is empty"
#         return self.stack.pop()
#
#     def peek (self):
#         if self.isEmpty():
#             return "Stack is empty"
#         return self.stack [-1]
#
#     def isEmpty(self):
#         return len (self.stack) == 0
#
#     def size (self):
#         return len(self.stack)
#
# myStack = stack()
#
# myStack.push(4)
# myStack.push(5)
# myStack.push(6)
#
# print("Stack: ", myStack.stack)
# print("Pop: ", myStack.pop())
# print("Stack after pop: ", myStack.stack)
# print("Top element: ", myStack.peek())
# print("Empty? ", myStack.isEmpty())
# print("Size of the stack: ", myStack.size())


#Stack Using Linked List

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class Stack:
#     def __init__(self):
#         self.head = None
#         self.size = 0
#
#     def push (self, data):
#         new_node = Node(data)
#         if self.head:
#             new_node.next = self.head
#         self.head = new_node
#         self.size += 1
#
#     def pop (self):
#         if self.isEmpty():
#             return "Stack is empty"
#         popped_node = self.head
#         self.head = self.head.next
#         self.size -= 1
#         return popped_node.data
#
#     def peek (self):
#         if self.isEmpty():
#             return "Stack is empty"
#         return self.head.data
#
#     def isEmpty(self):
#         return self.size == 0
#
#     def stack_size (self):
#         return self.size
#
#     def traverse_print(self):
#         current_node = self.head
#         while current_node:
#             print(current_node.data, end = " -> ")
#             current_node =current_node.next
#         print()
# myStack = Stack()
#
# myStack.push('1')
# myStack.push('2')
# myStack.push('3')
#
# print("LinkedList: ", end="")
# myStack.traverse_print()
# print("Peek: ", myStack.peek())
# print("Pop: ", myStack.pop())
# print("LinkedList after Pop: ", end="")
# myStack.traverse_print()
# print("isEmpty: ", myStack.isEmpty())
# print("Size: ", myStack.stack_size())

#Queue Using Linked List

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#         self.length = 0
#
#     def enqueue (self, data):
#         new_node = Node (data)
#         if self.rear is None:
#             self.front = self.rear = new_node
#             self.length += 1
#             return
#         self.rear.next = new_node
#         self.rear = new_node
#         self.length += 1
#
#     def dequeue (self):
#         if self.isEmpty():
#             return "Queue is empty"
#         temp = self.front
#         self.front = temp.next
#         self.length -= 1
#         if self.front is None:
#             self.rear = None
#         return temp.data
#     def peek (self):
#         if self.isEmpty():
#             return "Queue is empty"
#         return self.front.data
#     def isEmpty(self):
#         return self.length == 0
#     def size (self):
#         return self.length
#     def print_queue (self):
#         temp = self.front
#         while temp:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print()
# myQueue = Queue()
# myQueue.enqueue('1')
# myQueue.enqueue('2')
# myQueue.enqueue('3')
#
# print("Queue: ", end="")
# myQueue.print_queue()
# print("Peek: ", myQueue.peek())
# print("Dequeue: ", myQueue.dequeue())
# print("Queue after Dequeue: ", end="")
# myQueue.print_queue()
# print("isEmpty: ", myQueue.isEmpty())
# print("Size: ", myQueue.size())

# Linked List Traverse

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# def traverse (head):
#     current_node = head
#     while current_node:
#         print(current_node.data, end=" -> ")
#         current_node = current_node.next
#     print("Null")
#
# node1 = Node (1)
# node2 = Node (2)
# node3 = Node (4)
# node4 = Node (7)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
#
# traverse(node1)


# Linked List Minimum Value

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# def lowest_value (head):
#     minVal = head.data
#     current_node = head.next
#     while current_node:
#         if current_node.data < minVal:
#             minVal = current_node.data
#         current_node = current_node.next
#     return minVal
#
# node1 = Node (1)
# node2 = Node (2)
# node3 = Node (4)
# node4 = Node (7)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
#
# print("The lowest value in the linked list is:", lowest_value(node1))


#Linked List Delete a Node

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
#
# def traverse (head):
#     current_node = head
#     while current_node:
#         print(current_node.data, end=" -> ")
#         current_node = current_node.next
#     print("Null")
#
# def deleteNode (head, nodeToDelete):
#     if head == nodeToDelete:
#         return head.next
#     currentNode = head
#     while currentNode.next != nodeToDelete:
#         currentNode = currentNode.next
#
#     if currentNode.next is None:
#         return head
#     currentNode.next = currentNode.next.next
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
# traverse(node1)
#
# # Delete node4
# node1 = deleteNode(node1, node4)
#
# print("\nAfter deletion:")
# traverse(node1)


#Linked List Insert a Node

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
#
# def traverse (head):
#     current_node = head
#     while current_node:
#         print(current_node.data, end=" -> ")
#         current_node = current_node.next
#     print("Null")
#
# def insertNode (head, newNode, position):
#     if position == 1:
#         newNode.next = head
#         return newNode
#
#     currentNode = head
#
#     for i in range (position - 2):
#         if currentNode.next is None:
#             break
#         currentNode = currentNode.next
#
#     newNode.next = currentNode.next
#     currentNode.next = newNode
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
# traverse(node1)
#
# # Insert a new node with value 97 at position 2
# new_Node = Node(97)
# node1 = insertNode(node1, new_Node, 2)
#
# print("\nAfter insertion:")
# traverse(node1)


# Hash Table

# my_list = [None, None, None, None, None, None, None, None, None, None ]
#
# def hash_func (value):
#     sum_of_char = 0
#     for char in value:
#         sum_of_char = sum_of_char + ord(char)
#
#     return sum_of_char % 10
#
# def add (name):
#     index = hash_func(name)
#     my_list [index] = name
#
# def contains (name):
#     index = hash_func(name)
#     return my_list [index] == name
#
# add('Bob')
# add('Pete')
# add('Jones')
# add('Lisa')
# add('Siri')
# print("'Pete' is in the Hash Table:", contains('Pete'))
# print(my_list)

# Fixed version with collision handling using chaining
# class HashTable:
#     def __init__(self, size=7):
#         self.size = size
#         self.table = [[] for _ in range(size)]  # Each bucket is a list
#
#         # self.table = []  # Start with empty list
#         #
#         # for _ in range(size):
#         #     self.table.append([])  # Add a new empty list each time
#
#         # i = 0
#         # while i < size:
#         #     self.table.append([])
#         #     i += 1
#         # def __init__(self, size=7):
#         #     self.size = size
#         #     self.table = [None] * size  # Create [None, None, None, ...]
#         #
#         #     for i in range(size):
#         #         self.table[i] = []
#
#     def hash_func(self, value):
#         sum_of_char = 0
#         for char in value:
#             sum_of_char += ord(char)
#         return sum_of_char % self.size  # Use correct array size
#
#     def add(self, name):
#         index = self.hash_func(name)
#         bucket = self.table[index]
#
#         # Check if name already exists
#         if name not in bucket:
#             bucket.append(name)
#
#     def contains(self, name):
#         index = self.hash_func(name)
#         bucket = self.table[index]
#         return name in bucket
#
#     def display(self):
#         for i, bucket in enumerate(self.table):
#             print(f"Index {i}: {bucket}")
#
#
# # Test the fixed version
# hash_table = HashTable()
#
# # Add names
# hash_table.add('Bob')
# hash_table.add('Pete')
# hash_table.add('Jones')
# hash_table.add('Lisa')
# hash_table.add('Siri')
#
# print("Hash Table Contents:")
# hash_table.display()
#
# print("\nTesting contains:")
# print("'Pete' is in the Hash Table:", hash_table.contains('Pete'))
# print("'Alice' is in the Hash Table:", hash_table.contains('Alice'))
#
# # Test collision handling
# print("\nTesting collision handling:")
# hash_table.add('Tom')  # If this collides with existing names, both will be stored
# hash_table.display()


# BST In order traversal

# class TreeNode:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# def inorder_traverse (node):
#     if node is None:
#         return
#     inorder_traverse(node.left)
#     print(node.data, end=",")
#     inorder_traverse(node.right)
#
# root = TreeNode (13)
# node1 = TreeNode (7)
# node2 = TreeNode (15)
# node3 = TreeNode (3)
# node4 = TreeNode (8)
# node5 = TreeNode (14)
# node6 = TreeNode (19)
# node7 = TreeNode (18)
#
# root.left = node1
# root.right = node2
# node1.left = node3
# node1.right = node4
# node2.left = node5
# node2.right = node6
# node6.left = node7
#
# inorder_traverse(root)

#BST Finding a value

# class TreeNode:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# def search(node, target):
#     if node is None:
#         return None
#     elif node.data == target:
#         return node
#     elif target < node.data:
#         return search(node.left, target)
#     else:
#         return search(node.right, target)
#
# root = TreeNode (13)
# node1 = TreeNode (7)
# node2 = TreeNode (15)
# node3 = TreeNode (3)
# node4 = TreeNode (8)
# node5 = TreeNode (14)
# node6 = TreeNode (19)
# node7 = TreeNode (18)
#
# root.left = node1
# root.right = node2
# node1.left = node3
# node1.right = node4
# node2.left = node5
# node2.right = node6
# node6.left = node7
#
# result = search(root,13)
#
# if result:
#     print(f"We found the value : {result.data}")
# else:
#     print("Value doesn't exist")

#BST inserting a node
# class TreeNode:
#   def __init__(self, data):
#     self.data = data
#     self.left = None
#     self.right = None
#
# def insert(node, data):
#   if node is None:
#     return TreeNode(data)
#   else:
#     if data < node.data:
#       node.left = insert(node.left, data)
#     elif data > node.data:
#       node.right = insert(node.right, data)
#     return node
#
# def inOrderTraversal(node):
#   if node is None:
#     return
#   inOrderTraversal(node.left)
#   print(node.data, end=", ")
#   inOrderTraversal(node.right)
#
# root = TreeNode(13)
# node7 = TreeNode(7)
# node15 = TreeNode(15)
# node3 = TreeNode(3)
# node8 = TreeNode(8)
# node14 = TreeNode(14)
# node19 = TreeNode(19)
# node18 = TreeNode(18)
#
# root.left = node7
# root.right = node15
#
# node7.left = node3
# node7.right = node8
#
# node15.left = node14
# node15.right = node19
#
# node19.left = node18
#
# # Inserting new value into the BST
# insert(root, 10)

# Traverse
# inOrderTraversal(root)

#BST finding minimum value

# class TreeNode:
#   def __init__(self, data):
#     self.data = data
#     self.left = None
#     self.right = None
#
# def inOrderTraversal(node):
#   if node is None:
#     return
#   inOrderTraversal(node.left)
#   print(node.data, end=", ")
#   inOrderTraversal(node.right)
#
# def minValueNode(node):
#   current = node
#   while current.left is not None:
#     current = current.left
#   return current
#
# root = TreeNode(13)
# node7 = TreeNode(7)
# node15 = TreeNode(15)
# node3 = TreeNode(3)
# node8 = TreeNode(8)
# node14 = TreeNode(14)
# node19 = TreeNode(19)
# node18 = TreeNode(18)
#
# root.left = node7
# root.right = node15
#
# node7.left = node3
# node7.right = node8
#
# node15.left = node14
# node15.right = node19
#
# node19.left = node18
#
# # Traverse
# inOrderTraversal(root)
#
# # Find Lowest
# print("\nLowest value:",minValueNode(root).data)

#Linear Search

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1
#
# mylist = [1, 4, 5, 6, 7, 9]
# x = 9
# result = linear_search(mylist,x)
#
# if result != -1:
#     print("Index found", result)
# else:
#     print("Index not found")

#Binary Search

# def binary_search (arr, target):
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if arr[mid] == target:
#             return mid
#         if arr[mid] < target:
#             left  = mid + 1
#         else:
#             right = mid - 1
#     return -1
#
# mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# x = 11
#
# result = binary_search(mylist, x)
#
# if result != -1:
#   print("Found at index", result)
# else:
#   print("Not found")


#Bubble Sort
# mylist = [64, 34, 25, 12, 22, 11, 90, 5]
# n = len(mylist)
#
# for i in range (n - 1):
#     for j in range (n-1-i):
#         if mylist [j] > mylist [j+1]:
#             mylist [j], mylist [j + 1] = mylist [j + 1], mylist [j]
#
#
# print(mylist)

#Bubble Sort Optimization

# mylist = [54, 34, 25, 12, 22, 11, 90, 5]
#
# n =len(mylist)
# for i in range(n-1):
#     swapped = False
#     for j in range (n-1-i):
#         if mylist[j] > mylist[j + 1]:
#             mylist [j], mylist [j + 1] = mylist [j + 1], mylist [j]
#             swapped = True
#     if not swapped:
#         break
# print(mylist)

