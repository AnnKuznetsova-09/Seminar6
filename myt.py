#!/usr/bin/python3

reference = input()
sample = input()
for i, (ref_nuc, samp_nuc) in enumerate(zip(reference, sample), start = 1):
    if ref_nuc != samp_nuc:
        print(f"{i}: {ref_nuc} > {samp_nuc}")
