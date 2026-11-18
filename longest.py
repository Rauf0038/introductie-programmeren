def has_single_vowel(s: str) -> bool:
    """
    >>> has_single_vowel("bims")
    True
    >>> has_single_vowel("yolo")
    False
    >>> has_single_vowel("")
    False
    """
    klinkers = 'aeouiAEOUI'
    count = [0]