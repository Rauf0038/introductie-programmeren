def select_not_lower(strs: list[str]) -> list[str]:
    """Geeft een nieuwe lijst met alleen de strings uit strs die minimaal
    één teken bevatten dat niet lowercase is.

    >>> select_not_lower(['Roep', 'maar', 'HALLO '])
    ['Roep', 'HALLO ']
    >>> select_not_lower(['maar', 'kat'])
    []
    >>> select_not_lower(['kAt', 'KAT', 'kat'])
    ['kAt', 'KAT']
    >>> select_not_lower([])
    []
    """
       resultaat = []
    for woord in words:
        aantal = 0
        for letter in woord:
            if letter.lower() in 'aeoui':
                aantal += 1
        if aantal == 0:
            resultaat.append(woord)
    return resultaat