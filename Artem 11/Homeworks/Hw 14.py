def print_map(my_map: dict) -> None:
    print("All map:")
    item = my_map.items()
    for key, value in item:
        print(key, value)


author_stats = {
    "Rowling": {"books": 7, "pages": 4100},
    "Orwell": {"books": 2, "pages": 440},
    "Austen": {"books": 6, "pages": 1600}
}

print(author_stats.get("Tolkien", {"books": 0, "pages": 0}))

print_map(author_stats)

# item = author_stats.items()
# for key, value in item:
#     print(key, value.get("books"))

author_stats.update({"King": {"books": 5, "pages": 3200}})
print_map(author_stats)

Orwell = author_stats.pop("Orwell")

print(f"Orwell: {Orwell}")

total_pages = sum(pages["pages"] for pages in author_stats.values())
print(total_pages)