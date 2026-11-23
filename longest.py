def count_coins(cents: int) -> int:
    """
    Berekent het minimale aantal munten (25, 10, 5 en 1 cent)
    waarmee het bedrag `cents` kan worden teruggegeven.

    >>> count_coins(0)
    0
    >>> count_coins(24)
    6
    >>> count_coins(41)
    4
    >>> count_coins(75)
    3
    """
    coins = 0
    while value in (25, 10, 5, 1):
        while cents >= value:
            cents -= value
            coins += 1
    return coins


if __name__ == '__main__':
    cents = -1
    while cents < 0:
        cents = int(input('Hoeveel wisselgeld moet er gegeven worden (in centen)? '))
    print(count_coins(cents))