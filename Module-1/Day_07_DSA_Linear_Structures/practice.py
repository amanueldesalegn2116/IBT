"""
Day 07 - Custom Linear Data Structures & LeetCode-style Challenges
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    def to_list(self) -> list:
        res = []
        curr = self.head
        while curr:
            res.append(curr.value)
            curr = curr.next
        return res


def reverse_linked_list(head: Node) -> Node:
    """Challenge 16a: Reverses a singly linked list."""
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def has_cycle(head: Node) -> bool:
    """Challenge 16b: Floyd's Cycle Detection Algorithm."""
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def is_valid_parentheses(s: str) -> bool:
    """Challenge 17: Valid Parentheses using Stack."""
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack


class QueueUsingTwoStacks:
    """Challenge 18: Implement Queue using Two Stacks."""
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int):
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop() if self.s2 else None


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.append(10)
    sll.append(20)
    sll.append(30)
    print("Linked List:", sll.to_list())

    print("Valid Parentheses '({[]})':", is_valid_parentheses("({[]})"))
    print("Valid Parentheses '([)]':", is_valid_parentheses("([)]"))
