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
        