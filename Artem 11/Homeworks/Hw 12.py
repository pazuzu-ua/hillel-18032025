import sys
from random import randint

try:
    min_limit = int(input('Тут якийсь текст '))
    max_limit = int(input('Тут якийсь текст '))
    print(randint(min_limit, max_limit))
except ValueError:
    print("write NUMBER not ANYTHING ELSE!")
    sys.exit()
finally:
    print("END!")
