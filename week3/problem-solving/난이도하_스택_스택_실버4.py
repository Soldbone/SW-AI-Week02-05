# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self._top: Node = None
        self.length = 0

    def push(self, item: int) -> None:
        node = Node(item)

        if self.empty():
            self._top = node
        else:
            node.next = self._top
            self._top = node
        self.length += 1

    def pop(self) -> int:
        if self.empty():
            return -1

        node = self._top
        self._top = node.next
        # gc
        self.length -= 1
        return node.val

    def size(self) -> int:
        return self.length

    def empty(self) -> bool:
        return int(self._top is None)

    def top(self) -> int:
        if self.empty():
            return -1
        else:
            return self._top.val


import sys

input = sys.stdin.readline

N = int(input())
stack = Stack()
for _ in range(N):
    command = input().split()
    match command[0]:
        case "push":
            stack.push(int(command[1]))
        case "pop":
            print(stack.pop())
        case "size":
            print(stack.size())
        case "empty":
            print(stack.empty())
        case "top":
            print(stack.top())
