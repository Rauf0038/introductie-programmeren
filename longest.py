def remove_vowels(s: str) -> str:
    """
    >>> remove_vowels("hallo")
    'hll'
    >>> remove_vowels("")
    ''
    >>> remove_vowels("aeiou")
    ''
    >>> remove_vowels("just setting up my twitter")
    'jst sttng p my twttr'
    """
    result = ""
    for char in s:
        if char.lower() not in "aeiou":
            result += char
    return result


if __name__ == "__main__":
    tekst = input("Typ een zin: ")
    print(remove_vowels(tekst))