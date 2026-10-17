#!/usr/bin/python3



growth = [
        [0, 2, 4, 8],
        [0, 1, 1, 2],
        [0, 3, 6, 9]
]

threshold = 5
for culture  in growth:
    for i, value in enumerate(culture):
        if value >= threshold:
            result = i
        else:
            result = "отсутствует"
            break 
        print(result)
