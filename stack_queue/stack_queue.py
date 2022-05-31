from collections import deque


class Stack:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.stack = elements

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not len(self.stack):
            print("Il n'y a aucun élément dans la pile")
        else:
            return self.stack.pop()

    def peek(self):
        if not len(self.stack):
            print("Il n'y a aucun élément dans la pile")
        else:
            return self.stack[-1]

    def print_stack(self):
        print(self.stack)


class Queue:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.queue = deque(elements)

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if not len(self.queue):
            print("Il n'y a aucune carte dans la liste d'attente")
        else:
            return self.queue.popleft()

    def peek(self):
        if not len(self.queue):
            print("Il n'y a aucune carte dans la liste d'attente")
        else:
            return self.queue[0]

    def print_queue(self):
        print(list(self.queue))
