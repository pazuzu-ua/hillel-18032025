
author_stats = {
    "Rowling": {"books": 7, "pages": 4100},
    "Orwell": {"books": 2, "pages": 440},
    "Austen": {"books": 6, "pages": 1600}
}


tolkien_data = author_stats.get("Tolkien", {"books": 0, "pages": 0})
print("Tolkien:", tolkien_data)


for author, stats in author_stats.items():
    print(f"{author} — {stats['books']} книг")


author_stats.update({"King": {"books": 5, "pages": 3200}})
print("\nПісля додавання King:")
print(author_stats)


orwell_data = author_stats.pop("Orwell")
print("\nOrwell видалено. Його дані:")
print(orwell_data)


author_stats_copy = author_stats.copy()
total_pages = sum(author["pages"] for author in author_stats_copy.values())
print("\nЗагальна кількість сторінок:", total_pages)
