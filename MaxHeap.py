class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _print(self):
        return self.heap

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and self.heap[max_index] < self.heap[left_index]:
                max_index = left_index

            if right_index < len(self.heap) and self.heap[max_index] < self.heap[right_index]:
                max_index = right_index

            if max_index != index:
                self._swap(max_index, index)
                index = max_index
            else:
                return

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value


# my_list = [99, 75, 58, 72, 61]
Heap = MaxHeap()
Heap.insert(95)
Heap.insert(75)
Heap.insert(80)
Heap.insert(55)
Heap.insert(60)
# print(Heap.heap)
Heap.insert(50)
# print(Heap.heap)
Heap.insert(65)

print(Heap.heap)

Heap.remove()

print(Heap.heap)
Heap.remove()

print(Heap.heap)



