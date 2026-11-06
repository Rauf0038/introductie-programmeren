def hoeveelheid_water(minuten: int) -> int:
    """
    Geeft de hoeveelheid water uit de douche, gerekend in flesjes,
    gegeven het aantal minuten douchen.
    Hoeveel minuten douche je? 1
    12 flesjes water

    Hoeveel minuten douche je? 8
    96 flesjes water
    
    Hoeveel minuten douche je? 1
    12 flesjes water

    Hoeveel minuten douche je? 5
    60 flesjes water
    """

if __name__ == '__main__':
    minuten = int(input('hoeveel minuten doucht u?'))
    flesjes = minuten * 12
    print('u heeft', flesjes, 'water verbruikt')
 python -m doctest -v programma.py
