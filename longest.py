def count_exact_words(s: str, n: int) -> int:
    """
    # Hint: schrijf hier vier doctests. Bepaal de uitkomst met de hand.
    # 1. Het voorbeeld uit de opgave (antwoord 3)
    # 2. Een lege string (hoeveel woorden van lengte n zijn er?)
    # 3. Dezelfde string als het voorbeeld, maar met n = 3
    #    (loop de lengtes na: 3, 4, 4, 4, 3)
    # 4. Eén woord zonder spatie, bijvoorbeeld "aap" met n = 3
    """
    current = 0   # Hint: lengte van het huidige woord. Wat is de beginwaarde?
    count = 0     # Hint: aantal woorden dat precies n lang is. Beginwaarde?
    for char in s:                 # Hint: één teken per stap
        if char == " ":            # Hint: een spatie betekent dat het woord klaar is
            if current == n:      # Hint: je wilt PRECIES n. Welke vergelijking is dat? (niet > of <)
                count += 1          # Hint: het woord telt mee, dus de teller gaat omhoog
            current = 0          # Hint: het volgende woord begint, dus opnieuw tellen
        else:
            current ...            # Hint: een gewone letter, dus het woord wordt 1 langer
    # Hint: het laatste woord heeft geen spatie erachter.
    # Doe hier dezelfde check als in de loop:
    if current ... n:
        count ...
    return ...                     # Hint: wat moet de functie teruggeven?