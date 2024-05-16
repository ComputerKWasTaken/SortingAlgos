### README.md

# Sorting Algorithms Visualization

This repository contains Python implementations of various sorting algorithms, both standard and joke ones, with visualization using `matplotlib`. The project allows users to either learn about the algorithms or see them in action with randomized arrays.

## Folder Structure

```
.
├── joke
│   ├── bogo_sort.py
│   ├── bogobogo_sort.py
│   └── stalin_sort.py
├── normal
│   ├── bubble_sort.py
│   ├── cocktail_shaker_sort.py
│   ├── quick_sort.py
│   ├── merge_sort.py
│   ├── heap_sort.py
│   ├── tim_sort.py
│   ├── intro_sort.py
│   ├── shell_sort.py
│   └── comb_sort.py
├── requirements.txt
└── sorter.py
```

## Sorting Algorithms

### Normal Sorting Algorithms
- **Bubble Sort**: A simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
- **Cocktail Shaker Sort**: A variation of Bubble Sort that sorts in both directions on each pass through the list.
- **Quick Sort**: A highly efficient sorting algorithm that uses a divide-and-conquer approach.
- **Merge Sort**: A stable, comparison-based, divide-and-conquer sorting algorithm.
- **Heap Sort**: A comparison-based sorting technique based on Binary Heap data structure.
- **Tim Sort**: A hybrid sorting algorithm derived from Merge Sort and Insertion Sort.
- **Intro Sort**: A hybrid sorting algorithm that begins with Quick Sort and switches to Heap Sort when the recursion depth exceeds a level based on the number of elements being sorted.
- **Shell Sort**: Shell Sort is a generalization of Insertion Sort that allows the exchange of items that are far apart. The idea is to arrange the list of elements so that, starting anywhere, considering every hth element gives a sorted list.
- **Comb Sort**: Comb Sort is a comparison-based algorithm that improves on Bubble Sort by using a gap greater than 1. The gap starts with a large value and shrinks by a factor of 1.3 in every iteration until it reaches the value 1.

### Joke Sorting Algorithms
- **Bogo Sort**: A highly ineffective sorting algorithm based on the generate and test paradigm.
- **Bogobogo Sort**: An extremely inefficient and impractical sorting algorithm. It works by recursively applying Bogo Sort to progressively larger prefixes of the list and then shuffling the entire list if it is not sorted.
- **Stalin Sort**: A joke sorting algorithm where elements that are out of order are removed from the list, leaving only the sorted elements.

## How to Use

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/ComputerKWasTaken/SortingAlgos.git
    cd SortingAlgos
    ```

2. **Install the Requirements**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Script**:
    ```sh
    python sorter.py
    ```

4. **Choose an Option**:
    - To use the algorithms, select `use` and follow the prompts.
    - To learn about the algorithms, select `learn` and follow the prompts.

## Dependencies

- `matplotlib`

The required dependencies will be installed automatically when you run `pip install -r requirements.txt`.

## Contributing

Feel free to fork this repository, make changes, and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.
