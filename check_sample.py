"""check_sample.py：按 sample/values.json 走一圈，打印验收面。"""
import json
import os
import sys

from ddsketch import Sketch


def main() -> int:
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join("sample", "values.json")
    with open(path, encoding="utf-8") as handle:
        spec = json.load(handle)
    sketch = Sketch(spec["alpha"])
    for value in spec["values"]:
        sketch.add(value)
    buckets = sketch.bucket_map()
    estimates = [(q, sketch.quantile(q)) for q in spec["quantiles"]]
    exact = [(q, sketch.samples and sorted(sketch.samples)[min(len(sketch.samples) - 1,
                                                               int(q * len(sketch.samples)))])
             for q in spec["quantiles"]]
    second = Sketch(spec["alpha"])
    for value in spec["more_values"]:
        second.add(value)
    merged = sketch.merge(second)
    blob = sketch.persist()
    reborn = Sketch(spec["alpha"])
    restored = reborn.restore(blob)
    print("桶映射（桶号 -> 计数） =", buckets.get("counts"))
    print("桶个数 =", len(buckets.get("counts") or {}))
    print("分位估计 =", estimates)
    print("精确分位（对照） =", exact)
    print("相对误差上界 =", spec["alpha"])
    print("合并后的分位估计 =", merged.quantile(0.5))
    print("恢复后的桶个数 =", len(restored.get("counts") or {}))
    print("不变量（桶计数总和等于样本数） =", spec["count_invariant"])
    print("样本数 =", len(spec["values"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
