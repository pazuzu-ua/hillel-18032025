author_stats = {
    "Rowling": {"books": 7, "pages": 4100},
    "Orwell": {"books": 2, "pages": 440},
    "Austen": {"books": 6, "pages": 1600}
}

# Беремо інформацію про Tolkien
tolkien_stats = author_stats.get("Tolkien", {"books": 0, "pages": 0})

# Виводимо статистику для всіх письменників
for author, stats in author_stats.items():
    print(f"{author} — {stats['books']} книжок")

# Додаємо King і інформацію про нього
author_stats.update({"King": {"books": 5, "pages": 3200}})

# Видаляємо Orwell і додаємо інформацію про нього в змінну
orwell_stats = author_stats.pop("Orwell")

# Рахуємо суму всіх сторінок
import copy
author_stats_copy = copy.deepcopy(author_stats)
total_pages = sum(stats["pages"] for stats in author_stats_copy.values())

print("\nДані Tolkien:", tolkien_stats)
print("Дані Orwell:", orwell_stats)
print("Загальна кількість сторінок:", total_pages)
