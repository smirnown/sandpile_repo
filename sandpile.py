"""Sandpile class."""

from cell import Cell


class Sandpile:
    """A grid of cells"""

    def __init__(self, size, max_grains_per_cell):
        self.size = size
        self.__initialize_grid(max_grains_per_cell)

    def __initialize_grid(self, max_grains_per_cell):
        self.grid = [None] * self.size
        for _ in range(self.size):
            self.grid[_] = [Cell(max_grains_per_cell) for _ in range(self.size)] 

        row_index = 0
        for row in self.grid:
            column_index = 0
            for cell in row:
                cell_above = self.get_cell(row_index, column_index - 1)
                cell_below = self.get_cell(row_index, column_index + 1)
                cell_to_the_left = self.get_cell(row_index - 1, column_index)
                cell_to_the_right = self.get_cell(row_index + 1, column_index)

                cell.adjacent_cells += [cell_above] if cell_above is not None else []
                cell.adjacent_cells += [cell_below] if cell_below is not None else []
                cell.adjacent_cells += [cell_to_the_left] if cell_to_the_left is not None else []
                cell.adjacent_cells += [cell_to_the_right] if cell_to_the_right is not None else []

                column_index += 1
            row_index += 1

    def get_cell(self, row_index, column_index):
        """Returns cell at specified coordinates."""
        try:
            assert 0 <= row_index < self.size
            assert 0 <= column_index < self.size
            desired_cell = self.grid[row_index][column_index]
        except AssertionError:
            desired_cell = None
        return desired_cell

    def queue_up_grains(self, cells, number_of_grains):
        """Add grains to the queues of specified cells."""
        for cell in cells:
            cell.queue_up_grains(number_of_grains)

    def add_all_queued_grains(self):
        """Add all all grains in each cell's queue to the cell."""
        for row in self.grid:
            for cell in row:
                if cell.queued_grains > 0:
                    cell.add_queued_grains()

    def move_grains_from_over_capacity_cells(self):
        """Remove grains from over capacity cells and them to adjacent_cells_queues."""
        for row in self.grid:
            for cell in row:
                if cell.grains > cell.max_grains:
                    cell.move_grains()

    def display_grid(self):
        """Display the number of grains per cell in the sandpile represented as a square grid."""
        for row in self.grid:
            print([cell.grains for cell in row])
