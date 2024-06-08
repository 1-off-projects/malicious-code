# sillycode
import random
import string
import os
while True:
    path = os.path.dirname(os.path.abspath(__file__))
    endpath = os.path.join(path, '/text/')
    if not os.path.exists(endpath):
        os.mkdir(endpath)
        pass
    else:
        while True:
            filename = (endpath) + (random.choice(string.ascii_letters)) + (random.choice(string.ascii_letters)) + (random.choice(string.ascii_letters)) + (random.choice(string.ascii_letters)) + (random.choice(string.ascii_letters)) + (random.choice(string.ascii_letters)) + (random.choice(string.ascii_letters)) + (random.choice(string.ascii_letters)) + (random.choice(string.ascii_letters)) + (random.choice(string.ascii_letters)) + (".txt")
            with open(filename, 'w'):
                code='end'
            pass
        break
    break
print("check your files :)")