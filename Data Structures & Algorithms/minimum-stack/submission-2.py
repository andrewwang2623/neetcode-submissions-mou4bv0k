import heapq
class MinStack:


    def __init__(self):
        self.min_value = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if val < self.min_value:
            self.min_value = val
        self.stack.append((val, self.min_value))

    def pop(self) -> None:
        if len(self.stack) == 1:
            self.min_value = float('inf')
        else:
            self.min_value = self.stack[-2][1]
        return self.stack.pop()[0]
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min_value
