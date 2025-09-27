# Minimum value in an array
from wsgiref.validate import header_re


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

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self. head = None
        self.size = 0

    def push(self,value):
        new_node = Node (value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        popped_value = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_value.value


    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.head.value


    def isEmpty(self):
        return self.size == 0
    def stack_size(self):
        return self.size

myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Pop: ", myStack.pop())
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stack_size())