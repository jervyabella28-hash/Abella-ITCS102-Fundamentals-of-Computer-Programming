# ===== LEVEL 3: Each anime is a dictionary of characters =====

Black_clover = {"Asta": ["Has no Magic power", "Has a 5 Leaf Clover grimoire"]}

HxH = { "Gon Freecss": ["Powerful Nen", "Adult Gon"]}

Dandadan = {"Okarun": ["Turbo Granny's Powers", "Transformed Form"]}

# ===== LEVEL 2: Each genre is a dictionary of anime =====

Fantasy = { "Black Clover": Black_clover, "Hunter X Hunter": HxH}
   
Supernatural = {"Dandadan": Dandadan}

# ===== LEVEL 1: The main dictionary =====

Anime = { "Fantasy": Fantasy,"Supernatural": Supernatural}

# ===== 1. Going down one level at a time =====

print("=== 1. Going down one level at a time ===")
print(Anime["Fantasy"]["Black Clover"]["Asta"][1])

# ===== 2. Loop level 1: Categories =====

print()
print("=== 2. Loop level 1: categories ===")

for category in Anime:
    print(category)

# ===== 3. Loop levels 1-2: Categories and titles =====

print()
print("=== 3. Loop levels 1-2: categories and titles ===")

for category, titles in Anime.items():
    print(category)

    for title in titles:
        print(" ", title)

# ===== 4. Loop levels 1-3: Categories, titles and characters =====

print()
print("=== 4. Loop levels 1-3: categories, titles and characters ===")

for category, titles in Anime.items():
    print(category)

    for title, characters in titles.items():
        print(" ", title)

        for character in characters:
            print("   ", character)


# ===== 5. Display everything including character details =====

print()
print("=== 5. Complete Anime Information ===")

for category, titles in Anime.items():
    print("\nCategory:", category)

    for title, characters in titles.items():
        print(" Anime:", title)

        for character, details in characters.items():
            print("  Character:", character)

            for detail in details:
                print("   -", detail)