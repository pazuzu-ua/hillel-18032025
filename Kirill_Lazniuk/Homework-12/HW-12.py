import random
import sys

try:
    min_limit = int(input("Введіть мінімальну межу: "))
    max_limit = int(input("Введіть максимальну межу: "))
    
    if min_limit >= max_limit:
        print("Помилка: Мінімальна межа повинна бути меншою за максимальну.")
        sys.exit()

    random_number = random.randint(min_limit, max_limit)
    print(f"Випадкове число між {min_limit} та {max_limit}: {random_number}")

except ValueError:
    print("Помилка: Потрібно вводити лише цілі числа!")
    sys.exit()
