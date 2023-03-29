class MinStack:
    def __init__(self):
        self.s = []
        self.min_val = 2 ** 31 - 1

    def push(self, val: int) -> None:
        if val <= self.min_val:
            self.s.append(self.min_val)
            self.min_val = val
        self.s.append(val)

    def pop(self) -> None:
        popped = self.s.pop()
        if popped == self.min_val:
            self.min_val = self.s.pop()

    def top(self) -> int:
        return self.s[len(self.s)-1]

    def getMin(self) -> int:
        return self.min_val


class MinStack2:
    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        _min = self.getMin()
        if val < _min or _min is None:
            _min = val
        self.s.append((val, _min))

    def pop(self) -> None:
        if len(self.s) == 0:
            return None
        else:
            self.s.pop()

    def top(self) -> int:
        if len(self.s) == 0:
            return None
        return self.s[-1][0]

    def getMin(self) -> int:
        if len(self.s) == 0:
            return None
        return self.s[-1][1]
