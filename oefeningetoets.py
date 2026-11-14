def woorden_met_a(woorden):
    """Geeft alleen de woorden terug die de letter 'a' bevatten.

    >>> woorden_met_a(["appel", "peer", "banaan", "kiwi", "druif"])
    ['appel', 'banaan']
    >>> woorden_met_a(["Appel", "Aap", "peer"])
    ['Appel', 'Aap']
    >>> woorden_met_a(["peer", "kiwi"])
    []
    >>> woorden_met_a([])
    []
    """
    return [woord for woord in woorden if "a" in woord.lower()]
    

if __name__ == "__main__":
    woord = input('geef een lijst aan worden')
