"""
- push(): 맨 위에 원소를 추가
- pop(): 맨 위에 놓인 원소 제거 및 반환
- peek(): 맨 위에 놓인 원소 확인
- is_empty(): 비어 있는지 확인
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)

        if self.is_empty():
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self.is_empty():
            return None

        node = self.top
        self.top = node.next

        return node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None


if __name__ == "__main__":
    s = Stack()

    for i in range(3):
        s.push(chr(ord("A") + i))
        print(f"Push data = {s.peek()}")
    print()

    while not s.is_empty():
        print(f"Pop data = {s.pop()}")
    print()

    print(f"Peek data = {s.peek()}")
