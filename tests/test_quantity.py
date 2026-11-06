import unittest

from warehouse.quantity import parse_quantity


class QuantityTests(unittest.TestCase):
    def test_positive_quantity(self):
        self.assertEqual(parse_quantity(" 12 "), 12)

    def test_zero_quantity(self):
        for value in ("0", " 0 "):
            with self.subTest(value=value):
                self.assertEqual(parse_quantity(value), 0)

    def test_negative_quantity(self):
        for value in ("-1", " -12 "):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_quantity(value)
