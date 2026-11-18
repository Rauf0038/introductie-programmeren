def longest_word_length(s: str) -> int:
    
    current = 0
    count = 0
    for char in s:
        if char == ' ':
            break
        elif 