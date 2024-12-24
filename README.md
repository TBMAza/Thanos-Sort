# Thanos Sort

Thanos Sort is a unique sorting algorithm inspired by a "purge-and-conquer" approach to ordering data. Unlike traditional sorting algorithms that reorder elements through comparisons and swaps, Thanos Sort divides the input into a sorted list and a list of "non-conforming" elements, recursively sorting the latter until the entire array is sorted.

## Table of Contents

- [How It Works](#how-it-works)
- [Time Complexity](#time-complexity)
- [Use Cases](#use-cases)
- [Code Implementation](#code-implementation)
- [Benchmarks](#benchmarks)
- [Contributing](#contributing)
- [License](#license)

## How It Works

1. **Initial Pass:**
  
  - Traverse the input array while maintaining a running list of sorted elements (`sorted1`).
  - Any element that does not fit the ascending order is placed in an "unsorted" list (`unsorted`).
2. **Recursive Sorting:**
  
  - Recursively apply Thanos Sort to the `unsorted` list.
3. **Uniting:**
  
  - Unite the sorted list (`sorted1`) with the recursively sorted `unsorted` list to produce the final result.

## Time Complexity

- **Best Case:** `O(n)` — If the input array is already sorted.
- **Worst Case:** `O(n^2)` — If the input array is in reverse order.
- **Average Case:** Between `O(n)` and `O(n^2)` depending on the distribution of unsorted elements.

## Use Cases

While Thanos Sort is NOT a practical choice for general-purpose sorting due to its worst-case complexity, it has some niche applications:

- **Educational Tool:** Demonstrates recursive algorithms and adaptive sorting techniques.
- **Sorted-Input Optimization:** Performs well on nearly sorted data.
- **Algorithmic Humor:** A playful take on "sorting by purging the unsorted."

## Code Implementation

Below is the Python implementation of Thanos Sort:

```python
def unite(l, r):
    united = []
    i = 0
    j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            united.append(l[i])
            i += 1
        else:
            united.append(r[j])
            j += 1
    if i < len(l):
        united += l[i:]
    else:
        united += r[j:]
    return united

def thanos_sort(arr):
    if len(arr) <= 1:
        return arr
    sorted1 = []
    unsorted = []
    prev = 0
    for n in arr:
        if not sorted1:
            sorted1.append(n)
            prev = n
        elif n >= prev:
            sorted1.append(n)
            prev = n
        else:
            unsorted.append(n)
    if unsorted:
        sorted2 = thanos_sort(unsorted)
        return unite(sorted1, sorted2)
    return sorted1
```

## Benchmarks

To illustrate the performance of Thanos Sort, here are some benchmark results comparing it to traditional sorting algorithms:

| Input Type | Input Size | Thanos Sort Time | Python Built-in Sort Time |
| --- | --- | --- | --- |
| Already Sorted | 10,000 | `O(n)` | `O(n log n)` |
| Reverse Sorted | 10,000 | `O(n^2)` | `O(n log n)` |
| Random Order | 10,000 | `O(n^2)` | `O(n log n)` |

*Note:* These results highlight Thanos Sort's suitability for sorted or nearly sorted data.

## Contributing

Contributions are welcome! If you have ideas for optimizing Thanos Sort or creative ways to visualize it, feel free to fork this repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Fun Fact

The name "Thanos Sort" is a playful nod to the Marvel character Thanos, who famously aimed to bring balance to the universe by eliminating half of all life. Similarly, Thanos Sort "purges" elements that disrupt the order to bring balance to your array. Use responsibly!
