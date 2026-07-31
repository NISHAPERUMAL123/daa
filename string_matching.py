"""
Experiment 2: Comparative Analysis of Naive, Rabin-Karp, and KMP Algorithms
for String Matching

Naive        : O(n*m)  worst case, O(1) space
Rabin-Karp   : O(n+m)  average case (uses rolling hash), O(n*m) worst case
KMP          : O(n+m)  worst case guaranteed, O(m) space (LPS array)
"""

import random
import string
import time


def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    positions = []
    comparisons = 0
    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            positions.append(i)
    return positions, comparisons


def rabin_karp_search(text, pattern, prime=101):
    n, m = len(text), len(pattern)
    if m > n:
        return [], 0

    base = 256
    positions = []
    comparisons = 0

    pattern_hash = 0
    text_hash = 0
    h = 1

    for i in range(m - 1):
        h = (h * base) % prime

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            match = True
            for j in range(m):
                comparisons += 1
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                positions.append(i)

        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime

    return positions, comparisons


def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    return lps


def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return [], 0

    lps = compute_lps(pattern)
    positions = []
    comparisons = 0
    i = j = 0

    while i < n:
        comparisons += 1
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                positions.append(i - j)
                j = lps[j - 1]
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

    return positions, comparisons


def performance_analysis():
    sizes = [1000, 10000, 100000]
    pattern = "ABABCABAB"

    print(f"{'n':>10} | {'Naive t(s)':>11} | {'RK t(s)':>11} | {'KMP t(s)':>11}")
    print("-" * 55)

    for n in sizes:
        text = "".join(random.choices(string.ascii_uppercase[:3], k=n)) + pattern

        start = time.perf_counter()
        naive_search(text, pattern)
        t_naive = time.perf_counter() - start

        start = time.perf_counter()
        rabin_karp_search(text, pattern)
        t_rk = time.perf_counter() - start

        start = time.perf_counter()
        kmp_search(text, pattern)
        t_kmp = time.perf_counter() - start

        print(f"{n:>10} | {t_naive:>11.6f} | {t_rk:>11.6f} | {t_kmp:>11.6f}")


if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"

    print(f"Text: {text}")
    print(f"Pattern: {pattern}\n")

    for name, fn in [("Naive", naive_search), ("Rabin-Karp", rabin_karp_search), ("KMP", kmp_search)]:
        positions, comps = fn(text, pattern)
        print(f"{name:10s} -> Found at {positions}, comparisons: {comps}")

    print("\nPerformance Analysis")
    performance_analysis()
