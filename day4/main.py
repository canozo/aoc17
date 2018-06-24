def check_valids(text):
    valids = 0
    for line in text:
        flag = True
        words = []
        for word in line.split(' '):
            if word in words:
                flag = False
                break
            else:
                words.append(word)
        if flag:
            valids += 1
    return valids

def anagrams(text):
    valids = 0
    for line in text:
        flag = True
        words = []
        for word in line.split(' '):
            if sorted(word) in words:
                flag = False
                break
            else:
                words.append(sorted(word))
        if flag:
            valids += 1
    return valids


with open('input.txt', 'r') as texto:
    _input = texto.read().split('\n')
    
print(check_valids(_input))
print(anagrams(_input))
