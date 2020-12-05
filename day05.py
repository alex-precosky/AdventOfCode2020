import sys


def divide_row_and_seat(input_str):
    '''
    Take input str, and divide it into two strings to return.
    The first will be used to determine row, the other to determine column
    '''
    row = input_str[0:7]
    col = input_str[7:10]

    return row, col


def row_str_to_row(row_str):
    return_int = 0
    ROW_BITS = 7

    for i, ch in enumerate(row_str):
        if ch == 'B':
            return_int |= 1 << (ROW_BITS -i - 1)

    return return_int


def col_str_to_col(col_str):
    return_int = 0
    COL_BITS = 3

    for i, ch in enumerate(col_str):
        if ch == 'R':
            return_int |= 1 << (COL_BITS -i - 1)

    return return_int


def get_seat_id_for_boarding_pass(boarding_pass_str):
    row_str, col_str = divide_row_and_seat(boarding_pass_str)

    row = row_str_to_row(row_str)
    col = col_str_to_col(col_str)

    seat_id = 8 * row + col

    return seat_id


if __name__ == "__main__":

    # Find the maximum seat ID for part one. Also find the min seat ID
    boarding_pass_ids = [x.strip() for x in open('input/day05.txt', 'r').readlines()]
    max_seat_id = 0
    min_seat_id = sys.maxsize
    seat_ids = set()
    for boarding_pass_id in boarding_pass_ids:
        seat_id = get_seat_id_for_boarding_pass(boarding_pass_id)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
        if seat_id < min_seat_id:
            min_seat_id = seat_id
        seat_ids.add(seat_id)
        
    print(f'Part 1: Maximum seat id is {max_seat_id}')

    # For part 2, go through the set of seat IDs found, starting at the min seat
    # ID to the max seat ID, and print out any missing ones. There should be
    # just one. And that's our seat!
    for seat_id in range(min_seat_id, max_seat_id):
        if seat_id not in seat_ids:
            print(f'Part 2: Our seat is: {seat_id}')
            exit()
