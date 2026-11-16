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
    klinker == 'aeoui'
    for woord in strs:
        if klinker not in woord
            resultaat.append(woord)
    return resultaat