import unittest
from src.password_validator import validate_passwords


class TestPasswordValidator(unittest.TestCase):
    def test_valid_passwords(self):
        passwords = ["Afbhejr343@.1", "asdnd3H12#", "438hfvnG2", "DJNDW331111!!"]
        self.assertEqual(validate_passwords(passwords), ["asdnd3H12#"])


if __name__ == '__main__':
    unittest.main()