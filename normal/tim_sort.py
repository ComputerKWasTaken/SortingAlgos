import matplotlib.pyplot as plt
from typing import List

MIN_MERGE = 32
MIN_GALLOP = 7  # Minimum number of consecutive wins before galloping mode

def calc_min_run(n: int) -> int:
    """Calculate minimum run length for efficient merging"""
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

def binary_insertion_sort(arr: List[int], left: int, right: int, ax=None, passNum: int = 0) -> int:
    """Optimized insertion sort using binary search"""
    for i in range(left + 1, right + 1):
        key = arr[i]
        
        # Binary search to find insertion point
        lo, hi = left, i
        while lo < hi:
            mid = (lo + hi) // 2
            if key < arr[mid]:
                hi = mid
            else:
                lo = mid + 1
                
        # Move elements to make space
        for j in range(i, lo, -1):
            arr[j] = arr[j - 1]
        arr[lo] = key
        
        if ax:
            visualize(arr, passNum, lo, i, ax)
            passNum += 1
            
    return passNum

def gallop_left(key: int, arr: List[int], start: int, length: int) -> int:
    """Find insertion point for key in arr[start:start+length] using galloping"""
    offset = 1
    lastOffset = 0
    
    if key <= arr[start]:
        return start
    
    maxOffset = length
    while offset < maxOffset and arr[start + offset] <= key:
        lastOffset = offset
        offset = (offset << 1) + 1
        
    if offset > maxOffset:
        offset = maxOffset
        
    # Binary search in the identified range
    left = start + lastOffset
    right = start + min(offset, length)
    while left < right:
        mid = (left + right) // 2
        if key <= arr[mid]:
            right = mid
        else:
            left = mid + 1
            
    return left

def merge_compute_minrun(length: int) -> int:
    """Compute ideal run length for array of given length"""
    min_run = calc_min_run(length)
    return min(max(MIN_MERGE, min_run), length)

def merge_lo(arr: List[int], left: List[int], right: List[int], start: int, ax=None, passNum: int = 0) -> int:
    """Optimized merge of two arrays with galloping mode"""
    len_left, len_right = len(left), len(right)
    i = j = 0
    k = start
    min_gallop = MIN_GALLOP
    
    while i < len_left and j < len_right:
        count_left = count_right = 0
        
        # Enter galloping mode if winning streak is long enough
        while (count_left | count_right) < min_gallop:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
                count_left += 1
                count_right = 0
                if i == len_left:
                    break
            else:
                arr[k] = right[j]
                j += 1
                count_right += 1
                count_left = 0
                if j == len_right:
                    break
            k += 1
            if ax:
                visualize(arr, passNum, k-1, k-1, ax)
                passNum += 1
                
        # If we're in galloping mode
        if (count_left | count_right) >= min_gallop:
            min_gallop -= 1  # Be more likely to enter galloping mode
            while i < len_left and j < len_right:
                # Gallop in left array
                pos = gallop_left(right[j], left, i, len_left - i)
                for x in range(i, pos):
                    arr[k] = left[x]
                    k += 1
                    if ax:
                        visualize(arr, passNum, k-1, k-1, ax)
                        passNum += 1
                i = pos
                if i == len_left:
                    break
                
                # Gallop in right array
                arr[k] = right[j]
                j += 1
                k += 1
                if j == len_right:
                    break
                if ax:
                    visualize(arr, passNum, k-1, k-1, ax)
                    passNum += 1
                    
            min_gallop = max(MIN_GALLOP, min_gallop + 2)  # Penalize if galloping wasn't helpful
            
    # Copy remaining elements
    while i < len_left:
        arr[k] = left[i]
        i += 1
        k += 1
        if ax:
            visualize(arr, passNum, k-1, k-1, ax)
            passNum += 1
            
    while j < len_right:
        arr[k] = right[j]
        j += 1
        k += 1
        if ax:
            visualize(arr, passNum, k-1, k-1, ax)
            passNum += 1
            
    return passNum

def timSort(arr: List[int], ax=None):
    """Optimized TimSort implementation"""
    if not arr:
        return arr
        
    n = len(arr)
    min_run = merge_compute_minrun(n)
    passNum = 0
    
    # Create runs
    for start in range(0, n, min_run):
        end = min(start + min_run, n)
        passNum = binary_insertion_sort(arr, start, end - 1, ax, passNum)
    
    # Merge runs
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size
            right = min(left + 2 * size, n)
            if mid < right:
                # Create temporary arrays for merging
                left_run = arr[left:mid]
                right_run = arr[mid:right]
                passNum = merge_lo(arr, left_run, right_run, left, ax, passNum)
        size *= 2
        
    return arr

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
