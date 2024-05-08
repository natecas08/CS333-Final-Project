import unittest
from checkWin import CheckWin
from getRandWord import GetRandWord
from settings import Settings

class TestWinCondition(unittest.TestCase):

    def test_win_true(self):
        self.assertTrue(CheckWin(True, "word", 5))

    def test_win_false(self):
        self.assertFalse(CheckWin(False, "word", 7))

class TestRandWord(unittest.TestCase):

    def test_easy_not_null(self):
        self.assertIsNotNone(GetRandWord("easy"))

    def test_medium_not_null(self):
        self.assertIsNotNone(GetRandWord("medium"))

    def test_hard_not_null(self):
        self.assertIsNotNone(GetRandWord("hard"))

    def test_combo_not_null(self):
        self.assertIsNotNone(GetRandWord("combo"))

    #def test_custom_not_null(self):
    #    self.assertIsNotNone(GetRandWord("custom"))

class TestSettings(unittest.TestCase):

    def test_easy_return(self):
        self.assertEqual(Settings('a'), "easy")

    def test_medium_return(self):
        self.assertEqual(Settings('b'), "medium")

    def test_hard_return(self):
        self.assertEqual(Settings('c'), "hard")

    def test_combo_return(self):
        self.assertEqual(Settings('d'), "combo")

    def test_custom_return(self):
        self.assertEqual(Settings('e'), "wrong")

if __name__ == '__main__':
    unittest.main()