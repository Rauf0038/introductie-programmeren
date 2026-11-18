def sum_even(ints: list[int]) -> int:
    """
    >>>[1,2,3,4]
    [6]
    >>>[]
    []
    >>>[1,2,3,4,5]
    [6]
    >>>[2,4,6,8]
    [20]
    """
    even = []
    oneven = []
    for number in ints:
        if number % 2 == 0:
            number.append(even)
    return sum_even
    
    
count_words_with(s: str, letter: str) -> int:
    """
    >>>('appel peer banaan', 'a')
    2
    """
    
    count = 0
    for char in s:
        if char == letter:
            count += 1
    return count
    