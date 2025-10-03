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


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (except 0 itself) aren't palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For odd length: x == reversed_half // 10
        # For even length: x == reversed_half
        return x == reversed_half or x == reversed_half // 10