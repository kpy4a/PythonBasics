def num_translate(ver):
    vers = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыри',
        'five': 'пять',
        'six': 'шесть'
    }
    if a in vers:
        return vers[ver]
    else:
        return


a = input()
print(num_translate(a))


def thesaurus(*args):
    a = {}
    for i in args:
        if i[0] in a:
            a[i[0]].append(i)
        else:
            a[i[0]] = [i]
    return a


print(thesaurus("Ира", "Макс", "Петр", "Илья", "Петров", "Ильич"))

from random import randrange


def get_jokes(a, no_repeat=False):
    """
    a method that allows you to randomly compose a joke from 3 lists
    1)a - number of jokes
    2)no_repeat - the default is False
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if a > 5 and no_repeat:
        print("Слишком большое количество")
    else:
        all_jokes = []
        while a != 0:
            jokes = ''
            nouns1 = randrange(len(nouns))
            jokes += nouns[nouns1] + ' '
            if no_repeat:
                del nouns1
            adverbs1 = randrange(len(adverbs))
            jokes += adverbs[adverbs1] + " "
            if no_repeat:
                del adverbs1
            adjectives1 = randrange(len(adjectives))
            jokes += adjectives[adjectives1] + " "
            if no_repeat:
                del adjectives1
            a -= 1
            all_jokes.append(jokes)
        print(all_jokes)


get_jokes(2)