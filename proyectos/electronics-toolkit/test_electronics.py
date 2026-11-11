import unittest
from electronics import calculate


class ElectronicsTests(unittest.TestCase):
    def test_examples(self):
        for operation, values, expected in [
            ("ohm", [5, 1000], .005),
            ("gain", [1000, 10000], -10),
            ("divider", [5, 1000, 1000], 2.5),
            ("parallel", [100, 100], 50),
            ("rc", [1000, .000001], .001),
            ("median", [3, 100, 2], 3),
        ]:
            with self.subTest(operation=operation):
                self.assertAlmostEqual(calculate(operation, values), expected)

    def test_invalid(self):
        for values in [[0, 10], [-1, 10], [float("nan"), 10], [float("inf"), 10], [10]]:
            with self.subTest(values=values), self.assertRaises(ValueError):
                calculate("gain", values)


if __name__ == "__main__":
    unittest.main()
