s = input('Geef een string waarvan je de letters a, b en c encrypted wilt hebben: ')
resultaat = ''
for letter in s:
    if letter == 'a':
        resultaat += 'z'
    elif letter == 'b':
        resultaat += 'y'
    elif letter == 'c':
        resultaat += 'x'
    else:
        resultaat += letter
print(resultaat)