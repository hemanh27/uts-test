class CircularQueue:
    def __init__(self, max_length=5):
        self.queue = []
        self.max_length = max_length

    def is_full(self):
        return len(self.queue) == self.max_length

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, element):
        if self.is_full():
            self.dequeue()  # Remove the latest added element if the queue is full
        self.queue.append(element)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        else:
            removed_element = self.queue.pop(-1)  # Remove the latest element
            return removed_element

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Circular Queue:", self.queue)
