import hashlib

input = 'ckczppom'
index = 1
while True:
    m = hashlib.md5()
    m.update("{}{}".format(input, index))
    hash = m.hexdigest()
    if hash.startswith('000000'):
        break
    index += 1
print index