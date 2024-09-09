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

    def setUp(self):
        self.test = Wagon(TestWagon.most)

    def tearDown(self):
        del self.test

    def test_init_pillagers(self):
        assert self.test.pillagers == TestWagon.initial

    def test_init_gold(self):
        assert self.test.gold == TestWagon.initial

    def test_init_rations(self):
        assert self.test.rations == TestWagon.initial

    def test_init_fear(self):
        assert self.test.fear == TestWagon.initial

    def test_init_location(self):
        assert self.test.location == (TestWagon.initial, TestWagon.initial)

    def test_init_hate(self):
        assert self.test.hate == TestWagon.initial

    def test_change_fear_high(self):
        assert self.test.change_fear(TestWagon.high) is True
        assert self.test.fear == TestWagon.most

    def test_change_fear_too_high(self):
        assert self.test.change_fear(TestWagon.too_high) is True
        assert self.test.fear == TestWagon.most

    def test_change_fear_low(self):
        assert self.test.change_fear(TestWagon.low) is True
        assert self.test.fear == TestWagon.least

    def test_change_fear_too_low(self):
        assert self.test.change_fear(TestWagon.too_low) is False
        assert self.test.fear == TestWagon.initial

    def test_change_hate_high(self):
        assert self.test.change_hate(TestWagon.high) is True
        assert self.test.hate == TestWagon.most

    def test_change_hate_too_high(self):
        assert self.test.change_hate(TestWagon.too_high) is True
        assert self.test.hate == TestWagon.most

    def test_change_hate_low(self):
        assert self.test.change_hate(TestWagon.low) is True
        assert self.test.hate == TestWagon.least

    def test_change_hate_too_low(self):
        assert self.test.change_hate(TestWagon.too_low) is False
        assert self.test.hate == TestWagon.initial

    def test_change_gold_high(self):
        assert self.test.change_gold(TestWagon.high) is True
        assert self.test.gold == TestWagon.most

    def test_change_gold_too_high(self):
        assert self.test.change_gold(TestWagon.too_high) is True
        assert self.test.gold == TestWagon.most

    def test_change_gold_low(self):
        assert self.test.change_gold(self.low) is True
        assert self.test.gold == TestWagon.least

    def test_change_gold_too_low(self):
        assert self.test.change_gold(self.too_low) is False
        assert self.test.gold == TestWagon.initial

    def test_change_rations_high(self):
        assert self.test.change_rations(TestWagon.high) is True
        assert self.test.rations == TestWagon.most

    def test_change_rations_too_high(self):
        assert self.test.change_rations(TestWagon.too_high) is True
        assert self.test.rations == TestWagon.most

    def test_change_rations_low(self):
        assert self.test.change_rations(TestWagon.low) is True
        assert self.test.rations == TestWagon.least

    def test_change_rations_too_low(self):
        assert self.test.change_rations(TestWagon.too_low) is False
        assert self.test.rations == TestWagon.initial

    @unittest.skip("Function not written")
    def test_change_pillagers_high(self):
        assert self.test.change_pillagers(TestWagon.high) is True
        self.assertEqual(self.test.pillagers, TestWagon.most)

    @unittest.skip("Function not written")
    def test_change_pillagers_too_high(self):
        assert self.test.change_pillagers(TestWagon.too_high) is True
        assert self.test.pillagers == TestWagon.most

    @unittest.skip("Function not written")
    def test_change_pillagers_low(self):
        assert self.test.change_pillagers(TestWagon.low) is True
        assert self.test.pillagers == TestWagon.least

    @unittest.skip("Function not written")
    def test_change_pillagers_too_low(self):
        assert self.test.change_pillagers(TestWagon.too_low) is False
        assert self.test.pillagers == TestWagon.initial

    @unittest.skip("Test not written")
    def test_change_location_high(self):
        pass

    @unittest.skip("Test not written")
    def test_change_location_too_high(self):
        pass

    @unittest.skip("Test not written")
    def test_change_location_low(self):
        pass

    @unittest.skip("Test not written")
    def test_change_location_too_low(self):
        pass

    def test_change_stat_fear(self):
        assert self.test.change_stat('fear', TestWagon.high) is True
        assert self.test.fear == TestWagon.most

    def test_change_stat_hate(self):
        assert self.test.change_stat('hate', TestWagon.high) is True
        assert self.test.hate == self.most

    def test_change_stat_gold(self):
        assert self.test.change_stat('gold', TestWagon.high) is True
        assert self.test.gold == TestWagon.most

    def test_change_stat_rations(self):
        assert self.test.change_stat('rations', TestWagon.high) is True
        assert self.test.rations == TestWagon.most

    @unittest.skip("Function not written")
    def test_change_stat_pillagers(self):
        assert self.test.change_stat('pillagers', TestWagon.high) is True
        assert self.test.pillagers == TestWagon.most

    @unittest.skip("Test not written")
    def test_change_stat_location(self):
        pass

    def test_change_stat_fail(self):
        with self.assertRaisesRegex(ValueError,
                                    """Stat not recognised. Must be:
                fear,
                hate,
                gold,
                rations,
                pillagers
                or location"""):
            self.test.change_stat(1, TestWagon.high)

    def test_str(self):
        assert str(self.test) == (f"""fear = {self.test.fear},
                   hate = {self.test.hate},
                   gold = {self.test.gold},
                   rations = {self.test.rations},
                   location = {self.test.location}
                   pillagers = {self.test.pillagers}
                   """)

    def test_check_loss_both(self):
        assert self.test.check_loss() is True

    def test_check_loss_pillagers(self):
        self.test.rations = 1
        assert self.test.check_loss() is True

    def test_check_loss_rations(self):
        self.test.pillagers = 1
        assert self.test.check_loss() is True

    def test_check_loss_neither(self):
        self.test.pillagers = 1
        self.test.rations = 1
        assert self.test.check_loss() is False
