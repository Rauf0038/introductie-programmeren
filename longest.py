def longest_word_length(s: str) -> int:
    
    current = 0
    count = 0
    for char in s:
        if char != ' ':
            count +=1
        if count > current:
            current = count
        