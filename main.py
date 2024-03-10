import threading
from src.password_validator import validate_passwords
from src.circular_queue import CircularQueue


def program1():
    with open('input/passwords.txt', 'r') as file:
        passwords = file.read().split(',')
    accepted_passwords = validate_passwords(passwords)
    print("Accepted passwords:", ",".join(accepted_passwords))


def program2():
    queue = CircularQueue()
    for i in range(1, 10):
        queue.enqueue(i)
    queue.display()


def main():
    # Create threads for each program
    thread1 = threading.Thread(target=program1)
    thread2 = threading.Thread(target=program2)

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for all threads to complete
    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
