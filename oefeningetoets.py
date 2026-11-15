def vowely_words(words: list[str]) -> list[str]:
    """
    >>> vowely_words(['Aap', 'Noot', 'Mies'])
    ['Aap', 'Noot', 'Mies']
    >>> vowely_words(['bak', 'kat', 'mies'])
    ['mies']
    >>> vowely_words(['AI', 'b'])
    ['AI']
    >>> vowely_words([])
    []
    """
    result = []
    for word in words:
        count = 0
        for char in word:
            if char.lower() in "aeiou":
                count += 1
        if count >= 2:
            result.append(word)
    return result


if __name__ == "__main__":
    tekst = input("Typ woorden, gescheiden door spaties: ")
    woorden = tekst.split()   # alleen hier, niet in de functie
    print(woorden)
    
    















def no_vowely_words(words: list[str]) -> list[str]
"""
>>>no_vowely_words(['aap', 'noot', 'psst'])