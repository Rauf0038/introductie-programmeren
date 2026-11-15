def vowely_words(words: list[str]) -> list[str]:
    """Returns all words that contain two or more vowels (upper or lower case).

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