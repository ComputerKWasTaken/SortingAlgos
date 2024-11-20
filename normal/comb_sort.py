import matplotlib.pyplot as plt
from typing import List

def get_next_gap(gap: int) -> int:
    """Calculate next gap using optimal shrink factor of 1.3"""
    gap = (gap * 10) // 13  # Multiply first to maintain precision
    return max(1, gap)

def insertion_sort_pass(arr: List[int], start: int, gap: int, ax=None) -> bool:
    """Perform one pass of insertion sort with the given gap"""
    n = len(arr)
    swapped = False
    
    for i in range(start, n - gap):
        if arr[i] > arr[i + gap]:
            arr[i], arr[i + gap] = arr[i + gap], arr[i]
            swapped = True
            if ax:
                visualize(arr, gap, i, ax)
                
    return swapped

def is_sorted(arr: List[int]) -> bool:
    """Check if array is sorted"""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def combSort(arr: List[int], ax=None) -> List[int]:
    """Optimized comb sort implementation"""
    if not arr:
        return arr
        
    n = len(arr)
    if n < 2:
        return arr
        
    gap = n
    swapped = True
    
    # Optimization: Use different gap reduction factor for different array sizes
    shrink = 1.3 if n > 1000 else 1.25
    
    while gap > 1 or swapped:
        # Update gap using optimal shrink factor
        gap = max(1, int(gap / shrink))
        
        # Optimization: Use different strategies based on gap size
        if gap <= 1:
            # For gap=1, use traditional bubble sort pass with early exit
            swapped = False
            for i in range(n - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
                    if ax:
                        visualize(arr, gap, i, ax)
            
            # Early termination check
            if not swapped:
                break
        else:
            # For larger gaps, use multiple passes with offsets
            swapped = False
            for offset in range(min(gap, 3)):  # Use up to 3 offset passes for better distribution
                if insertion_sort_pass(arr, offset, gap, ax):
                    swapped = True
            
            # Quick check if array might be sorted
            if gap < n // 2 and not swapped and is_sorted(arr[:n//2]):
                # Verify if the entire array is sorted
                if is_sorted(arr):
                    break
    
    return arr

def visualize(arr: List[int], gap: int, currentIndex: int, ax):
    """Updates the matplotlib bar graph for visualization."""
    if ax is None:
        return
        
    ax.clear()
    barColors = ['blue'] * len(arr)
    barColors[currentIndex] = 'orange'
    if currentIndex + gap < len(arr):
        barColors[currentIndex + gap] = 'red'
    
    ax.bar(range(len(arr)), arr, color=barColors)
    ax.set_title(f'Gap: {gap}, Current Index: {currentIndex}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    
    plt.pause(0.01)  # Minimal pause to update the visualization
