'''Cell class'''

class Cell:
    '''An object that contains grains'''

    def __init__(self, max_grains):
        self.grains = 0
        self.queued_grains = 0
        self.max_grains = max_grains
        self.adjacent_cells = []

    def queue_up_grains(self, number_of_grains):
        """Add a grain to the cell's queue."""
        self.queued_grains += number_of_grains

    def add_queued_grains(self):
        """Add all grains in the queue to the cell"""
        self.grains += self.queued_grains
        self.queued_grains = 0

    def move_grains(self):
        """Move a grain to each adjacent cell's queue if grains > max_grains, so long as grains stays non-negative."""
        if self.grains > self.max_grains:
            for adjacent_cell in self.adjacent_cells:
                if self.grains > 0:
                    adjacent_cell.queue_up_grains(number_of_grains=1)
                    self.grains -= 1
    
