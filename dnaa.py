#!/usr/bin/python3


reads = ["ATGCC", "GCCAA", "CAAAT", "TTTGG"]
k = 3


n = len(reads)
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        suffix_i = reads[i][-k:]
        prefix_j = reads[j][:k]

        if suffix_i == prefix_j:
            print(f"{i + 1} - {j +1}")

