from typing import List


def find_product_of_sum_of_joltage_adaptor_trees(numbers: List[int]):
    '''numbers: List of adaptor joltages. Last element is the device joltage'''
    current_joltage = 0
    device_joltage = numbers[-1]  # last element is the device joltage

    joltage_boost_1_count = 0
    joltage_boost_3_count = 0

    while current_joltage < device_joltage:
        joltage_boost = numbers[0] - current_joltage

        if joltage_boost == 1:
            joltage_boost_1_count += 1
        elif joltage_boost == 3:
            joltage_boost_3_count += 1
        current_joltage += joltage_boost
        numbers = numbers[1:]

    return joltage_boost_1_count * joltage_boost_3_count


def dp_dfs_find_number_of_combinations(numbers: List[int], joltage, memo):
    '''numbers: List of adaptor joltages. Last element is the device joltage
       joltage: the base joltage we want to count the combinations we can build up from
       memo: dict of k: base joltage v: count of combinations we can build up from this joltage'''
    if joltage in memo:
        return memo[joltage]

    device_joltage = numbers[-1]

    if joltage == device_joltage:
        return 1

    sum1 = 0
    sum2 = 0
    sum3 = 0

    if joltage + 1 in numbers:
        sum1 = dp_dfs_find_number_of_combinations(numbers, joltage + 1, memo)

    if joltage + 2 in numbers:
        sum2 = dp_dfs_find_number_of_combinations(numbers, joltage + 2, memo)

    if joltage + 3 in numbers:
        sum3 = dp_dfs_find_number_of_combinations(numbers, joltage + 3, memo)

    memo[joltage] = sum1 + sum2 + sum3

    return sum1 + sum2 + sum3


if __name__ == "__main__":
    INPUT_FILE = 'input/example10_1.txt'
    DEVICE_JOLTAGE_BOOST = 3
#   INPUT_FILE = 'input/example10_2.txt'
#   INPUT_FILE = 'input/day10.txt'

    numbers = sorted([int(line.strip()) for line in open(INPUT_FILE, 'r').readlines()])
    numbers.append(numbers[-1] + DEVICE_JOLTAGE_BOOST)

    part1 = find_product_of_sum_of_joltage_adaptor_trees(numbers)
    print(f'The joltage differences sum product is: {part1}')

    memo = dict()  # k: adaptor joltage  v: number of combinations on can make with that joltage
    part2 = dp_dfs_find_number_of_combinations(numbers, 0, memo)
    print(f'The number of combinations is: {part2}')
