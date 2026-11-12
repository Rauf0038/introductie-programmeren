def is_acidic(ph: bool) -> bool:
    """
    geeft aan of een bepaalde ph zuur of basisch is
    >>>ph(3)
    zuur
    >>>ph(10)
    basisch
    >>>ph(7.1)
    basisch
    >>>ph(-1)
    zuur
    """

if __name__ == '__main__':
    ph = float(input('Wat is de ph van uw oplossing?'))
    if ph > 7:
        print('Uw oplossing is basisch')
    else:
        print('uw oplossing is zuur')

python -m doctest -v programma.py

