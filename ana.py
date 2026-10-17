#!/usr/bin/python3

valid_bases = {'A', 'T', 'G', 'C'}
count = 0

a = 1
dna = input()
while dna != 'STOP':
    if len(dna) == 4:
        for i in dna:
            if i not in valid_bases:
                print("error")
                a = 0
        if a == 1:
            count += 1
    dna = input()
    a = 1
print(count)
