def count_long_words(s: str, n: int) -> int:
    """
    doctests hier
    """
    current = 0        # lengte van het huidige woord
    count = 0            # aantal lange woorden
    for char in s:
        if char == " ":
            if current > n:
                count +=1
            current = 0
        else:
            ...
    # na de loop: het laatste woord
    if current > ...:
        ...
    return ...