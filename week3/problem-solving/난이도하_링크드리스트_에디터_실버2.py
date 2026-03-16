# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

# 다시 풀기
import sys

input = sys.stdin.readline
left = list(input().rstrip())
right = []
M = int(input())
for _ in range(M):
    command = input().rstrip()
    match command[0]:
        case "L":
            if left:
                right.append(left.pop())
        case "D":
            if right:
                left.append(right.pop())
        case "B":
            if left:
                left.pop()
        case "P":
            left.append(command[2])
print("".join(left + right[::-1]))


# """ class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next


# # Like Stack
# class LinkedList:
#     def __init__(self):
#         self.length = 0
#         self.head = None
#         self.cursor = Node("__cursor")
#         self.trace = []

#     def append_left(self, data):
#         """
#         초기 입력값을 받기 위한 함수
#         """
#         if self.head is None:
#             self.head = Node(data)
#         else:
#             node = Node(data)
#             node.next = self.head
#             self.head = node

#     def reset_cursor(self):
#         """초기 입력 후 커서 위치 초기화"""
#         node = Node(None)
#         node.next = self.head
#         self.head = node
#         self.cursor.data = self.head

#     def append(self, data):
#         # 명령 P가 들어왔을 경우 수행할 메서드
#         cursor: Node = self.cursor.data
#         next_node = cursor.next
#         new_node = Node(data)

#         new_node.next = next_node
#         cursor.next = new_node


#     def pop(self):
#         """
#         명령 B가 들어왔을 경우 수행할 메서드
#         왼쪽 끝인지 확인하기 위해서는 현재 노드의 node.next가 None인지 확인하면 된다.

#         왼쪽에 노드가 2개 있는지 1개 있는지에 따라서 동작이 달라진다.
#         """
#         cursor: Node = self.cursor.data
#         if cursor.next is None:
#             return

#         if cursor.next.next is None:
#             cursor.next = None
#         else:
#             next_node = cursor.next
#             cursor.next = next_node.next

#     def move_left(self):
#         """
#         명령 L이 들어왔을 경우 수행할 메서드
#         왼쪽 끝인지 확인하기 위해서는 현재 노드의 node.next가 None인지 확인하면 된다.
#         trace에 push하여 이동 전 노드를 기록한다.
#         """
#         cursor: Node = self.cursor.data
#         if cursor.next is None:
#             return

#         self.trace.append(cursor)
#         self.cursor.data = cursor.next

#     def move_right(self):
#         """
#         명령 D가 들어왔을 경우 수행할 메서드
#         오른쪽 끝인지 확인하기 위해서는 현재 노드가 self.head인지 확인하면 된다.
#         cursor를 trace.pop() 노드로 옮긴다.
#         """
#         cursor: Node = self.cursor.data
#         if cursor is self.head:
#             return

#         self.cursor.data = self.trace.pop()


# import sys

# # 입력
# input = sys.stdin.readline
# text = input().strip()
# linked_list = LinkedList()
# for char in text:
#     linked_list.append_left(char)
# linked_list.reset_cursor()

# # 명령 실행
# M = int(input())
# for _ in range(M):
#     command = input().split()
#     match command[0]:
#         case "L":
#             linked_list.move_left()
#         case "D":
#             linked_list.move_right()
#         case "B":
#             linked_list.pop()
#         case "P":
#             linked_list.append(command[1])

# # 출력
# stack = []
# traversal = linked_list.head
# while traversal.next is not None:
#     traversal = traversal.next
#     stack.append(traversal.data)
# print("".join(stack[::-1])) """
