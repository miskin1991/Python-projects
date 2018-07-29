word = input()

sum_vocals = 0
for letter in word:
    if letter is 'a':
        sum_vocals += 1
    elif letter is 'e':
        sum_vocals += 2
    elif letter is 'i':
        sum_vocals += 3
    elif letter is 'o':
        sum_vocals += 4
    elif letter is 'u':
        sum_vocals += 5

print(sum_vocals)
