import unittest
import unittest.mock
from Village import Village


class TestVillage(unittest.TestCase):

    most = 6
    initial = 0
    lowest = 0

    def setUp(self):
        self.test = Village(TestVillage.most)

    def tearDown(self):
        del self.test

    def test_pillagers_init(self):
        self.assertEqual(self.test.pillagers, TestVillage.initial)

    def test_defenders_init(self):
        self.assertEqual(self.test.defenders, TestVillage.initial)

    def test_desolated_init(self):
        self.assertFalse(self.test.desolated)

    def test_abandoned_init(self):
        self.assertFalse(self.test.abandoned)

    def test_start_init(self):
        self.assertFalse(self.test.start)

    def test_most_init(self):
        self.assertEqual(self.test.most, TestVillage.most)

    def test_trade_init(self):
        self.assertFalse(self.test.trade)

    def test_str(self):
        self.assertEqual(str(self.test), (f"""
                pillage_value = {self.test.pillage_value},
                defenders = {self.test.defenders},
                pillagers = {self.test.pillagers},
                desolated = {self.test.desolated},
                abandoned = {self.test.abandoned},
                start tile = {self.test.start},
                trade = {self.test.trade},
                trade_value = {self.test.trade_value}"""))

    def test_change_pillagers_most(self):
        result = self.test.change_pillagers(self.most-self.initial)
        self.assertTrue(result)
        self.assertEqual(self.test.pillagers, self.most)

    def test_change_pillagers_too_much(self):
        result = self.test.change_pillagers(self.most+1)
        self.assertFalse(result)
        self.assertEqual(self.test.pillagers, self.most)

    def test_change_pillagers_minus(self):
        self.test.pillagers = self.initial + 1
        result = self.test.change_pillagers(-1)
        self.assertTrue(result)
        self.assertEqual(self.test.pillagers, self.initial)

    def test_change_pillagers_too_low(self):
        result = self.test.change_pillagers(-1*(self.initial + 1))
        self.assertFalse(result)
        self.assertEqual(self.test.pillagers, self.lowest)

    def test_change_defenders_most(self):
        result = self.test.change_defenders(self.most-self.initial)
        self.assertTrue(result)
        self.assertEqual(self.test.defenders, self.most)

    def test_change_defenders_too_much(self):
        result = self.test.change_defenders(self.most+1)
        self.assertFalse(result)
        self.assertEqual(self.test.defenders, self.most)

    def test_change_defenders_minus(self):
        self.test.defenders = self.initial + 1
        result = self.test.change_defenders(-1)
        self.assertTrue(result)
        self.assertEqual(self.test.defenders, self.initial)

    def test_change_defenders_too_low(self):
        result = self.test.change_defenders(-1*(self.initial + 1))
        self.assertFalse(result)
        self.assertEqual(self.test.defenders, self.lowest)

    def test_abandon_normal(self):
        self.test.abandon()
        self.assertTrue(self.test.abandoned)
        self.assertFalse(self.test.desolated)

    def test_abandon_abandoned(self):
        self.test.abandoned = True
        self.test.abandon()
        self.assertFalse(self.test.abandoned)
        self.assertTrue(self.test.desolated)

    def test_abandon_desolated(self):
        self.test.desolated = True
        self.test.abandon()
        self.assertFalse(self.test.abandoned)
        self.assertTrue(self.test.desolated)

    def test_pillage_no_pillagers(self):
        self.assertEqual(self.test.pillage(), {})

    def test_pillage_desolated(self):
        self.test.pillagers = 1
        self.test.desolated = True
        self.assertEqual(self.test.pillage(), {})

    @unittest.mock.patch.object(Village, "roll_die", return_value=1)
    def test_pillage_abandoned_false(self, mock_roll):
        self.test.pillagers = 1
        self.test.abandoned = True
        self.assertEqual(self.test.pillage(), {})

    @unittest.mock.patch.object(Village, "roll_die", return_value=most//2+1)
    def test_pillage_abandoned_return(self, mock_roll):
        self.test.pillagers = 1
        self.test.abandoned = True
        self.assertEqual(self.test.pillage(), Village.pillage_value)

    def test_pillage_pass(self):
        self.test.pillagers = 1
        self.assertEqual(self.test.pillage(), Village.pillage_value)

    def test_roll_die(self):
        count = 100
        output = True
        while output and count > 0:
            roll = self.test.roll_die()
            if roll > self.most or roll < 1:
                output = False
            count -= 1
        self.assertTrue(output)

    @unittest.mock.patch.object(Village, "roll_die", return_value=1)
    def test_check_defence_low(self, mock_roll):
        self.test.check_defence()
        self.assertEqual(self.test.defenders, self.initial)
        self.assertEqual(self.test.pillagers, self.initial)

    @unittest.mock.patch.object(Village, "roll_die", return_value=most)
    def test_check_defence_most_die(self, mock_roll):
        self.test.check_defence()
        self.assertEqual(self.test.defenders, self.initial)
        self.assertEqual(self.test.pillagers, self.initial)

    @unittest.mock.patch.object(Village, "roll_die", return_value=1)
    def test_check_defence_low_most_defenders(self, mock_roll):
        self.test.defenders = self.most-1
        self.test.check_defence()
        self.assertEqual(self.test.defenders, self.most-1)
        self.assertEqual(self.test.pillagers, self.initial)

    @unittest.mock.patch.object(Village, "roll_die", return_value=1)
    def test_check_defence_over(self, mock_roll):
        self.test.pillagers = 1
        self.test.defenders = self.most
        self.test.check_defence()
        self.assertEqual(self.test.defenders, self.most-1)
        self.assertEqual(self.test.pillagers, 0)

    @unittest.mock.patch.object(Village, "roll_die", return_value=1)
    def test_check_defence_over_extra_pillagers(self, mock_roll):
        self.test.pillagers = 2
        self.test.defenders = self.most
        self.test.check_defence()
        self.assertEqual(self.test.defenders, self.most-1)
        self.assertEqual(self.test.pillagers, 2)

    @unittest.mock.patch.object(Village, "roll_die", return_value=2)
    def test_check_defence_over_two(self, mock_roll):
        self.test.pillagers = 1
        self.test.defenders = self.most
        self.test.check_defence()
        self.assertEqual(self.test.defenders, self.most-2)
        self.assertEqual(self.test.pillagers, 0)

    @unittest.mock.patch.object(Village, "roll_die", return_value=3)
    def test_check_defence_complex(self, mock_roll):
        self.test.pillagers = 3
        self.test.defenders = self.most
        self.test.check_defence()
        self.assertEqual(self.test.defenders, self.most-3)
        self.assertEqual(self.test.pillagers, 2)

    @unittest.mock.patch.object(Village, "roll_die", return_value=1)
    @unittest.mock.patch.object(Village, "abandon")
    def test_check_abandon_pass(self, mock_abandon, mock_roll):
        self.test.check_abandon(0)
        mock_abandon.assert_not_called()

    @unittest.mock.patch.object(Village, "roll_die", return_value=most)
    @unittest.mock.patch.object(Village, "abandon")
    def test_check_abandon_with_fear(self, mock_abandon, mock_roll):
        fear = self.most - 1
        self.test.check_abandon(fear)
        mock_abandon.assert_not_called()

    @unittest.mock.patch.object(Village, "roll_die", return_value=1)
    @unittest.mock.patch.object(Village, "abandon")
    def test_check_abandon_least(self, mock_roll, mock_abandon):
        self.test.check_abandon(1)
        mock_abandon.assert_called()

    @unittest.mock.patch.object(Village, "roll_die", return_value=most)
    @unittest.mock.patch.object(Village, "abandon")
    def test_check_abandon_most(self, mock_roll, mock_abandon):
        self.test.check_abandon(self.most)
        mock_abandon.assert_called()

    @unittest.mock.patch.object(Village, "check_defence")
    @unittest.mock.patch.object(Village, "pillage", return_value={})
    @unittest.mock.patch.object(Village, "check_abandon")
    @unittest.mock.patch.object(Village, "change_pillagers")
    @unittest.mock.patch.object(Village, "check_trade", return_value={})
    def test_complete_turn_trade_false(self, mock_t, mock_ps, mock_a, mock_p, mock_d):  # noqa: E501
        self.assertEqual(self.test.complete_turn(0), {"pillagers": 0})
        mock_ps.assert_called()
        mock_a.assert_called()
        mock_p.assert_called()
        mock_d.assert_called()
        mock_t.assert_not_called()
        self.assertFalse(self.test.trade)

    @unittest.mock.patch.object(Village, "check_defence")
    @unittest.mock.patch.object(Village, "pillage", return_value={})
    @unittest.mock.patch.object(Village, "check_abandon")
    @unittest.mock.patch.object(Village, "change_pillagers")
    @unittest.mock.patch.object(Village, "check_trade", return_value={})
    def test_complete_turn_trade_true(self, mock_t, mock_ps, mock_a, mock_p, mock_d):  # noqa: E501
        self.test.trade = True
        self.assertEqual(self.test.complete_turn(0), {"pillagers": 0})
        mock_ps.assert_called()
        mock_a.assert_called()
        mock_p.assert_not_called()
        mock_d.assert_called()
        mock_t.assert_called()
        self.assertFalse(self.test.trade)

    def test_check_trade_no_pillagers(self):
        self.assertEqual(self.test.check_trade(), {})

    def test_check_trade_desolated(self):
        self.test.pillagers = 1
        self.test.desolated = True
        self.assertEqual(self.test.check_trade(), {})

    def test_check_trade_abandoned_false(self):
        self.test.pillagers = 1
        self.test.abandoned = True
        self.assertEqual(self.test.check_trade(), {})

    def test_check_trade_pass(self):
        self.test.pillagers = 1
        self.assertEqual(self.test.check_trade(), Village.trade_value)
