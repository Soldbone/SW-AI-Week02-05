# 우선순위 큐 (https://wikidocs.net/194546)
class MinHeap:
    @staticmethod
    def heappush(heap, data):
        heap.append(data)
        MinHeap._shift_up(heap, len(heap) - 1)

    @staticmethod
    def heappop(heap):
        if not heap:
            return "Empty Heap!"
        elif len(heap) == 1:
            return heap.pop()

        pop_data, heap[0] = heap[0], heap.pop()
        MinHeap._shift_down(heap, 0)
        return pop_data

    @staticmethod
    def heapify(heap):
        last = len(heap) // 2
        for current in range(last - 1, -1, -1):
            MinHeap._shift_down(heap, current)

    @staticmethod
    def _shift_up(heap, child):
        while child > 0:
            parent = (child - 1) // 2
            if heap[parent] > heap[child]:
                heap[parent], heap[child] = heap[child], heap[parent]
                child = parent
            else:
                break

    @staticmethod
    def _shift_down(heap, parent):
        while parent < len(heap):
            child = parent * 2 + 1
            sibling = child + 1
            if sibling < len(heap) and heap[child] > heap[sibling]:
                child = sibling
            if child < len(heap) and heap[parent] > heap[child]:
                heap[parent], heap[child] = heap[child], heap[parent]
                parent = child
            else:
                break


if __name__ == "__main__":
    heap = [9, 4, 7, 6, 8, 4, 1, 2, 3]
    print(f"{heap}을 heapify한 결과:", end=" ")
    MinHeap.heapify(heap)
    print(heap)

    pop_element = MinHeap.heappop(heap)
    print(f"\nheap에서 heappop한 값: {pop_element}")
    print(f"\nheappop 후의 heap의 상태: {heap}")

    MinHeap.heappush(heap, 0)
    print(f"\n0을 heappush한 결과: {heap}")
