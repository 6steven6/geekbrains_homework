import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num):
    """Функция состовляющая разное колличество шуток из рандомных слов заддных в списке """
    joke_list = []
    for joke in range(num):
        randm_nouns = random.choice(nouns)
        randm_adverbs = random.choice(adverbs)
        randm_adjectives = random.choice(adjectives)
        joke_list.append(f'{randm_nouns} {randm_adverbs} {randm_adjectives}')
    return joke_list

print(get_jokes(1))
print(get_jokes(2))


