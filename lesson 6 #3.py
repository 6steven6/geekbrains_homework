from itertools import zip_longest
import json

result = {}
with open('users.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        lines_in_users = sum(1 for line in users)
        lines_in_hobby = sum(1 for line in hobby)

        if lines_in_users < lines_in_hobby:
            exit(1)
        users.seek(0)
        hobby.seek(0)

        for line_user, line_user_hobby in zip_longest(users, hobby):
            result[line_user.strip()] = line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby

with open('user_and_hobby', 'w+', encoding='utf-8') as user_hobby:
    json.dump(result, user_hobby, ensure_ascii=False)
