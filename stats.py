def count_words_in_text(text):
    total = 0

    for _ in text.split():
        total += 1

    return total


def count_characters_in_text(text):
    character_map = {}

    for word in text.split():
        for char in word.lower():
            if char.isalpha():
                character_map[char] = character_map.get(char, 0) + 1

    return character_map


def sort_on(item):
    return item["num"]


def display_sorted_characters(dict):
    character_list = []

    for key, value in dict.items():
        character_list.append({"char": key, "num": value})

    character_list.sort(key=sort_on, reverse=True)

    for char_dict in character_list:
        print(f"{char_dict["char"]}: {char_dict["num"]}")
