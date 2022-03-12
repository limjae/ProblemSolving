class MyCircularQueue:
    queue = []
    capacity = 0
    front = 0
    rear = 0
    Empty = True

    def __init__(self, k: int):
        self.queue = [0 for _ in range(k)]
        self.capacity = k
        self.front = 0
        self.rear = 0
        self.Empty = True

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        if self.Empty:
            self.Empty = False

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        # unnecessary
        # self.queue[self.front] = 0
        self.front = (self.front + 1) % self.capacity
        if self.front == self.rear:
            self.Empty = True

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[(self.rear + self.capacity - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.Empty

    def isFull(self) -> bool:
        return self.front == self.rear and self.Empty == False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()