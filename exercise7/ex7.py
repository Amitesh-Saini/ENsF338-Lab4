# ex7.py

import timeit
import matplotlib.pyplot as plt


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, node):
        node.next = self.head
        self.head = node

    def insert_tail(self, node):
        if self.head is None:
            self.head = node
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = node

    def get_size(self):
        count = 0
        curr = self.head
        while curr is not None:
            count += 1
            curr = curr.next
        return count

    def get_element_at_pos(self, pos):
        curr = self.head
        index = 0

        while curr is not None:
            if index == pos:
                return curr
            curr = curr.next
            index += 1

        return None

    def reverse_slow(self):
        newhead = None
        prevNode = None

        for i in range(self.get_size() - 1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)

            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode

            prevNode = currNewNode

        self.head = newhead

    def reverse_fast(self):
        prev = None
        curr = self.head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    def copy(self):
        new_list = SinglyLinkedList()
        curr = self.head
        while curr is not None:
            new_list.insert_tail(Node(curr.data))
            curr = curr.next
        return new_list


def build_list(n):
    ll = SinglyLinkedList()
    for i in range(n):
        ll.insert_tail(Node(i))
    return ll


def measure_reverse(method_name, size, repetitions=100):
    times = []

    for _ in range(repetitions):
        ll = build_list(size)

        if method_name == "slow":
            t = timeit.timeit(lambda: ll.reverse_slow(), number=1)
        else:
            t = timeit.timeit(lambda: ll.reverse_fast(), number=1)

        times.append(t)

    return times


def run_experiment():
    sizes = [200, 400, 600, 800]

    slow_results = []
    fast_results = []

    for size in sizes:
        slow_times = measure_reverse("slow", size, 20)
        fast_times = measure_reverse("fast", size, 20)

        slow_results.append(slow_times)
        fast_results.append(fast_times)

    return sizes, slow_results, fast_results


def plot_results(sizes, slow_results, fast_results):
    slow_means = [sum(times) / len(times) for times in slow_results]
    fast_means = [sum(times) / len(times) for times in fast_results]

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, slow_means, marker='o', label='Original reverse (O(n^2))')
    plt.plot(sizes, fast_means, marker='o', label='Optimized reverse (O(n))')
    plt.xlabel("List Size")
    plt.ylabel("Average Time (seconds)")
    plt.title("Reverse Linked List Performance")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Distribution plot
    plt.figure(figsize=(12, 6))
    data = []
    labels = []

    for i, size in enumerate(sizes):
        data.append(slow_results[i])
        labels.append(f"Slow {size}")
        data.append(fast_results[i])
        labels.append(f"Fast {size}")
        print("hi")

    plt.boxplot(data, labels=labels)
    plt.ylabel("Execution Time (seconds)")
    plt.title("Distribution of Reverse Times")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    sizes, slow_results, fast_results = run_experiment()
    plot_results(sizes, slow_results, fast_results)
