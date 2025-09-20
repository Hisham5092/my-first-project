# Minimum value in an array

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
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(my_array)

for i in range (n):
    min_index = i # 0 index which is 64
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]: 
            min_index = j
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]
print("Sorted array:", my_array)