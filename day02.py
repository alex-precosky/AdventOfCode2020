from typing import NamedTuple
from typing import List
import re


class PasswordRule(NamedTuple):
    letter: str
    min_count: int
    max_count: int

    @classmethod
    def from_string(cls, input_str):
        '''@param input_str for example: "1-3 a" means letter a must appear 1 to 3
        times. Except in part 2, it means 'a' must appear in exactly one of
        position 1 or 3

        '''
        letter = input_str[-1]

        min_count = int(re.search('\d+', input_str).group())
        max_count = int(re.search('(?<=-)\d+', input_str).group())

        return PasswordRule(letter, min_count, max_count)

    def __repr__(self):
        return f'letter: {self.letter}, min_count: {self.min_count} max_count: {self.max_count}'


def is_password_valid_part1(line: str) -> bool:
    line_parts = line.split(':')
    rule_str = line_parts[0]
    password_str = line_parts[1].strip()

    rule = PasswordRule.from_string(rule_str)

    letter_dict = dict()

    for char in password_str:
        if char not in letter_dict:
            letter_dict[char] = 1
        else:
            letter_dict[char] += 1

    if rule.letter not in letter_dict:
        return False
    else:
        if letter_dict[rule.letter] < rule.min_count:
            return False
        if letter_dict[rule.letter] > rule.max_count:
            return False

    return True


def is_password_valid_part2(line: str) -> bool:
    line_parts = line.split(':')
    rule_str = line_parts[0]
    password_str = line_parts[1].strip()

    rule = PasswordRule.from_string(rule_str)

    found_one = False

    if rule.min_count > len(password_str):
        return False

    if rule.max_count > len(password_str):
        return False

    if password_str[rule.min_count - 1] == rule.letter:
        found_one = True

    if password_str[rule.max_count - 1] == rule.letter:
        if found_one is True:
            return False
        else:
            return True

    if found_one is True:
        return True

    return False


def count_valid_passwords_part1(lines: List[str]) -> int:
    valid_count = 0
    for line in lines:
        if is_password_valid_part1(line):
            valid_count += 1

    return valid_count


def count_valid_passwords_part2(lines: List[str]) -> int:
    valid_count = 0
    for line in lines:
        if is_password_valid_part2(line):
            valid_count += 1

    return valid_count


if __name__ == '__main__':
    INPUT_FILE = 'input/day02.txt'

    input_lines = [line.strip() for line in open(INPUT_FILE, 'r').readlines()]

    part1 = count_valid_passwords_part1(input_lines)
    print(f'Part1: There are {part1} valid passwords')

    part2 = count_valid_passwords_part2(input_lines)
    print(f'Part2: There are {part2} valid passwords')
