class MinStack:

    def __init__(self):
        self.arr = []
        self.minimum = [[0,0]]
        self.initialized = True

    def push(self, val: int) -> None:
        if self.initialized:
            self.minimum.pop()
            self.minimum.append([val, val])
            self.initialized = False
        elif len(self.minimum) == 0:
            self.minimum.append([val, val])
        elif val <= self.minimum[-1][-1]:
            self.minimum.append([self.minimum[-1][-1],val])
        self.arr.append(val)

    def pop(self) -> None:
        x = self.arr[-1]
        del self.arr[-1]
        if x == self.minimum[-1][-1]:
            del self.minimum[-1]
        return x

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        print(self.arr)
        return self.minimum[-1][-1]
