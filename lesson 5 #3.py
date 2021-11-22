from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def result(tutors, classes):
    res = zip_longest(tutors, classes)
    yield res


print(tuple(next(result(tutors, classes))))


