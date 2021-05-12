import unittest
from multielo import Player, Match

class TestMatch(unittest.TestCase):

    def test_calculate_place(self):
        match = Match([Player("001", 3), Player("002", 1), Player("003", 2)])
        match.calcualte_place()
        self.assertEqual(3, match.get_player("001").place)

        match = Match([Player("001", 2), Player("002", 1), Player("003", 2)])
        match.calcualte_place()
        self.assertEqual(2.5, match.get_player("001").place)

        match = Match([Player("001", 2), Player("002", 1), Player("003", 2), Player("0004", 2)])
        match.calcualte_place()
        self.assertEqual(3, match.get_player("001").place)

        match = Match([Player("001", 2), Player("002", 1), Player("003", 2), Player("0004", 2), Player("005", 1)])
        match.calcualte_place()
        self.assertEqual(4, match.get_player("001").place)

    def test_calculate_rating(self):
        match = Match([Player("001", 3), Player("002", 1), Player("003", 2)])
        match.calculate_rating()
        self.assertGreater(match.get_player("002").post_rating, match.get_player("003").post_rating)
        self.assertGreater(match.get_player("003").post_rating, match.get_player("001").post_rating)

        match = Match([Player("001", 2), Player("002", 1), Player("003", 1), Player("004",3)])
        match.calculate_rating()
        self.assertEqual(match.get_player("002").post_rating, match.get_player("003").post_rating)
        self.assertGreater(match.get_player("003").post_rating, match.get_player("001").post_rating)
        self.assertGreater(match.get_player("001").post_rating, match.get_player("004").post_rating)

        match = Match([Player("001", 1), Player("002", 1), Player("003", 1)])
        match.calculate_rating()
        self.assertEqual(match.get_player("001").post_rating, match.get_player("002").post_rating)
        self.assertEqual(match.get_player("001").post_rating, match.get_player("003").post_rating)

        match = Match([Player("001", 1, 1600), Player("002", 1, 1500), Player("003", 1, 1200)])
        match.calculate_rating()
        self.assertGreater(match.get_player("001").post_rating, match.get_player("002").post_rating)
        self.assertGreater(match.get_player("001").post_rating, match.get_player("003").post_rating)
        self.assertGreater(1600, match.get_player("001").post_rating)
        self.assertGreater(1500, match.get_player("002").post_rating)
        self.assertLess(1200, match.get_player("003").post_rating)

        match = Match([Player("001", 2, 1600), Player("002", 1, 1400), Player("003", 2, 1200), Player("004", 2, 1100), Player("005", 1, 1500)])
        match.calculate_rating()
        print(match.get_player("001").post_rating)
        print(match.get_player("002").post_rating)
        print(match.get_player("003").post_rating)
        print(match.get_player("004").post_rating)
        print(match.get_player("005").post_rating)

if __name__ == "__main__":
    unittest.main()
