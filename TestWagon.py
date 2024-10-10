import unittest
from Wagon import Wagon


class TestWagon(unittest.TestCase):
    initial = 0
    most = 6
    least = 0
    high = most - initial
    too_high = high + 1
    low = 0
    too_low = low - 1
    stats = Wagon.stat_keys
    not_stat = "fish"
    not_int = 0.5

    def setUp(self):
        self.test = Wagon(TestWagon.most)
        self.most = TestWagon.most

    def tearDown(self):
        del self.test

    def test_init(self):
        for stat in TestWagon.stats:
            self.assertEqual(self.test.stats[stat], TestWagon.initial)
        self.assertEqual(self.test.most, TestWagon.most)

    def test_change_stat_high(self):
        for stat in TestWagon.stats:
            self.assertEqual(self.test.change_stat(stat, TestWagon.high), TestWagon.high)  # noqa: E501
            self.assertEqual(self.test.stats[stat], TestWagon.most)

    def test_change_stat_too_high(self):
        for stat in TestWagon.stats:
            self.assertEqual(self.test.change_stat(stat, TestWagon.too_high), TestWagon.most)  # noqa: E501
            self.assertEqual(self.test.stats[stat], TestWagon.most)

    def test_change_stat_low(self):
        for stat in TestWagon.stats:
            self.assertEqual(self.test.change_stat(stat, TestWagon.low), TestWagon.low)  # noqa: E501
            self.assertEqual(self.test.stats[stat], TestWagon.least)

    def test_change_stat_too_low(self):
        for stat in TestWagon.stats:
            self.assertEqual(self.test.change_stat(stat, TestWagon.too_low), TestWagon.least)  # noqa: E501
            self.assertEqual(self.test.stats[stat], TestWagon.least)

    def test_change_stat_not_int(self):
        with self.assertRaises(ValueError):
            for stat in TestWagon.stats:
                self.test.change_stat(stat, TestWagon.not_int)
        self.assertEqual(self.test.stats[stat], TestWagon.initial)

    def test_change_stat_fail(self):
        with self.assertRaises(KeyError):
            self.test.change_stat(TestWagon.not_stat, TestWagon.high)
        with self.assertRaises(KeyError):
            self.test.stats[TestWagon.not_stat]

    def test_str(self):
        self.assertEqual(str(self.test), f"{self.test.stats}, max = {self.most}")  # noqa: E501

    def test_check_loss_both(self):
        self.assertTrue(self.test.check_loss())

    def test_check_loss_pillagers(self):
        self.test.change_stat("rations", 1)
        self.assertTrue(self.test.check_loss())

    def test_check_loss_rations(self):
        self.test.change_stat("pillagers", 1)
        self.assertTrue(self.test.check_loss() is True)

    def test_check_loss_neither(self):
        self.test.change_stat("pillagers", 1)
        self.test.change_stat("rations", 1)
        self.assertFalse(self.test.check_loss())
