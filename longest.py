def count_coins(cents: int) -> int:
    """
    Berekent het minimale aantal munten (25, 10, 5 en 1 cent)
    waarmee het bedrag `cents` kan worden teruggegeven.

    >>> count_coins(0)
    0
    >>> count_coins(1)
    1
    >>> count_coins(24)
    6
    >>> count_coins(25)
    1
    >>> count_coins(41)
    4
    >>> count_coins(402)
    20
    """
    coins = 0
    for value in (25, 10, 5, 1):
        while cents >= value:
            cents -= value
            coins += 1
    return coins


if __name__ == '__main__':
    amount = -1
    while amount < 0:
        text = input('Hoeveel wisselgeld moet er gegeven worden? ')
        try:
            amount = float(text)
        except ValueError:
            amount = -1

    cents = round(amount * 100)
    print(count_coins(cents))
    