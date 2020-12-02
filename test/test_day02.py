import unittest
from day02 import PasswordRule


class Test(unittest.TestCase):
    def test_PasswordRule_from_string(self):
        RULE_STR = '1-3 a'

        expected = PasswordRule(letter='a', min_count=1, max_count=3)
        actual = PasswordRule.from_string(RULE_STR)

        assert expected == actual
