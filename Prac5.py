#Practical 5

import random
import time

def deterministic_quicksort(arr):
    if len(arr) <= 1:         
        return arr
    pivot = arr[len(arr) // 2] 
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quicksort(left) + middle + deterministic_quicksort(right)

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)

def analyze_sorting_algorithm(sort_function, array):
    start_time = time.time()
    sorted_array = sort_function(array)
    end_time = time.time()
    return sorted_array, end_time - start_time

test_array = [3, 2, 1, 5, 4, 8, 7, 6]
sorted_array_det, time_taken_det = analyze_sorting_algorithm(deterministic_quicksort, test_array)
sorted_array_rand, time_taken_rand = analyze_sorting_algorithm(randomized_quicksort, test_array)

print("Deterministic Quicksort:")
print("Sorted Array:", sorted_array_det)
print(f"Time taken: {time_taken_det:.6f} seconds")
print("\nRandomized Quicksort:")
print("Sorted Array:", sorted_array_rand)
print(f"Time taken: {time_taken_rand:.6f} seconds")

def generate_random_array(start, end, size):
  array = []
  for i in range(size):
    array.append(random.randint(start, end))
  return array
