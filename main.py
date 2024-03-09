# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from src.password_validator import validate_passwords
from src.circular_queue import CircularQueue


def main():
    with open('input/passwords.txt', 'r') as file:
        passwords = file.read().split(',')
    accepted_passwords = validate_passwords(passwords)
    print("Accepted passwords:", ",".join(accepted_passwords))

    queue = CircularQueue()
    for i in range(1, 10):
        queue.enqueue(i)
    queue.display()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
