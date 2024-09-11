import unittest
import unittest.mock
from Grid import Grid


class TestGrid(unittest.TestCase):

    def set_up(self):
        self.test = Grid(6, 6, 6)

    def tear_down(self):
        del self.test
