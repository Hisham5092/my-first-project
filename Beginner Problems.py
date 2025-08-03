# Print Numbers from 1 to 10
# for i in range(10):
#     print(i+1)
from heapq import merge
from shlex import split

# Print Odd Numbers Less Than 100
# for i in range(100):
#     if i % 2 == 1:
#         print(i)

# Print Multiplication Table with 7

# for i in range(10):
#     print(7 * (i+1))

# Print All Multiplication Tables (1 to 10)

# for i in range(10):
#     print(f"Multiplication Table for {i+1}")
#     for j in range(10):
#         multiply = (i + 1) * (j + 1)
#         print(f"{i+1} × {j+1} = {multiply}")
#     print()

# Calculate Sum of Numbers from 1 to 10
# sum = 0
# for i in range(1,11):
#     sum = sum + i
# print(sum)

# Challenge 6: Calculate 10!

# def factorial(n):
#     # number = n * (n - 1) * (n - 2) * (n - 3) * (n - 4)
#     if n == 1:
#         return 1
#     return n * factorial (n - 1)
# result = factorial(5)
# print(result)

# Challenge 7: Sum of Odd Numbers (10 to 30)
# sum = 0
# for i in range(10,30):
#     if i % 2 == 1:
#         sum = sum + i
# print(sum)

# Challenge 8: Celsius to Fahrenheit Conversion

# (1°C × 9/5) + 32 = 33.8°F
# print("Input your temperature in celsius:", end="")
# number = int(input())
# temperature =  (number * 9/5) +32
# print(f"The temperature in farenheit is: {temperature}")

# Challenge 9: Fahrenheit to Celsius Conversion

#(fahrenheit - 32) * 5/9

# print("Input your temperature in farenheit:", end="")
# number = int(input())
# temperature =  (number - 32) * 5/9
# print(f"The temperature in celsius is: {temperature}")

# Challenge 10: Sum of Numbers in an Array

# number = [2,4,5,7,11]
# sum = 0
# for i in number:
#     sum = sum + i
# print(sum)

# Challenge 11: Average of Numbers in an Array

# number = [2,4,5,7,11]
# sum = 0
# for i in number:
#     sum = sum + i
# average = sum / len(number)
# print(average)
# average = sum(number) / len(number)
# print(average)

# Challenge 12: Positive Numbers in an Array (Solution 1)

# number = [2,4,-6,7,11,5]
# for i in number:
#     if i>0:
#         print(i)
#     else:
#         continue
#         # print("Negative number detected")

# numbers = list(map(int, input("Input the numbers with space:").split()))
# for i in numbers:
#     if i>0:
#         print(i)
#     else:
#         continue

# Challenge 13: Maximum number in an array

# number = [2,4,-6,7,11,5]
# x = max(number)
# print(x)

# Challenge 14: First 10 Fibonacci numbers without recursion
# fibo =[0,1]
# for i in range(8):
#     fibo.append(fibo[i]+fibo[i+1])
# print(fibo)

# Challenge 15: nth Fibonacci number using recursion
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# result = fibonacci(10)
# print(result)

# Challenge 16: Check if a number is prime

# for i in range(1,11):
#     if i>1:
#         is_prime = True
#         for j in range(2,i):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(i)

# def is_prime(n):
#     if n < 2:  # 0 and 1 are not prime numbers
#         return False
#     for i in range(2, int(n**0.5) + 1):  # Check divisibility up to √n
#         if n % i == 0:
#             return False  # If divisible, it's not prime
#     return True  # If not divisible by any, it's prime
#
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

# Challenge 17: Sum of digits of a positive integer

# num = list(map(int, input("Enter a number: ")))
# sum = 0
# for i in num:
#     sum = sum + i
# print(sum)
#
#
# num = input("Enter a number: ")
# sum_of_digits = sum(map(int, num))
# print(sum_of_digits)

# Challenge 18: First 100 prime numbers

# for i in range(1,100):
#     if i > 1:
#         is_prime = True
#         for j in range(2,i):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(i)

# Challenge 19: First "nPrimes" prime numbers greater than "startAt"

# prime =[]
# for i in range(10,30):
#     if i > 1:
#         is_prime = True
#         for j in range (2,i):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(i)
#             prime.append(i)
#             if len(prime) == 5:
#                 break


# def prime(n_primes, start_at):
#     primes = []
#     num = start_at + 1
#     while len(primes) < n_primes:
#         is_prime = True
#         for i in range(2, int(num**0.5)+1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
#         num = num + 1
#     return primes
#
# print(prime(5, 10))


# def print_primes_in_range(start, end):
#     """Print all prime numbers from start to end (inclusive)"""
#     for i in range(start, end + 1):
#         if i < 2:  # Numbers less than 2 are not prime
#             continue
#
#         is_prime = True
#         # Check if i is divisible by any number from 2 to sqrt(i)
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 is_prime = False
#                 break
#
#         if is_prime:
#             print(i)
# # Usage examples
# print("Prime numbers from 5 to 30:")
# print_primes_in_range(5, 30)

# def get_primes_in_range(start, end):
#     """Return a list of prime numbers from start to end (inclusive)"""
#     primes = []
#     for i in range(start, end + 1):
#         if i < 2:  # Numbers less than 2 are not prime
#             continue
#
#         is_prime = True
#         # Check if i is divisible by any number from 2 to sqrt(i)
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 is_prime = False
#                 break
#
#         if is_prime:
#             primes.append(i)
#     return primes
# print("\nPrimes as a list:")
# prime_list = get_primes_in_range(5, 30)
# print(prime_list)



# Challenge 20: Rotate an array to the left 1 position

# def rotate_left(arr):
#     if not arr:  # Handle empty array case
#         return []
#     return arr[1:] + [arr[0]]  # Shift all elements left and move the first element to the end
#
# # Example usage:
# arr = [1, 2, 3, 4, 5]
# print(rotate_left(arr))

# def rotate_left_inplace(arr):
#     if not arr:
#         return arr  # Return empty list if input is empty
#
#     first = arr.pop(0)  # Remove first element
#     arr.append(first)  # Append it to the end
#
#
# # Example usage:
# arr = [1, 2, 3, 4, 5]
# rotate_left_inplace(arr)
# print(arr)  # Output: [2, 3, 4, 5, 1]


# from collections import deque
#
# def rotate_left_deque(arr):
#     dq = deque(arr)
#     dq.rotate(-1)  # Rotate left by 1
#     return list(dq)
#
# # Example usage:
# arr = [1, 2, 3, 4, 5]
# print(rotate_left_deque(arr))

# Challenge 21: Rotate an array to the right 1 position

# def rotate_right(arr):
#     if not arr:
#         return []
#     return [arr[4]] + arr[:-1]
#
# arr = [1, 2, 3, 4, 5]
# arr = rotate_right(arr)
# print(arr)

# def rotate_right(arr):
#     if not arr:
#         return []
#     last = arr.pop(4)
#     arr.insert(0,last)
#
# arr = [1, 2, 3, 4, 5]
# rotate_right(arr)
# print(arr)

# from collections import deque
# def rotate_right(arr):
#     dq = deque(arr)
#     dq.rotate(1)
#     return list(dq)
# arr = [1, 2, 3, 4, 5]
# print(rotate_right(arr))

#Challenge 22: Reverse an array

# arr = [1,2,3,4,5]
#
# reversed_arr = arr[::-1]
# print(reversed_arr)

# arr = [1, 2, 3, 4, 5]
# arr.reverse()
# print(arr)

# arr = [1, 2, 3, 4, 5]
# reversed_arr = list(reversed(arr))
# print(reversed_arr)

# arr = [1, 2, 3, 4, 5]
# reversed_arr = []
# for i in range(len(arr) - 1, -1, -1):
#     reversed_arr.append(arr[i])
# print(reversed_arr)

# arr = [1, 2, 3, 4, 5]
# reverse_arr = sorted(arr, reverse = True)
# print(reverse_arr)

#Challenge 23: Reverse a string

# a = input("Enter a string:")
# reverse_str = a[::-1]
# print(reverse_str)

# s = input("Enter a string: ")
# reversed_s = ''.join(reversed(s))
# print("Reversed string:", reversed_s)

# Challenge 24: Merge two arrays
# arr_1 = [1,2,3]
# arr_2 = [4,5,6]
# arr_3 = arr_1 + arr_2
# print(arr_3)

# arr_1 = [1,2,3]
# arr_2 = [4,5,6]
# arr_1.extend(arr_2)
# print(arr_1)

# Challenge 25: Elements in the first or second array but not both
# arr1 = [1, 2, 3, 4]
# arr2 = [3, 4, 5, 6]
#
# result = list(set(arr1).symmetric_difference(set(arr2)))
# print("Elements in one array but not both:", result)

# arr1 = [1, 2, 3, 4]
# arr2 = [3, 4, 5, 6]
#
# result = list(set(arr1) ^ set(arr2))
# print("Elements in one array but not both:", result)

# arr1 = [1, 2, 3, 4]
# arr2 = [3, 4, 5, 6]
#
# result = [x for x in arr1 if x not in arr2] + [y for y in arr2 if y not in arr1]
# print("Elements in one array but not both:", result)

# Challenge 26: Elements in the first array but not in the second

# arr1 = [1, 2, 3, 4]
# arr2 = [3, 4, 5, 6]
#
# result = list(set(arr1).difference(set(arr2)))
# print(result)

# Challenge 27: Distinct elements in an array
# arr = [1, 2, 3, 2, 4, 1, 5, 3]
# distinct = list(set(arr))
# print(distinct)

# arr = [1, 2, 3, 2, 4, 1, 5, 3]
# distinct_elements = []
#
# for num in arr:
#     if num not in distinct_elements:
#         distinct_elements.append(num)
#
# print("Distinct elements:", distinct_elements)

# Challenge 28: Distance between the first 100 prime numbers

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# primes = []
# num = 2

# Generate the first 100 prime numbers
# while len(primes) < 100:
#     if is_prime(num):
#         primes.append(num)
#     num += 1
#
# # Calculate the distance between consecutive primes
# # distances = [primes[i+1] - primes[i] for i in range(len(primes) - 1)]
# distances =[]
# for i in range(len(primes) - 1):
#     distances.append(primes[i+1] - primes[i])
#
# print("First 100 prime numbers:")
# print(primes)
# print("\nDistances between consecutive primes:")
# print(distances)

# Challenge 29: Add two positive numbers of indefinite size as strings

# def add_large_numbers(num1, num2):
#     # Reverse the strings to make addition easier
#     num1 = num1[::-1]
#     num2 = num2[::-1]
#
#     carry = 0
#     result = []
#
#     # Loop through the digits
#     max_length = max(len(num1), len(num2))
#     for i in range(max_length):
#         digit1 = int(num1[i]) if i < len(num1) else 0
#         digit2 = int(num2[i]) if i < len(num2) else 0
#
#         # Add the digits and the carry
#         total = digit1 + digit2 + carry
#         carry = total // 10  # Calculate the new carry
#         result.append(str(total % 10))  # Add the digit to the result
#
#     # If there is a leftover carry, add it
#     if carry:
#         result.append(str(carry))
#
#     # Reverse the result and join to form the final number
#     return ''.join(result[::-1])

# # Example Usage
# num1 = input("Enter the first large number: ")
# num2 = input("Enter the second large number: ")
# print("Sum:", add_large_numbers(num1, num2))

# Challenge 30: Number of words in a text

# var = input("Enter a text:") #Counting characters
# count = 0
# for i in var:
#     count = count + len(i)
# print(count)

# var = input("Enter a text: ")
# words = var.split()  # Split by spaces to get a list of words
# count = len(words)  # Count the number of words
# print(count)
# print(words)

# Challenge 31: Capitalize the first letter of each word in a text

# text = input("Enter a text: ")
# capitalized_text = text.title()  # Capitalizes the first letter of each word
# print(capitalized_text)
#
#
# text = input("Enter a text: ")
# words = text.split()  # Split the text into words
# capitalized_words = [word.capitalize() for word in words]  # Capitalize each word
# capitalized_text = ' '.join(capitalized_words)  # Join them back into a single string
# print(capitalized_text)

# txt = input("Enter a text:")
# words = txt.split()
# capitalized_words =[]
# for word in words:
#     capita = word.capitalize()
#     capita_txt= capitalized_words.append(capita)
# final_one = ' '.join(capitalized_words)
# print(final_one)

# Challenge 32: Sum of numbers in a comma-delimited string

# num = input("Enter numbers separated by comma:")
# arr = list(map(int, num.split(',')))
# total = sum(arr)
# print(total)

# Challenge 33: Words inside a text

# txt = input("Enter a text:")
# words = txt.split()
#
# for word in words:
#     print(word)

# # Challenge 34: Convert CSV text to a bi-dimensional array
# csv_text = input("Enter CSV text: ")
# rows = csv_text.split('\n')  # Split by new lines
# array = []
#
# for row in rows:
#     columns = row.split(',')  # Split each row by commas
#     array.append(columns)  # Add the list of columns to the array
#
# print("Bi-dimensional array:")
# for row in array:
#     print(row)

# Challenge 35: Convert a string to an array of characters

# str = "Hisham"
# arr =[]
# for chr in str:
#     arr.append(chr)
# print(arr)

#Challenge 36: Convert an array of ASCII codes to a string
# ascii_codes = [72, 101, 108, 108, 111]  # This represents "Hello"
# result = ""
#
# for code in ascii_codes:
#     result += chr(code)  # Convert each ASCII code to character and add to result
#
# print("Converted string:", result)

# Challenge 37: Implement the Caesar cipher
# def caesar_cipher(text, shift):
#     result = ""
#
#     for char in text:
#         if char.isalpha():  # Only shift letters
#             offset = 65 if char.isupper() else 97  # ASCII for A or a
#             shifted = (ord(char) - offset + shift) % 26 + offset
#             result += chr(shifted)
#         else:
#             result += char  # Keep punctuation, space, numbers unchanged
#
#     return result

# Example
# text = input("Enter a message: ")
# shift = int(input("Enter shift amount: "))
# encrypted = caesar_cipher(text, shift)
# print("Encrypted text:", encrypted)

# Challenge 38: Bubble sort algorithm

# arr = [4, 2, 3, 6, 1]
#
# n = len(arr)
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if arr[j] > arr[j + 1]:  # descending order
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
# print(arr)
# def bubble_sort(arr):
#     n = len(arr)
#
#     for i in range(n):
#         # Last i elements are already in place
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 # Swap if the element is greater than the next
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#     return arr
# nums = [5, 1, 4, 2, 8]
# sorted_nums = bubble_sort(nums)
# print("Sorted list:", sorted_nums)

# Challenge 39: Distance between two points defined by their coordinates
# import math
#
# # Input: coordinates of two points
# x1, y1 = map(float, input("Enter x1 and y1: ").split())
# x2, y2 = map(float, input("Enter x2 and y2: ").split())
#
# # Calculate distance using Euclidean formula
# distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#
# # Output the result
# print(f"Distance between the points: {distance:.2f}")

# Challenge 40: Check Circle Intersection
# import math
#
# def check_circle_intersection(x1, y1, r1, x2, y2, r2):
#     distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#
#     if distance > r1 + r2:
#         return "No intersection"
#     elif distance == r1 + r2 or distance == abs(r1 - r2):
#         return "Touching"
#     else:
#         return "Intersecting"
#
# # Example usage
# print(check_circle_intersection(0, 0, 5, 8, 0, 3))  # Outputs: "Touching"

# Challenge 41: Extract Column from 2D Array

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# column_index = 1  # 0-based indexing: 0 is first column, 1 is second
#
# column = []
# for row in matrix:
#     column.append(row[column_index])
#
# print("Extracted column:", column)

# Challenge 42: Convert Binary String to Decimal Number
# binary_string = input("Enter a binary number: ")
#
# # Convert binary string to integer
# decimal_number = int(binary_string, 2)
# print("Decimal equivalent:", decimal_number)

# def binary_to_decimal(binary_str):
#     if binary_str.startswith('-'):
#         return -int(binary_str[1:], 2)
#     return int(binary_str, 2)
#
# # Example usage
# binary_input = input("Enter a binary number (can be negative): ")
# decimal_output = binary_to_decimal(binary_input)
# print("Decimal equivalent:", decimal_output)

# Challenge 43: Convert Decimal Number to Binary String

# decimal = int(input("Enter a decimal number:"))
#
# binary = bin(decimal) [2:]
#
# print("Binary equivalent:", binary)

# Challenge 44: Sum of Numbers in Jagged Array
# jagged_array = [
#     [1, 2, 3],
#     [4, 5],
#     [6],
#     [7, 8, 9, 10]
# ]
#
# total_sum = 0
# for sublist in jagged_array:
#     for num in sublist:
#         total_sum += num
#
# print("Total sum:", total_sum)

# Challenge 45: Find Maximum Number in Jagged Array
# jagged_array = [
#     [1, 2, 3],
#     [10, 5],
#     [6],
#     [7, 8, 9, 0]
# ]
#
# # Start with a very small number as the initial max
# maximum = float('-inf')  # Represents negative infinity
#
# for sublist in jagged_array:
#     for num in sublist:
#         if num > maximum:
#             maximum = num
#
# print("Maximum number:", maximum)

# Star pyramid

# rows = int(input("Enter the number of rows: "))
#
# for i in range(1, rows + 1):
#     # Print spaces
#     for space in range(rows - i):
#         print(" ", end="")
#
#     # Print stars
#     for star in range(2 * i - 1):
#         print("*", end="")
#
#     print()  # Move to next line

# Star pyramid v2
# rows = int(input("Enter the number of rows: "))
#
# for i in range(1, rows + 1):
#     # Print spaces
#     for space in range(rows - i):
#         print(" ", end="")
#
#     # Print stars
#     for star in range(i):
#         print("* ", end="")
#
#     print()  # Move to next line

# Reverse pyramid v1

# rows = int(input("Enter the number of rows: "))
#
# for i in range(1, rows + 1):
#     for star in range(rows + 1 - i):
#         print("* ", end="")
#     print()
#     for space in range(0,i):
#         print(" ", end="")


# Reverse pyramid v2
# rows = int(input("Enter the number of rows: "))
#
# for i in range(rows, 0, -1):   # Start from rows, down to 1
#     for space in range(rows - i):
#         print(" ", end="")
#
#     for star in range(i):
#         print("* ", end="")  # Star with space
#     print()
