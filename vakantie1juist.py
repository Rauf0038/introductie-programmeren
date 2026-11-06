def bereken_kosten(afstand: int, duur: int) -> int:
    """
    Berekent de totale kosten van een reis: 0,13 euro per km
    vervoerskosten plus 60 euro per nacht verblijfskosten,
    afgerond op hele euro's.

    >>> bereken_kosten(100, 2)
    133
    >>> bereken_kosten(0, 0)
    0
    >>> bereken_kosten(0, 1)
    60
    >>> bereken_kosten(100, 0)
    13
    """
    
    if __name__ == '__main__':
    
    vervoerskosten = 0.13 * afstand
    verblijfskosten = 60 * duur
    totaal = round(verblijfskosten + vervoerskosten)
    return totaal