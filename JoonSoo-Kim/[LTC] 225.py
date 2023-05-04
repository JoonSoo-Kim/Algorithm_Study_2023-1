import collections

class stackByQueue:
    def __init__(self):
        self.queue = collections.deque()

    def push(self, item):
        self.queue.append(item)

        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        return self.queue.popleft()

    def top(self):
        return self.queue[0]

    def empty(self):
        return len(self.queue) == 0


stack = stackByQueue()
stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())