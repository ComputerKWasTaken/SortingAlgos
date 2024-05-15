import matplotlib.pyplot as plt
from typing import List

MIN_MERGE = 32

def calc_min_run(n):
    """Returns the minimum length of a run from 23 - 64 so that
    the array of n elements can be divided into an array of runs
    with length of at most a power of 2.
    """
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

def insertion_sort(arr: List[int], left: int, right: int, ax, passNum):
    """A simple insertion sort function for sorting a range in the array."""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        visualize(arr, passNum, j + 1, i, ax)
        passNum += 1
    return passNum

def merge(arr: List[int], l: int, m: int, r: int, ax, passNum):
    """Merge function to merge sorted runs."""
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(len1):
        left.append(arr[l + i])
    for i in range(len2):
        right.append(arr[m + 1 + i])
    
    i = j = 0
    k = l
    
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        visualize(arr, passNum, k, k, ax)
        k += 1
        passNum += 1
    
    while i < len1:
        arr[k] = left[i]
        i += 1
        k += 1
        visualize(arr, passNum, k - 1, k - 1, ax)
        passNum += 1
    
    while j < len2:
        arr[k] = right[j]
        j += 1
        k += 1
        visualize(arr, passNum, k - 1, k - 1, ax)
        passNum += 1
    
    return passNum

def timSort(arr: List[int], ax=None):
    """Implements the Tim Sort algorithm with visualization."""
    n = len(arr)
    min_run = calc_min_run(n)
    passNum = 0

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        passNum = insertion_sort(arr, start, end, ax, passNum)
    
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                passNum = merge(arr, left, mid, right, ax, passNum)
        
        size = 2 * size

def visualize(arr: List[int], passNum: int, swapIndex: int, selectedIndex: int, ax):
    """Updates the matplotlib bar graph for visualization."""
    ax.clear()
    barColors = ['blue'] * len(arr)
    barColors[selectedIndex] = 'orange'
    
    ax.bar(range(len(arr)), arr, color=barColors)
    ax.set_title(f'Tim Sort Pass: {passNum}, Swap Index: {swapIndex}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    
    plt.pause(0.01)  # Minimal pause to update the visualization
