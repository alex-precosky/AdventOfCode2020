import unittest
from day01 import get_twosum_product, get_threesum_product, load_input

class Test(unittest.TestCase):
    def test_twosum(self):
        FILENAME = "input/example01_1.txt"
        TARGET = 2020

        expense_report = load_input(FILENAME)

        expected = 514579
        actual = get_twosum_product(expense_report, TARGET)

        assert expected == actual

    def test_threesum(self):
        FILENAME = "input/example01_1.txt"
        TARGET = 2020

        expense_report = load_input(FILENAME)

        expected = 241861950
        actual = get_threesum_product(expense_report, TARGET)

        assert expected == actual
