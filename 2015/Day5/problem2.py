import re
nice = 0
prop1 = re.compile(r'.*(..).*\1.*')
prop2 = re.compile(r'.*(.).\1.*')
with open('input.txt') as input:
    for word in input:
        if prop1.match(word) and prop2.match(word):
            nice += 1
    print(nice)