"""
Experiment 1: Implementation and Performance Analysis of Interpolation Search

Interpolation Search improves on Binary Search for uniformly distributed,
sorted data by estimating the probable position of the target using the
formula:

    pos = low + ((target - arr[low]) * (high - low)) / (arr[high] - arr[low])

Time Complexity : O(log log n) average case (uniform data), O(n) worst case
Space Complexity: O(1)
"""

import random
import time


def interpolation_search(arr, target):
    """Returns index of target in arr, or -1 if not found. Also returns comparisons made."""
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1
        if arr[low] == arr[high]:
            if arr[low] == target:
                return low, comparisons
            break

        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1, comparisons


def binary_search(arr, target):
    """Standard binary search for comparison purposes."""
    low, high = 0, len(arr) - 1
    comparisons = 0
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons


def performance_analysis():
    sizes = [1000, 10000, 100000, 1000000]
    print(f"{'n':>10} | {'IS time(s)':>12} | {'IS comps':>10} | {'BS time(s)':>12} | {'BS comps':>10}")
    print("-" * 65)

    for n in sizes:
        arr = sorted(random.sample(range(n * 10), n))
        target = arr[random.randint(0, n - 1)]

        start = time.perf_counter()
        _, is_comp = interpolation_search(arr, target)
        is_time = time.perf_counter() - start

        start = time.perf_counter()
        _, bs_comp = binary_search(arr, target)
        bs_time = time.perf_counter() - start

        print(f"{n:>10} | {is_time:>12.8f} | {is_comp:>10} | {bs_time:>12.8f} | {bs_comp:>10}")


if __name__ == "__main__":
    arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    target = 33
    idx, comps = interpolation_search(arr, target)
    print(f"Sample array: {arr}")
    print(f"Searching for {target} -> Found at index {idx} using {comps} comparisons\n")

    print("Performance Analysis: Interpolation Search vs Binary Search")
    performance_analysis()
