def meal(time: str) -> str | None:
    """
    Converteert een tijd-string naar een maaltijd.
    De maaltijd kan zijn "ontbijt", "lunch", "avondeten".

    >>> meal("7:15")
    'ontbijt'
    >>> meal("13:00")
    'lunch'
    >>> meal("18:53")
    'avondeten'
    >>> meal("22:12") is None
    True
    """
    uren, minuten = time.split(":")
    totaal = int(uren) * 60 + int(minuten)

    if 7 * 60 <= totaal <= 8 * 60:
        return "ontbijt"
    if 12 * 60 <= totaal <= 13 * 60:
        return "lunch"
    if 18 * 60 <= totaal <= 19 * 60:
        return "avondeten"
    return None


if __name__ == '__main__':
    tijd = input("Hoe laat is het? ")
    maaltijd = meal(tijd)
    if maaltijd is not None:
        print(f"Het is tijd voor {maaltijd}")