# Two Sum
#Brute Force
# nums = [2,3,4]
# target = 6
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         sum = nums[i] + nums[j]
#         if sum == target:
#             print([i, j])
from time import process_time_ns

# 2 Sum Hashmap
# nums = [2,3,4]
# target = 6
# num_map = {}
# for i,j in enumerate(nums):
#     diff = target - j
#     if diff in num_map:
#         print([num_map[diff], i])
#     num_map[j] = i

# Palindrome Number
# import time
# start_time = time.perf_counter()
# x = 212
# value = list(str(x))
# n = len(value)
# second = []
#
# for j in range(n - 1, -1, -1):
#     second.append(value[j])
#
# if value == second:
#     print("Palindrome found")
# else:
#     print("Not Palindrome")
#
# end_time = time.perf_counter()
# print(f"Execution time: {end_time - start_time:.6f} seconds")

# import time
#
# start_time = time.perf_counter()
# x = 212
# value = str(x)
#
# if value == value[::-1]:
#     print("Palindrome found")
# else:
#     print("Not Palindrome")
#
# end_time = time.perf_counter()
# print(f"Execution time: {end_time - start_time:.6f} seconds")

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         value = list(str(x))
#         if value == value [::-1]:
#             print("Palindrome found")
#             return True
#         else:
#             print("Palindrome Not found")
#             return False
#
# solu = Solution()
# palindrome = solu.isPalindrome(int(123))


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         # Negative numbers and numbers ending in 0 (except 0 itself) aren't palindromes
#         if x < 0 or (x % 10 == 0 and x != 0):
#             return False
#
#         reversed_half = 0
#         while x > reversed_half:
#             reversed_half = reversed_half * 10 + x % 10
#             x //= 10
#
#         # For odd length: x == reversed_half // 10
#         # For even length: x == reversed_half
#         return x == reversed_half or x == reversed_half // 10

# Roman to Integers
# import time
# start_time = time.perf_counter()
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000,
#         }
#         totals = 0
#         previous = 0
#         n = len(s)
#         for i in range(n - 1, -1, -1):
#             char = s[i]
#             current = roman[char]
#             if current < previous:
#                 totals = totals - current
#             else:
#                 totals = totals + current
#             previous = current
#         return totals
# end_time = time.perf_counter()
# print(f"Execution time: {end_time - start_time:.6f} seconds")

# import time
# start_time = time.perf_counter()
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman = {
#             "I": 1, "V": 5, "X": 10, "L": 50,
#             "C": 100, "D": 500, "M": 1000
#         }
#
#         total = 0
#         n = len(s)
#         for i in range(n):
#             if i < n - 1 and roman[s[i]] < roman[s[i + 1]]:
#                 total = total - roman[s[i]]
#
#             else:
#                 total = total + roman[s[i]]
#
#         return total
#
# sol = Solution()
# print(sol.romanToInt("V"))
# end_time = time.perf_counter()
# print(f"Execution time: {end_time - start_time:.6f} seconds")

# Longest Common Prefix
# words =["flower", "flow", "flock"]
# prefix =''
# for i in range(len(words[0])):
#     char = words[0][i]
#     for word in words:
#         if i >= len(word):
#             print(prefix)
#             exit()
#         if word[i] != char:
#             print(prefix)
#             exit()
#
#     prefix = prefix + char
#
# print(prefix)

# Valid Parentheses

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []  # ← Create a separate stack!
#         opening = ['(', '[', '{']
#         closing = [')', ']', '}']
#         matches = {
#             ')': '(',
#             ']': '[',
#             '}': '{'
#         }
#         for char in s:  # Loop through the string
#             if char in opening:
#                 stack.append(char)  # ✓ Append to stack
#
#             elif char in closing:
#                 if not stack:  # ✓ Check if stack is empty
#                     return False
#
#                 if stack[-1] == matches[char]:  # ✓ Check stack's top
#                     stack.pop()  # ✓ Pop from stack
#                 else:
#                     return False
#
#         return len(stack) == 0  # ✓ True if stack is empty

# Binary Tree Pre Order

# class Solution:
#     def preOrderTraversal(self, root):
#         result=[]
#         def preOrder(node):
#             if node is None:
#                 return
#             result.append(node.value)
#             preOrder(node.left)
#             preOrder(node.right)
#
#         preOrder(root)
#         return result


# Merge Two Sorted List

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         # Create a dummy node to make things easier
#         dummy = ListNode(0)
#         current = dummy
#
#         # While both lists have nodes
#         while list1 and list2:
#             if list1.val <= list2.val:
#                 current.next = list1  # Attach list1's node
#                 list1 = list1.next  # Move list1 forward
#             else:
#                 current.next = list2  # Attach list2's node
#                 list2 = list2.next  # Move list2 forward
#
#             current = current.next  # Move current forward
#
#         # Attach remaining nodes (one list is empty, one might have nodes left)
#         if list1:
#             current.next = list1
#         if list2:
#             current.next = list2
#
#         # Return the head (skip dummy node)
#         return dummy.next


# Remove Elements From Sorted Array

# def remove(arr):
#     n = len(arr)
#     k = 0
#     for i in range(1,n):
#         if arr[i] != arr[i-1]:
#             k = k + 1
#             arr[k] = arr[i]
#         else:
#             continue
#     return k + 1
#
# arr1 = [1,1,2,3,3,4,5]
# result = remove(arr1)
# print(result)
# print(arr1[:result])

# Remove Element
# def remove(arr, value):
#     k = 0
#     n = len(arr)
#     for i in range(n):
#         if arr[i] != value:
#             arr[k] = arr[i]
#             k = k + 1
#     while len(arr) > k:
#         arr.pop()
#     return k
#
# arr1 = [1,1,2,3,3,4,5]
# result = remove(arr1,3)
# print(result)

# Find The Index of The First Occurrence in A String

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if not needle:
#             return 0
#         for i in range(len(haystack) - len(needle) + 1):
#             substring = haystack[i: i + len(needle)]
#
#             if substring == needle:
#                 print(f"found at index {i}")
#                 return i
#         return -1
#
# sol = Solution()
# result = sol.strStr("sadbutsad", "sad")

# Search Insert Position

# def find(arr, target):
#
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right:
#
#         mid = (left + right) // 2
#
#         if target == arr[mid]:
#             return mid
#
#         if target < arr[mid]:
#             right = mid - 1
#
#         else:
#             left = mid + 1
#
#     return -1
#
# myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# myTarget = 15
#
# result = find(myArray, myTarget)
#
# if result != 1:
#     print("Found", result)
# else:
#     print("Not found")

# Length of Last Word
#
# s = "Hello World"
#
# words = s.rsplit(maxsplit=1)
# print(words)

# def lengthOfLastWord(s):
#     count = 0
#     i = len(s) - 1
#
#     while i >= 0 and s[i] == " ":
#         i = i - 1
#
#     while i >= 0 and s[i] != " ":
#         count = count + 1
#         i = i - 1
#
#     return count
#
# result = lengthOfLastWord('Hello Doug')
# print(result)


# Plus One

class Solution:
    def plusOne(self, digits):

        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits

sol = Solution()
arr = [1,9,9]
result = sol.plusOne(arr)
print(result)


