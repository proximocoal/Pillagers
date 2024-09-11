import unittest
import unittest.mock
from Grid import Grid
from Tile import Tile
from Town import Town
from Village import Village


class TestGrid(unittest.TestCase):

    most = 6
    length = 7
    width = 8
    vill_prob = (1, 3)
    vill_range = 2
    town_range = 3
    town_min = 4

    def setUp(self):
        self.test = Grid(TestGrid.most, TestGrid.width, TestGrid.length)

    def tearDown(self):
        del self.test

    def test_init(self):
        self.assertEqual(self.test.length, TestGrid.length)
        self.assertEqual(self.test.width, TestGrid.width)
        self.assertEqual(self.test.most, TestGrid.most)
        self.assertEqual(self.test.grid, [])
        self.assertEqual(self.test.start, (TestGrid.length // 2, 0))
        self.assertEqual(self.test.town_coord, [])
        self.assertEqual(self.test.village_coord, [self.test.start])

    def test_str_empty(self):
        self.assertEqual(str(self.test), "")

    def test_make_grid(self):
        make_grid_res = self.test.make_grid(TestGrid.width, TestGrid.length)
        self.assertEqual(len(make_grid_res), TestGrid.length)
        self.assertEqual(len(make_grid_res[0]), TestGrid.width)
        self.assertEqual(type(make_grid_res[0][0]), Tile)

    def test_str_no_v_t(self):
        self.test.grid = self.test.make_grid(TestGrid.width, TestGrid.length)
        row = "F " * TestGrid.width
        expected = f"\n{row}" * TestGrid.length
        self.assertEqual(str(self.test), expected)

    def test_make_start(self):
        self.test.grid = self.test.make_grid(TestGrid.width, TestGrid.length)
        self.test.make_start()
        len_coord = self.test.start[0]
        width_coord = self.test.start[1]
        self.assertTrue(self.test.grid[len_coord][width_coord].start)

    def test_rand_village(self):
        self.assertTrue(isinstance(self.test.rand_village(), bool))

    @unittest.mock.patch("Grid.randrange", return_value=1)
    def test_rand_village_false(self, mock_rand):
        self.assertFalse(self.test.rand_village())

    @unittest.mock.patch("Grid.randrange", return_value=vill_prob)
    def test_rand_village_true(self, mock_rand):
        self.assertFalse(self.test.rand_village())

    def test_check_vill_coord_empty(self):
        self.assertTrue(self.test.check_vill_coord(1, 1))

    def test_check_vill_coord_same(self):
        self.test.village_coord = [(1, 1)]
        self.assertFalse(self.test.check_vill_coord(1, 1))

    def test_check_vill_coord_lower(self):
        coord = (TestGrid.vill_range - 1, TestGrid.vill_range - 1)
        self.test.village_coord = [coord]
        self.assertFalse(self.test.check_vill_coord(0, 0))

    def test_check_vill_coord_higher(self):
        coord = (TestGrid.vill_range - 1, TestGrid.vill_range - 1)
        self.test.village_coord = [(0, 0)]
        self.assertFalse(self.test.check_vill_coord(coord[0], coord[1]))

    def test_check_vill_coord_too_high(self):
        coord = (TestGrid.vill_range, TestGrid.vill_range - 1)
        self.test.village_coord = [(0, 0)]
        self.assertTrue(self.test.check_vill_coord(coord[0], coord[1]))

    def test_check_vill_coord_too_low(self):
        coord = (TestGrid.vill_range - 1, TestGrid.vill_range)
        self.test.village_coord = [coord]
        self.assertTrue(self.test.check_vill_coord(0, 0))

    def test_check_vill_coord_multiple_false(self):
        coord = (TestGrid.vill_range - 1, TestGrid.vill_range - 1)
        self.test.village_coord = [(10, 10), (20, 20), (0, 0), (30, 30)]
        self.assertFalse(self.test.check_vill_coord(coord[0], coord[1]))

    def test_check_vill_coord_multiple_true(self):
        coord = (TestGrid.vill_range, TestGrid.vill_range)
        self.test.village_coord = [(10, 10), (20, 20), coord, (30, 30)]
        self.assertTrue(self.test.check_vill_coord(0, 0))

    def test_check_town_coord_empty(self):
        self.assertTrue(self.test.check_town_coord(1, 1))

    def test_check_town_coord_same(self):
        self.test.town_coord = [(1, 1)]
        self.assertFalse(self.test.check_town_coord(1, 1))

    def test_check_town_coord_lower(self):
        coord = (TestGrid.town_range - 1, TestGrid.town_range - 1)
        self.test.town_coord = [coord]
        self.assertFalse(self.test.check_town_coord(0, 0))

    def test_check_town_coord_higher(self):
        coord = (TestGrid.town_range - 1, TestGrid.town_range - 1)
        self.test.town_coord = [(0, 0)]
        self.assertFalse(self.test.check_town_coord(coord[0], coord[1]))

    def test_check_town_coord_too_high(self):
        coord = (TestGrid.town_range, TestGrid.town_range - 1)
        self.test.town_coord = [(0, 0)]
        self.assertTrue(self.test.check_town_coord(coord[0], coord[1]))

    def test_check_town_coord_too_low(self):
        coord = (TestGrid.town_range - 1, TestGrid.town_range)
        self.test.town_coord = [coord]
        self.assertTrue(self.test.check_town_coord(0, 0))

    def test_check_town_coord_multiple_false(self):
        coord = (TestGrid.town_range - 1, TestGrid.town_range - 1)
        self.test.town_coord = [(10, 10), (20, 20), (0, 0), (30, 30)]
        self.assertFalse(self.test.check_town_coord(coord[0], coord[1]))

    def test_check_town_coord_multiple_true(self):
        coord = (TestGrid.town_range, TestGrid.town_range)
        self.test.town_coord = [(10, 10), (20, 20), coord, (30, 30)]
        self.assertTrue(self.test.check_town_coord(0, 0))

    def test_check_town_below(self):
        count = 0
        column_count = 0
        row_count = count % TestGrid.town_range
        while count < TestGrid.town_min:
            if row_count == 0:
                column_count += 1
            self.test.village_coord.append((column_count, row_count))
            count += 1
        self.test.check_town()
        self.assertEqual(self.test.town_coord, [])

    def test_check_town_correct(self):
        count = 0
        column_count = 0
        row_count = count % TestGrid.town_range
        while count <= TestGrid.town_min:
            if row_count == 0:
                column_count += 1
            self.test.village_coord.append((column_count, row_count))
            count += 1
        self.test.check_town()
        self.assertEqual(len(self.test.town_coord), 1)

    def test_check_town_extra(self):
        count = 0
        column_count = 0
        row_count = count % TestGrid.town_range
        while count <= TestGrid.town_min+1:
            if row_count == 0:
                column_count += 1
            self.test.village_coord.append((column_count, row_count))
            count += 1
        self.test.check_town()
        self.assertEqual(len(self.test.town_coord), 1)

    def test_make_towns_empty(self):
        self.test.grid = self.test.make_grid(TestGrid.width, TestGrid.length)
        self.test.make_towns(self.test.town_coord)
        checker = False
        for sublist in self.test.grid:
            for obj in sublist:
                if isinstance(obj, Town):
                    checker = True
                    break
        self.assertFalse(checker)

    def test_make_towns_one(self):
        self.test.grid = self.test.make_grid(TestGrid.width, TestGrid.length)
        coord = [(0, 0)]
        self.test.make_towns(coord)
        self.assertTrue(isinstance(self.test.grid[0][0], Town))

    def test_make_towns_multiple(self):
        self.test.grid = self.test.make_grid(TestGrid.width, TestGrid.length)
        len = TestGrid.length - 1
        wid = TestGrid.width - 1
        coord = [(0, 0), (len, wid)]
        self.test.make_towns(coord)
        self.test.make_towns(coord)
        self.assertTrue(isinstance(self.test.grid[0][0], Town))
        self.assertTrue(isinstance(self.test.grid[len][wid], Town))

    @unittest.mock.patch.object(Grid, "rand_village", return_value=False)
    def test_make_villages_false_rand(self, mock_rand):
        self.test.grid = self.test.make_grid(TestGrid.width, TestGrid.length)
        self.test.make_villages()
        checker = False
        for sublist in self.test.grid:
            for obj in sublist:
                if isinstance(obj, Village):
                    checker = True
                    break
        self.assertFalse(checker)

    @unittest.mock.patch.object(Grid, "rand_village", return_value=True)
    @unittest.mock.patch.object(Grid, "check_vill_coord", return_value=False)
    def test_make_villages_false_check(self, mock_rand, mock_check):
        self.test.grid = self.test.make_grid(TestGrid.width, TestGrid.length)
        self.test.make_villages()
        checker = False
        for sublist in self.test.grid:
            for obj in sublist:
                if isinstance(obj, Village):
                    checker = True
                    break
        self.assertFalse(checker)

    @unittest.mock.patch.object(Grid, "rand_village", return_value=True)
    @unittest.mock.patch.object(Grid, "check_vill_coord", return_value=True)
    def test_make_villages_all(self, mock_rand, mock_check):
        self.test.grid = self.test.make_grid(TestGrid.width, TestGrid.length)
        self.test.make_villages()
        checker = False
        for sublist in self.test.grid:
            for obj in sublist:
                if not isinstance(obj, Village):
                    checker = True
                    break
        self.assertFalse(checker)

    def test_complete_grid_true(self):
        self.assertTrue(self.test.complete_grid())
        self.assertEqual(len(self.test.grid), TestGrid.length)
        self.assertTrue(len(self.test.village_coord) > 1)
        self.assertTrue(len(self.test.town_coord) > 0)

    def test_complete_grid_false(self):
        self.test.length = TestGrid.vill_range
        self.test.width = TestGrid.vill_range
        self.test.start = (self.test.length // 2, 0)
        self.assertFalse(self.test.complete_grid())
        self.assertEqual(len(self.test.grid), TestGrid.vill_range)
        self.assertEqual(len(self.test.town_coord), 0)
