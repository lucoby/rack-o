import unittest
from RackO import RackO

class TestRackO(unittest.TestCase):

    def test_rack_o(self):
        rack_o = RackO(deck_size=10, hand_size=3, deck=[3, 1, 9, 6, 4, 7, 2, 10, 8, 5])


if __name__ == '__main__':
    unittest.main()
