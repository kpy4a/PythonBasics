"""Task 2"""
# при любых значениях выводит любую длину без ошибок
genator = (num for num in range(1, int(input("")) + 1, 2))
print(*genator)

"""Task 3"""
Names = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
Grade = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

Name_grade = zip((n for n in Names), (k for k in Grade))

print(*Name_grade)

"""Task 4"""
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

a = [
    src[i]
    for i in range(1, len(src))
    if src[i] > src[i - 1]
]

print(a)

"""Task 5"""
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
a = [i for i in src if src.count(i) == 1]
print(a)