#!/ust/bin/python3


rna = input()
stop_codons = {"UAA", "UAG", "UGA"}
count = 0


for i in range(0, len(rna), 3):
    codon = rna[i:i + 3]
    if codon in stop_codons:
        print(f"количество кодирующих кодонов: {count}")
        print(f"стоп-кодон: {codon}")
        break
    count += 1
