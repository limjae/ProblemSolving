class MyQueue:
    queue_stack = list()
    def __init__(self):
        self.queue_stack = list()

    def push(self, x: int) -> None:
        self.queue_stack.append(x)

    def pop(self) -> int:
        tmp_stack = []

        while self.queue_stack:
            tmp_stack.append(self.queue_stack.pop())

        result = tmp_stack.pop()

        while tmp_stack:
            self.queue_stack.append(tmp_stack.pop())

        return result

    def peek(self) -> int:
        tmp_stack = []

        while self.queue_stack:
            tmp_stack.append(self.queue_stack.pop())

        result = tmp_stack.pop()
        tmp_stack.append(result)

        while tmp_stack:
            self.queue_stack.append(tmp_stack.pop())

        return result


    def empty(self) -> bool:
        return False if self.queue_stack else True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()