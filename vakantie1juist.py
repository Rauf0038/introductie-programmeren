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
    vervoerskosten = 0.13 * afstand
    verblijfskosten = 60 * duur
    totaal = round(verblijfskosten + vervoerskosten)
    return totaal

if __name__ == '__main__':
    
    afstand = int(input('Wat is de afstand van de volledige reis? (in km)'))
    duur = int(input('Hoeveel nachten gaat u verblijven?'))
    
    totaal = bereken_kosten(afstand, duur)
    print('Uw totale kosten voor deze vakantie zijn', totaal, 'euro')
