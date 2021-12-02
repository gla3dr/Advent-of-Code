import re
nice = 0
naughty = ('ab', 'cd', 'pq', 'xy')
vowels = ('a', 'e', 'i', 'o', 'u')
dubs = re.compile(r'.*(.)\1.*')
with open('input.txt') as input:
    for word in input:
        if not any(x in word for x in naughty):
            if sum(letter in vowels for letter in word) >= 3:
                if dubs.match(word):
                    nice += 1
    print(nice)
