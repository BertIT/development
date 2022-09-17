import unittest

import multiply_arrays


class TestMultiplyArrays(unittest.TestCase):

    def setUp(self) -> None:
        n = 4
        self.positive_numbers = [*range(1, n + 1)]
        self.negative_numbers = [*range(-1, -n - 1, -1)]
        self.numbers_one_zero = [*range(0, n + 1)]
        self.zeros = [0] * n
        self.empty_arr = []

    # positive numbers
    def test_multiply_arr(self):
        self.assertEqual(
            multiply_arrays.multiply_arr(self.positive_numbers),
            [24, 12, 8, 6],
        )
        self.assertEqual(
            multiply_arrays.multiply_arr(self.negative_numbers),
            [-24, -12, -8, -6],
        )
        self.assertEqual(
            multiply_arrays.multiply_arr(self.numbers_one_zero),
            [24, 0, 0, 0, 0],
        )
        self.assertEqual(
            multiply_arrays.multiply_arr(self.zeros),
            [0, 0, 0, 0],
        )
        self.assertEqual(
            multiply_arrays.multiply_arr(self.empty_arr),
            [],
        )

    def test_multiply_arr2(self):
        self.assertEqual(
            multiply_arrays.multiply_arr_2(self.positive_numbers),
            [24, 12, 8, 6],
        )
        self.assertEqual(
            multiply_arrays.multiply_arr_2(self.negative_numbers),
            [-24, -12, -8, -6],
        )
        self.assertEqual(
            multiply_arrays.multiply_arr(self.numbers_one_zero),
            [24, 0, 0, 0, 0],
        )
        self.assertEqual(
            multiply_arrays.multiply_arr_2(self.zeros),
            [0, 0, 0, 0],
        )
        self.assertEqual(
            multiply_arrays.multiply_arr_2(self.empty_arr),
            [],
        )


if __name__ == '__main__':

    unittest.main()
