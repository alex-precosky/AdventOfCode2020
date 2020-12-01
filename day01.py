def get_twosum_product(expense_report: list, target: int) -> int:
    required_items = dict()

    for expense in expense_report:
        required_items[expense] = target - expense

    for item in required_items.items():
        if item[1] in required_items:
            return item[0] * item[1]

    return None

def get_threesum_product(expense_report: list, target: int) -> int:
    for expense in expense_report:
        twosum_target = target - expense
        twosum_product = get_twosum_product(expense_report, twosum_target)
        if twosum_product is not None:
            return twosum_product * expense


def load_input(file_name: str) -> list:
    return [int(x.strip()) for x in open(file_name).readlines()]

if __name__ == "__main__":
    FILENAME = "input/day01.txt"
    TARGET = 2020

    expense_report = load_input(FILENAME)

    twosum_product = get_twosum_product(expense_report, TARGET)
    print(f"Part 1: {twosum_product}")

    threesum_product = get_threesum_product(expense_report, TARGET)
    print(f"Part 2: {threesum_product}")
