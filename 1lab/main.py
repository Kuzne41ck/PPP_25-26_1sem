#задание 2
import random
students = int(input('Введите количество учеников '))
subjects = int(input('Введите количество предметов '))
a = [[x for x in range(subjects)] for y in range(students)]
for i in range(students):
    for j in range(subjects):
        a[i][j]=random.randint(1, 5)
best = -100
worst = 100
for i in range(len(a)):
    average_mark=sum(a[i])/len(a[i])
    max_mark, min_mark=max(a[i]), min(a[i])
    if average_mark>best:
        best = average_mark
        besti = i
    if average_mark<worst:
        worst = average_mark
        worsti = i
    print(i+1, a[i], average_mark, max_mark, min_mark)
print('Студент с лучшим средним баллом под номером ', besti+1)
print('Студент с худшим средним баллом под номером ', worsti+1)
