def split_by_vowel(letters: list[str]) -> list[list[str]]:

klinkers = 'aeoui'
lijst_klinkers = []
lijst_medeklinkers = []

for char in letters:
    if char.lower() in klinkers:
        lijst_klinkers.append(char)
    else:
        lijst_medeklinkers.append(char)
        
return[lijst_klinkers, lijst_medeklinkers]