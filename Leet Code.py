# Two Sum
#Brute Force
# nums = [2,3,4]
# target = 6
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         sum = nums[i] + nums[j]
#         if sum == target:
#             print([i, j])

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

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # ← Create a separate stack!
        opening = ['(', '[', '{']
        closing = [')', ']', '}']
        matches = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:  # Loop through the string
            if char in opening:
                stack.append(char)  # ✓ Append to stack

            elif char in closing:
                if not stack:  # ✓ Check if stack is empty
                    return False

                if stack[-1] == matches[char]:  # ✓ Check stack's top
                    stack.pop()  # ✓ Pop from stack
                else:
                    return False

        return len(stack) == 0  # ✓ True if stack is empty