def vowely_words(words: list[str]) -> list[str]:
    
klinker = 'aeoui'
tweeklinkers = []
for word in words:
    for char in word:
        count = 0
        if char in kli:
            count += 1
        if count >= 2:
            tweeklinkers.append(word)
            
return tweeklinkers

        
    