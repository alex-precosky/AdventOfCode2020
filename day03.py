import numpy as np


class Hill():
    """A Hill is a gridular toboggan course. Each square in the grid is a tree or
    is open

    """
    def __init__(self):
        self.width = None
        self.height = None
        self.grid = None  # np.array, 1 is tree, 0 is open

    @classmethod
    def from_string(cls, input_lines):
        return_hill = Hill()

        return_hill.width = len(input_lines[0].strip())
        return_hill.height = len(input_lines)

        return_hill.grid = np.zeros([return_hill.width, return_hill.height])

        for row, row_str in enumerate(input_lines):
            for col, col_str in enumerate(row_str.strip()):
                if col_str == '#':
                    return_hill.grid[col, row] = 1

        return return_hill


class Simulator():
    def __init__(self, hill: Hill, inc_x: int, inc_y: int):
        self.hill: Hill = hill

        self.cur_x = 0
        self.cur_y = 0

        self.inc_x = inc_x
        self.inc_y = inc_y

        self.trees_encountered = 0

    def _step(self):
        self.cur_x = (self.cur_x + self.inc_x) % self.hill.width
        self.cur_y += self.inc_y

        if self.cur_y >= self.hill.height:
            return

        if self.hill.grid[self.cur_x, self.cur_y] == 1:
            self.trees_encountered += 1

    def run_to_completion(self) -> int:
        while self.cur_y < self.hill.height:
            self._step()

        return self.trees_encountered


if __name__ == "__main__":
    INPUT_FILE = 'input/day03.txt'
    INC_X = 3
    INC_Y = 1

    hill = Hill.from_string(open(INPUT_FILE, 'r').readlines())

    # In Part one, we just go down the hill once
    simulator = Simulator(hill, INC_X, INC_Y)
    part1 = simulator.run_to_completion()

    print(f'Part 1: Trees Encountered: {part1}')

    # Part two is going down the hill a few times in different ways
    PART_2_INCREMENTS = ((1, 1),
                         (3, 1),
                         (5, 1),
                         (7, 1),
                         (1, 2))
    product = 1
    for inc_x, inc_y in PART_2_INCREMENTS:
        simulator = Simulator(hill, inc_x, inc_y)
        product *= simulator.run_to_completion()

    print(f'Part 2: Product of trees encountered: {product}')
