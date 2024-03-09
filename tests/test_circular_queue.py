import unittest
from src.circular_queue import CircularQueue


class TestCircularQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = CircularQueue()
        for i in range(1, 7):
            queue.enqueue(i)
        self.assertEqual(queue.queue, [1, 2, 3, 4, 6])


if __name__ == '__main__':
    unittest.main()