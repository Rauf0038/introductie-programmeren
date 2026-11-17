def vowely_words(words: list[str]) -> list[str]:
    
klinker = 'aeoui'
tweeklinkers = []
for word in words:
    count = 0
    for char in word:
        if char in klinker:
            count += 1
        if count >= 2:
            tweeklinkers.append(word)
            
return tweeklinkers

        
    