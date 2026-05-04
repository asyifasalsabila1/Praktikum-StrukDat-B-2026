class StackList:
    def __init__(self):
        self.items = []  

    def is_empty(self):
        return len(self.items) == 0

    def push(self, url):
        self.items.append(url)

    def pop(self):
        if self.is_empty():
            return "Riwayat kosong"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)


# bikin object di luar class
History = StackList()

History.push('cipa')
History.push('bila')
History.push('salsa')

print("stack:", History.items)
print("pop:", History.pop())
print("Peek:", History.peek())
print("isEmpty:", History.is_empty())
print("Size:", History.size())

