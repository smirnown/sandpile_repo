from unittest import TestCase
from sandpile import Sandpile


class TestSandpile(TestCase):

    def setUp(self):
        self.sandpile = Sandpile(size=3, max_grains_per_cell=4)

    def test_instantiate_sandpile(self):
        assert self.sandpile.size == 3
        for row in self.sandpile.grid:
            for cell in row:
                assert cell.grains == 0
    
    def test_get_cell(self):
        cell = self.sandpile.get_cell(row_index=0, column_index=0)
        assert cell == self.sandpile.grid[0][0]
    
    def test_get_cell_out_of_range(self):
        cell = self.sandpile.get_cell(row_index=-1, column_index=0)
        assert cell is None

    def test_corner_has_2_adjacent_cells(self):
        corner_cell = self.sandpile.get_cell(row_index=0, column_index=0)
        adjacent_cells = [
            self.sandpile.grid[0][1],
            self.sandpile.grid[1][0]]
        assert len(corner_cell.adjacent_cells) == 2
        assert set(adjacent_cells) == set(corner_cell.adjacent_cells)

    def test_edge_has_3_adjacent_cells(self):
        edge_cell = self.sandpile.get_cell(row_index=0, column_index=1)
        adjacent_cells = [
            self.sandpile.grid[0][0],
            self.sandpile.grid[0][2],
            self.sandpile.grid[1][1]]
        assert len(edge_cell.adjacent_cells) == 3
        assert set(adjacent_cells) == set(edge_cell.adjacent_cells)

    def test_non_edge_has_4_adjacent_cells(self):
        cell = self.sandpile.get_cell(row_index=1, column_index=1)
        adjacent_cells = [
            self.sandpile.grid[0][1],
            self.sandpile.grid[1][0],
            self.sandpile.grid[2][1],
            self.sandpile.grid[1][2]]
        assert len(cell.adjacent_cells) == 4
        assert set(adjacent_cells) ==  set(cell.adjacent_cells)

    def test_move_grains_from_cells_to_adajcent_queues(self):
        cell = self.sandpile.get_cell(row_index=1, column_index=1)
        cell.grains = 5
        self.sandpile.move_grains_from_over_capacity_cells()
        assert cell.grains == 1
        for adjacent_cell in cell.adjacent_cells:
            assert adjacent_cell.grains == 0
            assert adjacent_cell.queued_grains == 1

    def test_queue_up_grains(self):
        cell = self.sandpile.get_cell(row_index=1, column_index=1)
        self.sandpile.queue_up_grains(cells=[cell], number_of_grains=1)
        assert cell.queued_grains == 1

    def test_add_all_queued_grains(self):
        cells = [self.sandpile.get_cell(row_index=0, column_index=0)]
        cells[0].queued_grains = 1
        self.sandpile.add_all_queued_grains()
        assert cells[0].grains == 1
        assert cells[0].queued_grains == 0
