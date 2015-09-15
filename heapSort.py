"""
    heapSort.py
    
    -------------------
    Uses the max heap data structure implemented in a list.
    Time Complexity: O(n log n)
    Stable: NO
"""


def max_heapify(seq, i, n):
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child <= n and seq[left_child] > seq[i]:
        largest = left_child
    else:
        largest = i
    if right_child <= n and seq[right_child] > seq[largest]:
        largest = right_child

    if largest != i:
        seq[i], seq[largest] = seq[largest], seq[i]
        max_heapify(seq, largest, n)


def build_heap(seq):
    n = len(seq) - 1
    for i in range(n//2, -1, -1):
        max_heapify(seq, i, n)


def heapsort(seq):
    build_heap(seq)
    heap_size = len(seq) - 1
    for x in range(heap_size, 0, -1):
        seq[0], seq[x] = seq[x], seq[0]
        heap_size = heap_size - 1
        max_heapify(seq, 0, heap_size)

    return seq

ans=heapsort([71,84,65,1,7,856,34,96,20,34,70,12,5,3])

print(ans)
