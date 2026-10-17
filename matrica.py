#!/usr/bin/python3

def hamming_distance(seq1, seq2):
    if len(seq1 != len(seq2):
           raise ValueError("Последовательности должны быть одинаковой длины")
           return sum(c1 != c2 for c1, c2 in zip(seq1, seq2))

sequences = ["AACG", "AATG", "TATG", "TTTG"]
           n = len(sequences)
           distance_matrix = [ * n for _ in range(n)]

           for i in range(n):
            for j in range(n):
              distance_matrix[i][j] = hamming_distance(sequences[i], sequences[j])
           for row in distance_matrix:
            print(" ".join(str(x) for x in row))


