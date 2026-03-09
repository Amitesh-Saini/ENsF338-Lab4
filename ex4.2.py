import timeit
import random
import matplotlib.pyplot as plt


def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


"""
Q4.
Worst-case complexity:
- Linear search: O(n)
- Binary search: O(log n)

Linear search may need to inspect every element.
Binary search repeatedly halves the search interval.
"""


def run_experiment():
    sizes = [1000, 5000, 10000, 20000]
    repeats = 100

    linear_times = []
    binary_times = []

    for n in sizes:
        arr = list(range(n))
        target = random.choice(arr)

        linear_size_times = []
        binary_size_times = []

        for _ in range(repeats):
            t1 = timeit.timeit(lambda: linear_search(arr, target), number=1)
            t2 = timeit.timeit(lambda: binary_search(arr, target), number=1)

            linear_size_times.append(t1)
            binary_size_times.append(t2)

        linear_times.append(linear_size_times)
        binary_times.append(binary_size_times)

    return sizes, linear_times, binary_times


def plot_results(sizes, linear_times, binary_times):
    plt.figure(figsize=(10, 6))

    linear_means = [sum(times) / len(times) for times in linear_times]
    binary_means = [sum(times) / len(times) for times in binary_times]

    plt.plot(sizes, linear_means, marker='o', label='Linear Search')
    plt.plot(sizes, binary_means, marker='o', label='Binary Search')

    plt.xlabel("Array Size")
    plt.ylabel("Average Time (seconds)")
    plt.title("Linear Search vs Binary Search")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Distribution plots
    plt.figure(figsize=(10, 6))
    plt.boxplot(
        [linear_times[0], binary_times[0], linear_times[-1], binary_times[-1]],
        labels=[
            f"Linear n={sizes[0]}",
            f"Binary n={sizes[0]}",
            f"Linear n={sizes[-1]}",
            f"Binary n={sizes[-1]}"
        ]
    )
    plt.ylabel("Execution Time (seconds)")
    plt.title("Distribution of Search Times")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    sizes, linear_times, binary_times = run_experiment()
    plot_results(sizes, linear_times, binary_times)