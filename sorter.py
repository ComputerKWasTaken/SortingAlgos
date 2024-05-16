import matplotlib.pyplot as plt
import random
from normal.bubble_sort import bubbleSortRecursive
from normal.cocktail_shaker_sort import cocktailShakerSort
from normal.quick_sort import quickSort
from normal.merge_sort import mergeSort
from normal.heap_sort import heapSort
from normal.tim_sort import timSort
from normal.intro_sort import introSort
from normal.shell_sort import shellSort
from normal.comb_sort import combSort
from joke.bogo_sort import bogoSort
from joke.stalin_sort import stalinSort
from joke.bogobogo_sort import bogobogoSort

def get_algorithm_info(category, sortType):
    """Returns information about the selected sorting algorithm."""
    info = {
        'normal': {
            'bubble': 'Bubble Sort is a simple comparison-based algorithm in which each pair of adjacent elements is compared and the elements are swapped if they are not in order. This process repeats from the beginning until the list is sorted.',
            'cocktail': 'Cocktail Shaker Sort is a variation of Bubble Sort that sorts in both directions on each pass through the list, first from left to right, then from right to left.',
            'quick': 'Quick Sort is a highly efficient sorting algorithm that uses a divide-and-conquer approach to partition the array and recursively sort the sub-arrays.',
            'merge': 'Merge Sort is a stable, comparison-based, divide-and-conquer sorting algorithm that divides the array into halves, recursively sorts them, and then merges the sorted halves.',
            'heap': 'Heap Sort is a comparison-based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place it at the end.',
            'tim': 'Tim Sort is a hybrid sorting algorithm derived from Merge Sort and Insertion Sort. It is used in Python’s built-in sort() and sorted() functions.',
            'intro': 'Intro Sort is a hybrid sorting algorithm that begins with Quick Sort and switches to Heap Sort when the recursion depth exceeds a certain level.',
            'shell': 'Shell Sort is a generalization of Insertion Sort that allows the exchange of items that are far apart. The idea is to arrange the list of elements so that, starting anywhere, considering every hth element gives a sorted list.',
            'comb': 'Comb Sort is a comparison-based algorithm that improves on Bubble Sort by using a gap greater than 1. The gap starts with a large value and shrinks by a factor of 1.3 in every iteration until it reaches the value 1.'
        },
        'joke': {
            'bogo': 'Bogo Sort is a highly ineffective sorting algorithm based on the generate and test paradigm. It successively generates permutations of its input until it finds one that is sorted.',
            'stalin': 'Stalin Sort is a joke sorting algorithm where elements that are out of order are removed from the list, leaving only the sorted elements.',
            'bogobogo': 'BogoBogo Sort is an extremely inefficient sorting algorithm that recursively applies Bogo Sort to progressively larger prefixes of the list and then shuffles the entire list if it is not sorted.'
        }
    }
    return info[category].get(sortType, "Information not available for the selected algorithm.")

def animateSort(arr, sortType, category):
    """Initializes the figure and selects the sorting algorithm."""
    fig, ax = plt.subplots()
    valid_sort_types = ['bubble', 'cocktail', 'quick', 'merge', 'heap', 'tim', 'intro', 'shell', 'comb', 'bogo', 'stalin', 'bogobogo']
    while sortType not in valid_sort_types:
        sortType = input("Invalid sort type. Please enter a valid sort type: ")
    if category == 'normal':
        if sortType == 'bubble':
            bubbleSortRecursive(arr, len(arr), 0, ax)
        elif sortType == 'cocktail':
            cocktailShakerSort(arr, ax)
        elif sortType == 'quick':
            quickSort(arr, 0, len(arr) - 1, 0, ax)
        elif sortType == 'merge':
            mergeSort(arr, 0, len(arr) - 1, 0, ax)
        elif sortType == 'heap':
            heapSort(arr, ax)
        elif sortType == 'tim':
            timSort(arr, ax)
        elif sortType == 'intro':
            introSort(arr, ax)
        elif sortType == 'shell':
            shellSort(arr, ax)
        elif sortType == 'comb':
            combSort(arr, ax)
    elif category == 'joke':
        if sortType == 'bogo':
            bogoSort(arr, ax)
        elif sortType == 'stalin':
            stalinSort(arr, ax)
        elif sortType == 'bogobogo':
            bogobogoSort(arr, ax)
    plt.show()

def main():
    """Main function to drive the sorting visualization."""
    while True:
        action = input("Would you like to use the algorithms or learn about them? (use/learn): ").strip().lower()
        if action in ['use', 'learn']:
            break
        print("Invalid input. Please enter 'use' or 'learn'.")
    
    if action == 'learn':
        while True:
            category = input("Select the category of sorting algorithms (normal/joke): ").strip().lower()
            if category in ['normal', 'joke']:
                break
            print("Invalid category. Please enter 'normal' or 'joke'.")
        
        while True:
            sortType = input(f"Enter the {category} sorting algorithm: ").strip().lower()
            info = get_algorithm_info(category, sortType)
            if info != "Information not available for the selected algorithm.":
                print(info)
                break
            print("Invalid sorting algorithm. Please enter a valid sorting algorithm.")
    
    elif action == 'use':
        while True:
            try:
                lengthOfArray = int(input("Enter the length of the array: "))
                if lengthOfArray > 0:
                    break
                else:
                    print("Array length must be a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
        
        while True:
            category = input("Select the category of sorting algorithms (normal/joke): ").strip().lower()
            if category in ['normal', 'joke']:
                break
            print("Invalid category. Please enter 'normal' or 'joke'.")
        
        if category == 'normal':
            valid_normal_sorts = ['bubble', 'cocktail', 'quick', 'merge', 'heap', 'tim', 'intro', 'shell', 'comb']
            while True:
                sortType = input("Enter the normal sorting algorithm (bubble/cocktail/quick/merge/heap/tim/intro/shell/comb): ").strip().lower()
                if sortType in valid_normal_sorts:
                    break
                print("Invalid sorting algorithm. Please enter a valid normal sorting algorithm.")
        elif category == 'joke':
            valid_joke_sorts = ['bogo', 'stalin', 'bogobogo']
            while True:
                sortType = input("Enter the joke sorting algorithm (bogo/stalin/bogobogo): ").strip().lower()
                if sortType in valid_joke_sorts:
                    break
                print("Invalid sorting algorithm. Please enter a valid joke sorting algorithm.")
        
        arrayToSort = list(range(1, lengthOfArray + 1))
        random.shuffle(arrayToSort)
        
        print("Array to sort:", arrayToSort)
        animateSort(arrayToSort, sortType, category)

if __name__ == "__main__":
    main()
