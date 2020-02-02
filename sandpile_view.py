import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from sandpile import Sandpile
import time

class SandpileView:
    """Visually displays the number of grains per cell, laid out in a square grid."""

    def __init__(self, sandpile):
        self.sandpile = sandpile

    def display_sandpile(self):
        """Display number of grains per cell as a 2D histogram."""
        row_indices, column_indices = self.__get_coordinate_vectors_for_grains()
        # fig, axs = plt.subplots(1, 1, figsize=(5, 5), sharex=True, sharey=True,
        #                         tight_layout=True)

        # axs.hist2d(row_indices, column_indices, bins=self.sandpile.size, norm=colors.LogNorm())
        # plt.show()

        plt.ion()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.hist2d(row_indices, column_indices, bins=self.sandpile.size, norm=colors.LogNorm())
        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(1)

    def __get_coordinate_vectors_for_grains(self):
        """Constructs a list of the row indices of all grains, and another list for column indices."""
        row_indices_of_grains = []
        column_indices_of_grains = []
        row_index = 0
        for row in self.sandpile.grid:
            row_index += 1
            column_index = 0
            for cell in row:
                column_index += 1
                row_indices_of_grains += [row_index] * cell.grains
                column_indices_of_grains += [column_index] * cell.grains
        return (row_indices_of_grains, column_indices_of_grains)
