def split_by_parity(ints: list[int]) -> list[list[int]]:
    

even = []
oneven = []

for int in ints:
    if int % 2 == 0:
        even.append(int)
    else:
        
        