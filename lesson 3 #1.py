def num_translate(english_word):
    return translated_words.get(english_word)


translated_words = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

english_word = input("введите цифру:")
print(num_translate(english_word))
