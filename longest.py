split_by_limit(ints: list[int], limit: int) -> list[list[int]]:
    
    
    
Kleiner = []
Groter = []

for number in ints:
    if number < limit:
        Kleiner.append(number)
    else:
        