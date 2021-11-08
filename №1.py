duration = int(input('Введите время: '))

days_if_more_one_day = duration // 86400
hours_if_more_one_day = duration % 86400 // 3600
mins_if_more_one_day = duration % 86400 % 3600 // 60
secs_if_more_one_day = duration % 86400 % 3600 % 60


hours_if_less_one_day = duration // 3600
mins_if_less_one_day = duration % 3600 // 60
secs_if_less_one_day = duration % 3600 % 60 // 1


if duration < 60:
    print(str(duration // 1), ' secs ')

if 60 <= duration < 3600:
    print(mins_if_less_one_day, ' mins ', secs_if_less_one_day, ' secs ')

if 3600 <= duration < 86400:
    print(hours_if_less_one_day, ' hours ', mins_if_less_one_day, ' mins ', secs_if_less_one_day, ' secs ')

if duration >= 86400:
    print(days_if_more_one_day, ' days ', hours_if_more_one_day, ' hours ', mins_if_more_one_day, ' mins ',
          secs_if_more_one_day, ' secs ')


