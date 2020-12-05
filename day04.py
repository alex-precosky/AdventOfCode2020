import re


def validate(key: str, value: str) -> bool:
    if 'byr' == key:
        if value.isdigit() is False:
            return False

        if (int(value) < 1920) or (int(value) > 2002):
            return False

    elif 'iyr' == key:
        if value.isdigit() is False:
            return False

        if (int(value) < 2010) or (int(value) > 2020):
            return False

    elif 'eyr' == key:
        if value.isdigit() is False:
            return False

        if (int(value) < 2020) or (int(value) > 2030):
            return False

    elif 'hgt' == key:
        mx = re.match(r'(\d+)(cm|in)', value)
        if mx is None:
            return False

        unit = mx.groups()[1]
        measure = int(mx.groups()[0])

        if unit == 'cm':
            if (measure < 150) or (measure > 193):
                return False
        elif unit == 'in':
            if (measure < 59) or (measure > 76):
                return False

    elif 'hcl' == key:
        mx = re.match('#[0-9a-f]{6}', value)
        if mx is None:
            return False

    elif 'ecl' == key:
        valid_colors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
        if value not in valid_colors:
            return False

    elif 'pid' == key:
        mx = re.match('^[0-9]{9}$', value)
        if mx is None:
            return False

    return True


def is_passport_valid(passport_dict: dict, is_strict: bool) -> bool:
    '''Return True if all of the required keys are present in passport_dict'''
    required_keys = ('byr',
                     'iyr',
                     'eyr',
                     'hgt',
                     'hcl',
                     'ecl',
                     'pid')

    for required_key in required_keys:
        if required_key not in passport_dict:
            return False

        if is_strict is True:
            if validate(required_key, passport_dict[required_key]) is False:
                return False

    return True


def read_passport(passport_str):
    passport = dict()
    passport_str = passport_str.replace('\n', ' ')
    elements = passport_str.split(' ')

    for element in elements:
        k, v = element.split(':')
        passport[k] = v

    return passport


def read_passports(input_str):
    splitted = input_str.split('\n\n')
    passport_strs = [x.strip() for x in splitted]

    passports = [read_passport(passport_str) for passport_str in passport_strs]
    return passports


if __name__ == "__main__":
    # INPUT_FILE = 'input/example04_1.txt'
    # INPUT_FILE = 'input/example04_4valid.txt'
    # INPUT_FILE = 'input/example04_0valid.txt'
    INPUT_FILE = 'input/day04.txt'
    input_str = open(INPUT_FILE).read()

    num_valid_passports = 0
    passports = read_passports(input_str)
    for passport in passports:
        if is_passport_valid(passport, is_strict=False) is True:
            num_valid_passports += 1

    print(f'Part 1: Number of valid passports: {num_valid_passports}')

    num_valid_passports = 0
    for passport in passports:
        if is_passport_valid(passport, is_strict=True) is True:
            num_valid_passports += 1

    print(f'Part 2: Number of valid passports: {num_valid_passports}')
