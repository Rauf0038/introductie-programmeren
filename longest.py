def split_by_parity(ints: list[int]) -> list[list[int]]:
    
    
    even = []
    oneven = []
    
    for getal in ints:
        if int % 2 == 0:
            even.append(int)
        else:
            oneven.append(int)
            
    return [even, oneven]
            