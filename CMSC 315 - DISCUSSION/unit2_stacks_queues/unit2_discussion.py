"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        #  This puts new values at the top of the stack.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # If the stack is empty, nothing will be popped.
        # The if statement returns none if the stack is empty. 
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek allows you to look at the top value in a stack without modifying it.
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object. *
    # 2. Add at least 4 values to the stack. *
    # 3. Improve the print statements so they clearly explain what is happening. *
    # 4. Demonstrate LIFO behavior. *
    # 5. Show what happens when pop() is used on an empty stack. *
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack. *
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward. *


print("\n=== STACK DEMO ===")

stack = Stack()

print("Adding the following weapons to the stack:")
stack.push("Midnight Coup")
stack.push("Steelfeather Repeater")
stack.push("Le Monarque")
stack.push("Devil's Ruin")

print(f"Stack items: {stack.items}")
print(f"The stack's top value is: {stack.peek()}")

print("\nLIFO Behavior Demonstration:")

while not stack.is_empty():
    print(f"Popped item: {stack.pop()}")
print(f"No items in the stack?: {stack.is_empty()}")

# Empty stack pop and peek edge case
test_empty_stack = stack.pop()
print("\nPopping from empty stack.")
print(f"Result:  {test_empty_stack}")

test_empty_peek = stack.peek()
print("Peeking into an empty stack.")
print(f"Result: {test_empty_peek}")

# 1 item edge case
one_stack = Stack()
one_stack.push("Little guy")

print("\nOne Item Stack Test")
print(f"Original: {one_stack.items}")
print(f"Popped item: {one_stack.pop()}")
print(f"Is the stack empty after popping?: {one_stack.is_empty()}")


# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")

queue = Queue()

print("Adding the following weapons to queue:")
queue.enqueue("Leviathan's Breath")
queue.enqueue("Anarchy")
queue.enqueue("Felwinter's Lie")
queue.enqueue("Tlaloc")

print(f"Queue items: {list(queue.items)}")
print(f"First weapon transfer: {queue.front()}")

print("\nFIFO Behavior Demonstration:")

while not queue.is_empty():
    print(f"Dequeued item: {queue.dequeue()}")
print(f"No items in the queue?: {queue.is_empty()}")

test_empty_queue = queue.dequeue()
print("\nDequeueing from empty queue.")
print(f"Result: {test_empty_queue}")

test_front_empty = queue.front()
print("Peeking into an empty queue.")
print(f"Result: {test_front_empty}")

one_queue = Queue()
one_queue.enqueue("Littler guy")

print("\nOne Item Queue Test")
print(f"Original: {list(one_queue.items)}")
print(f"Dequeued item: {one_queue.dequeue()}")
print(f"Is the queue empty after a dequeue?: {one_queue.is_empty()}")

if __name__ == "__main__":
    main()
