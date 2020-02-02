from unittest import TestCase
from cell import Cell


class TestCell(TestCase):

    def setUp(self):
        self.cell = Cell(1)
        self.cell.grains = 2
        self.cell.adjacent_cells = [Cell(1)]

    def test_add_grains_to_queue(self):
        self.cell.queue_up_grains(1)
        assert self.cell.grains == 2
        assert self.cell.queued_grains == 1

    def test_move_grain_above_capacity(self):
        self.cell.move_grains()
        assert self.cell.grains == 1
        assert self.cell.adjacent_cells[0].grains == 0
        assert self.cell.adjacent_cells[0].queued_grains == 1

    def test_move_grain_not_above_capacity(self):
        self.cell.grains = 1
        self.cell.move_grains()
        assert self.cell.grains == 1
        assert self.cell.adjacent_cells[0].queued_grains == 0

    def test_move_grain_not_enough_grains(self):
        self.cell.adjacent_cells.extend([Cell(1), Cell(1)])
        self.cell.move_grains()
        assert self.cell.grains == 0
        assert self.cell.adjacent_cells[0].queued_grains == 1
        assert self.cell.adjacent_cells[1].queued_grains == 1
        assert self.cell.adjacent_cells[2].queued_grains == 0

    def test_add_queued_grains(self):
        self.cell.queued_grains = 1
        self.cell.add_queued_grains()
        assert self.cell.grains == 3
