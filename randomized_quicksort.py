"""
Experiment 10: Improving Quick Sort Efficiency using Randomized Algorithm

Standard Quick Sort degrades to O(n^2) on already-sorted or reverse-sorted
input when the pivot is always chosen as the first/last element.
Randomized Quick Sort picks a random pivot each time, making the O(n^2)
worst case extremely unlikely regardless of input order.

Time Complexity: O(n log n) expected, O(n^2) worst case (rare with randomization)
Space Complexity: O(log n) recursion stack
"""

import random
import time
import sys

sys.setrecursionlimit(10000)


def deterministic_quicksort(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high, high)  # always last element
        deterministic_quicksort(arr, low, pivot_idx - 1)
        deterministic_quicksort(arr, pivot_idx + 1, high)


def randomized_quicksort(arr, low, high):
    if low < high:
        rand_idx = random.randint(low, high)
        pivot_idx = partition(arr, low, high, rand_idx)
        randomized_quicksort(arr, low, pivot_idx - 1)
        randomized_quicksort(arr, pivot_idx + 1, high)


def partition(arr, low, high, pivot_choice_idx):
    arr[pivot_choice_idx], arr[high] = arr[high], arr[pivot_choice_idx]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def performance_analysis():
    sizes = [500, 1000, 2000]

    print(f"{'n':>8} | {'Input':>16} | {'Deterministic (s)':>18} | {'Randomized (s)':>15}")
    print("-" * 68)

    for n in sizes:
        for label, base in [("Random", list(range(n))), ("Sorted", list(range(n))), ("Reverse Sorted", list(range(n, 0, -1)))]:
            if label == "Random":
                data = base[:]
                random.shuffle(data)
            else:
                data = base[:]

            arr1 = data[:]
            start = time.perf_counter()
            deterministic_quicksort(arr1, 0, len(arr1) - 1)
            t_det = time.perf_counter() - start

            arr2 = data[:]
            start = time.perf_counter()
            randomized_quicksort(arr2, 0, len(arr2) - 1)
            t_rand = time.perf_counter() - start

            print(f"{n:>8} | {label:>16} | {t_det:>18.6f} | {t_rand:>15.6f}")


if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print(f"Original array: {arr}")
    randomized_quicksort(arr, 0, len(arr) - 1)
    print(f"Sorted array:   {arr}\n")

    print("Performance Analysis: Deterministic vs Randomized Quick Sort")
    print("(Note: on Sorted/Reverse Sorted input, deterministic quicksort")
    print(" is expected to be significantly slower due to O(n^2) worst case)\n")
    performance_analysis()
