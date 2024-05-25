class Stack:
    def __init__(self):
        self.stack = []

    # Add an element
    def push(self, item):
        self.stack.append(item)

    # Remove an element
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    # Display  the queue
    def display(self):
        return self.stack

    def get_len(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0
