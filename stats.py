def get_num_words(text):
    words = text.split()
    return len(words)

def get_each_character_count(text):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


def print_character_count(characters):
    sorted_characters = sorted(characters.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_characters:
        print(f"{char}: {count}")