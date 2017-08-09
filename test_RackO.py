import unittest
from RackO import RackO


class TestRackO(unittest.TestCase):

    def test_rack_o(self):
        rack_o = RackO(deck_size=10, hand_size=3, deck=[3, 1, 9, 6, 4, 7, 2, 10, 8, 5])
        self.assertEqual(rack_o.check_deck(), 9)
        self.assertEqual(rack_o.check_discard(), 6)
        self.assertEqual(rack_o.game_over(), True)

    def test_rack_o2(self):
        rack_o = RackO(deck_size=10, hand_size=3, deck=[8, 1, 9, 6, 4, 7, 2, 10, 3, 5])
        self.assertEqual(rack_o.check_deck(), 9)
        self.assertEqual(rack_o.check_discard(), 6)
        self.assertEqual(rack_o.game_over(), False)


if __name__ == '__main__':
    unittest.main()
