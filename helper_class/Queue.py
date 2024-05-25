class Queue:
    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return self.get_len() == 0

    # Display  the queue
    def display(self):
        return self.queue

    def get_len(self):
        return len(self.queue)
