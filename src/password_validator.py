def validate_password(password):
    return all([
        6 <= len(password) <= 12,
        any(char.islower() for char in password),
        any(char.isdigit() for char in password),
        any(char.isupper() for char in password),
        any(char in '$#@' for char in password)
    ])


def validate_passwords(passwords):
    valid_passwords = []
    for password in passwords:
        if validate_password(password):
            valid_passwords.append(password)
    return valid_passwords
