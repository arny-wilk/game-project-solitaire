from solitaire.stack_queue.stack_queue import Stack
from solitaire.stack_queue.stack_queue import Queue

if __name__ == '__main__':
    s = Stack(["a", "b", "c", "d", "e", "f", "g"])
    s.print_stack()
    print(s.peek())
    s.pop()
    s.print_stack()
    s.push("e")
    s.print_stack()
    print(s.peek())

    q = Queue(["a", "b", "c", "d", "e", "f", "g"])
    print(q.peek())
    q.dequeue()
    q.print_queue()
    q.enqueue("e")
    q.print_queue()
    print(q.peek())

