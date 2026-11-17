def split_by_sign(ints: list[int]) -> list[list[int]]:

"""
>>>([-3, 0, 5, -1, 2])
[[-3, -1], [0, 5, 2]]

>>>([-1, 0 1])
[[-3], [0, 1]]

>>>([])
[[], []]

>>>([4, 5, -8])
[[-8], [4,5]]
"""

negatief = []
niet_negatief = []

for getal in ints:
    if getal < 0:
        negatief.append(getal)
    elif getal >= 0:
        niet_negatief.append(getal)
return[[negatief], []