"""quantapi.py：对外门面（老接口 add/quantile 不能改）。"""
from __future__ import annotations

from ddsketch import Sketch


class Quantiles:
    def __init__(self, alpha: float = 0.1):
        self.sketch = Sketch(alpha)

    def add(self, value: float) -> dict:
        return self.sketch.add(value)

    def quantile(self, q: float) -> float:
        return self.sketch.quantile(q)

    def bucket_map(self) -> dict:
        return self.sketch.bucket_map()

    def merge(self, other) -> "Quantiles":
        return self.sketch.merge(other.sketch if hasattr(other, "sketch") else other)

    def snapshot(self) -> bytes:
        return self.sketch.persist()

    def rebuild(self, blob: bytes = None) -> dict:
        return self.sketch.restore(blob)
