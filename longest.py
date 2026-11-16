result = ""
    for char in s:
        if char.lower() not in "aeiou":
            result += char
    return result