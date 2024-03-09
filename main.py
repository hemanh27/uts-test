# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from src.password_validator import validate_passwords


def main():
    with open('input/passwords.txt', 'r') as file:
        passwords = file.read().split(',')
    print(passwords)
    accepted_passwords = validate_passwords(passwords)
    print("Accepted passwords:", ",".join(accepted_passwords))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
