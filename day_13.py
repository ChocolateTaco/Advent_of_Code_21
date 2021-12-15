import csv

x_max = 0
y_max = 0
lines = []
with open('day_13_input.txt', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',', quotechar='|')
    print(csvreader)
    for row in csvreader:
        lines.append(row)
        # print(', '.join(row))
    print(lines)

    # Finding the x and y bounds
    for line in lines:
        if int(line[0]) > x_max:
            x_max = int(line[0])
        if int(line[1]) > y_max:
            y_max = int(line[1])

print(x_max, y_max)

class Grid():
    def __init__(self, x_length, y_length):
        self._x = x_length
        self._y = y_length
        self._grid = []
        for row in range(self._y):
            self._grid.append([])
            for column in range(self._x):
                self._grid[row].append(".")

    def print_grid(self):
        for row in self._grid:
            print(row)

    def fold_along(self, folding_spot):
        pass

example = Grid(x_max, y_max)
example.print_grid()
