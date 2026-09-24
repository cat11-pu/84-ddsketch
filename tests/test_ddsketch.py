import unittest

from ddsketch import Sketch
from quantapi import Quantiles


class TestSketch(unittest.TestCase):
    def test_add_counts(self):
        self.assertEqual(Sketch().add(1.0)["count"], 1)

    def test_quantile_single(self):
        sketch = Sketch()
        sketch.add(5.0)
        self.assertEqual(sketch.quantile(0.5), 5.0)

    def test_quantile_empty(self):
        self.assertIsNone(Sketch().quantile(0.5))

    def test_stats_shape(self):
        self.assertIn("alpha", Sketch().stats())

    def test_quantiles_wraps_sketch(self):
        quantiles = Quantiles()
        quantiles.add(1.0)
        self.assertEqual(quantiles.sketch.stats()["count"], 1)


if __name__ == "__main__":
    unittest.main()
