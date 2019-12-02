import unittest
from advent_of_code.challenges import day_21 as challenge

from advent_of_code.utils import load_answer


class TestDay21(unittest.TestCase):

    def test_part_1(self):
        result = challenge.part1()
        answer = load_answer(21, 1)
        self.assertEqual(str(result), answer)

    def test_part_2(self):
        result = challenge.part2()
        answer = load_answer(21, 2)
        self.assertEqual(str(result), answer)

if __name__ == '__main__':
    unittest.main(verbosity=2)