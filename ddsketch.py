"""ddsketch.py：分位估计（基线：全量样本）。"""
from __future__ import annotations


class Sketch:
    def __init__(self, alpha: float = 0.1):
        self.alpha = alpha
        self.samples = []
        self.buckets = {}
        self.merges = 0

    def add(self, value: float) -> dict:
        """基线：全留样本。"""
        self.samples.append(value)
        return {"count": len(self.samples)}

    def quantile(self, q: float) -> float:
        """基线：排序后精确取值。"""
        ordered = sorted(self.samples)
        if not ordered:
            return None
        return ordered[min(len(ordered) - 1, int(q * len(ordered)))]

    def bucket_map(self) -> dict:
        raise NotImplementedError("桶映射还没实现")

    def merge(self, other) -> "Sketch":
        raise NotImplementedError("合并还没实现")

    def relative_error(self, q: float) -> float:
        raise NotImplementedError("相对误差还没实现")

    def persist(self) -> bytes:
        raise NotImplementedError("快照还没实现")

    def restore(self, blob: bytes = None) -> dict:
        raise NotImplementedError("重启恢复还没实现")

    def stats(self) -> dict:
        return {"alpha": self.alpha, "count": len(self.samples), "buckets": len(self.buckets),
                "merges": self.merges}
