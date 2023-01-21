
a = input('letters: ')
letters = [x for x in a]
must_letter = input('must letter: ')
possibility = []

with open('dictionary/popular.txt') as word_file:
    words = set(word_file.read().split())

print(letters)

for word in words:
    flag = False
    for c in word:
        if c == must_letter:
            flag = True
    if flag == False:
        continue
    flag = True
    for c in word:
        flag2 = False
        for g in letters:
            if c == g:
                flag2 = True
        if flag2 != True:
            flag = False
    if flag == False:
        continue
    if (len(word) > 3):
        possibility.append(word)
print(len(possibility))
for i in possibility:
    print(i)
