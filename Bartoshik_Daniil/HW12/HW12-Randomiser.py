import random
import sys

try:
    minv = int(input('Enter the minimum number: '))
    maxv = int(input('Enter the maximum number: '))
except ValueError:
    print('Error | You must enter only integer numeric values.')
    sys.exit()

if minv >= maxv:
    print('Error | The minimum limit must be less than the maximum limit.')
    sys.exit()

random_number = random.randint(minv, maxv)
print(f'Random number between {minv} and {maxv}: {random_number}')
