# Challenge 28: Distance between the first 100 prime numbers
# def prime (num):
#     prime_num = []
#     start = 2
#     while len (prime_num) < num:
#         is_prime = True
#         for i in range (2, int(start**0.5) + 1):
#             if start % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#                 prime_num.append(start)
#         start += 1
#     distances = []
#     for i in range(len(prime_num) - 1):
#         distances.append(prime_num[i + 1] - prime_num[i])
#     return prime_num, distances
#
#
# print("The first 10 prime numbers are: ")
# primes, distances = prime(10)
# print("Primes:", primes)
# print("Distances:", distances)


# def two_sum (nums, target):
#     lookup = {}
#     for i, num in enumerate(nums):
#         if target - num in lookup:
#             return [lookup[target - num],i]
#         lookup[num] = i
# print(two_sum([2,7,11,15], 9))

