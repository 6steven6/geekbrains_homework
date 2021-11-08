for percentages in range(1, 101):
    if percentages % 10 == 2 or percentages % 10 == 3 or percentages % 10 == 4:
        print(percentages, 'процента')
    elif percentages % 10 == 1 and percentages != 11:
        print(percentages, 'процент')
    else:
        print(percentages, 'процентов')
    

