result = []
for word in s:
    count = 0
    for char in word:
        count +=1
        if count >= 10 :
            result.append(word)

if __name__ = '__main__':
    tekst = input('schrijf een zin op:')
    
    