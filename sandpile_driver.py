"""Iteratively executes the sandpile."""
from sandpile import Sandpile
from sandpile_view import SandpileView

class SandpileDriver:
    """Executes sandpile."""

    def __init__(self, size, max_grains_per_cell, iterations, source_coordinates_list):
        self.sandpile = Sandpile(size, max_grains_per_cell)
        self.iterations = iterations
        self.view = SandpileView(self.sandpile)
        self.sources = []
        for coordinates in source_coordinates_list:
            self.sources += [self.sandpile.get_cell(row_index=coordinates[0], column_index=coordinates[1])]

    def execute_sandpile(self):
        for _ in range(self.iterations):
            self.sandpile.queue_up_grains(cells=self.sources, number_of_grains=1)

            attempts_until_break = 100
            while_loop_iterations = 0
            while True and (while_loop_iterations < attempts_until_break):
                while_loop_iterations += 1

                over_capacity_cells = []
                cells_with_queued_grains = []
                for row in self.sandpile.grid:
                    for cell in row:
                        if cell.grains > cell.max_grains:
                            over_capacity_cells.append(cell)
                        if cell.queued_grains > 0:
                            cells_with_queued_grains.append(cell)

                if over_capacity_cells:
                    self.sandpile.move_grains_from_over_capacity_cells()
                elif cells_with_queued_grains:
                    self.sandpile.add_all_queued_grains()
                else:
                    break

            self.view.display_sandpile()
            print()
