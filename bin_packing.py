"""
Experiment 9: Efficient Bin Packing using Approximation Algorithm

Bin Packing is NP-Hard, so we use approximation (heuristic) algorithms:

1. Next Fit           : O(n)          -- simplest, weakest packing
2. First Fit          : O(n^2)        -- checks all open bins in order
3. Best Fit           : O(n^2)        -- places item in the tightest-fitting bin
4. First Fit Decreasing (FFD): O(n log n + n^2) -- sorts items first,
                                        gives a 11/9 * OPT + 1 approximation
                                        guarantee (better than plain First Fit)
"""

import random


def next_fit(items, capacity):
    bins = [0]
    for item in items:
        if bins[-1] + item <= capacity:
            bins[-1] += item
        else:
            bins.append(item)
    return bins


def first_fit(items, capacity):
    bins = []
    for item in items:
        placed = False
        for i in range(len(bins)):
            if bins[i] + item <= capacity:
                bins[i] += item
                placed = True
                break
        if not placed:
            bins.append(item)
    return bins


def best_fit(items, capacity):
    bins = []
    for item in items:
        best_idx = -1
        best_remaining = capacity + 1
        for i in range(len(bins)):
            remaining = capacity - bins[i]
            if remaining >= item and remaining < best_remaining:
                best_remaining = remaining
                best_idx = i
        if best_idx != -1:
            bins[best_idx] += item
        else:
            bins.append(item)
    return bins


def first_fit_decreasing(items, capacity):
    sorted_items = sorted(items, reverse=True)
    return first_fit(sorted_items, capacity)


if __name__ == "__main__":
    capacity = 10
    items = [random.randint(1, 8) for _ in range(15)]

    print(f"Bin capacity: {capacity}")
    print(f"Items: {items}\n")

    for name, fn in [
        ("Next Fit", next_fit),
        ("First Fit", first_fit),
        ("Best Fit", best_fit),
        ("First Fit Decreasing", first_fit_decreasing),
    ]:
        bins = fn(items, capacity)
        print(f"{name:22s} -> Bins used: {len(bins):2d}  |  Fill levels: {bins}")
