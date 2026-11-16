def longest_vowel_start(s: str) -> int

count == 0
current == 0

for word in s:
    if word[0] is in 'aeoui':
        for char in word:
            count += 1
            if count > current:
                current == count
                

return current
            
        