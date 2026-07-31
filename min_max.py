"""
Experiment 5: To Find Min-Max Value by Applying Divide and Conquer Technique

The array is recursively split in half. Each half returns its own (min, max)
pair, and the results are combined by comparing the mins and maxes.

Time Complexity: O(n)         -- but with ~ (3n/2) comparisons vs 2n for
                                  the naive linear scan
Space Complexity: O(log n)     -- recursion stack
"""

import random


def min_max_divide_conquer(arr, low, high):
    """Returns (min, max) tuple. Also counts comparisons via a mutable list."""
    # Base case: single element
    if low == high:
        return arr[low], arr[low]

    # Base case: two elements
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide
    mid = (low + high) // 2
    min1, max1 = min_max_divide_conquer(arr, low, mid)
    min2, max2 = min_max_divide_conquer(arr, mid + 1, high)

    # Combine
    return min(min1, min2), max(max1, max2)


def min_max_naive(arr):
    """Linear scan for comparison."""
    curr_min = curr_max = arr[0]
    for x in arr[1:]:
        if x < curr_min:
            curr_min = x
        if x > curr_max:
            curr_max = x
    return curr_min, curr_max


if __name__ == "__main__":
    arr = [random.randint(1, 1000) for _ in range(15)]
    print(f"Array: {arr}\n")

    dc_min, dc_max = min_max_divide_conquer(arr, 0, len(arr) - 1)
    print(f"Divide & Conquer -> Min: {dc_min}, Max: {dc_max}")

    naive_min, naive_max = min_max_naive(arr)
    print(f"Naive Linear Scan -> Min: {naive_min}, Max: {naive_max}")

    assert (dc_min, dc_max) == (naive_min, naive_max), "Mismatch!"
    print("\nBoth methods agree. Divide & Conquer uses ~3n/2 comparisons vs 2n for naive.")
