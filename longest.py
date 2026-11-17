def split_by_spaces(zin: str) -> list[str]:
    
    
alfabet = 'qwertyuiopasdfghjklzxcvbnm'
woorden = ['']

for char in zin:
    if char in alfabet:
        woorden.append(char)
    if char == ' ':
        break
        
    