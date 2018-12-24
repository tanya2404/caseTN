import random


def text_in():
    with open('input.txt', 'r') as f_in:
        txt = f_in.read()
        signs = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя.,!?'
        for i in txt:
            if i not in signs:
                txt = txt.replace(i, ' ')
        txt.replace('...', ' ')
    txt = txt.split()
    return txt


def chain(txt):
    words = dict()
    for item in txt:
        words.update({item: list()})
    for i in range(len(txt) - 1):
        words[txt[i]].append(txt[i + 1])
    for_end = list()
    for_start = list()
    for item in txt:
        if item.count('.') + item.count('!') + item.count('?') > 0:
            for_end.append(item)
    for i in range(len(txt)):
        if txt[i].lower() != txt[i] and txt[i - 1] in for_end:
            for_start.append(txt[i])
    middle = list()
    for i in txt:
        if i not in for_end and i not in for_start:
            middle.append(i)

    return words, for_end, for_start, middle


def sentence(words, for_end, for_start, middle):
    length = random.randint(5, 20)
    sentence = [random.choice(for_start)]
    counter = 1
    while True:
        if counter > 20:
            counter = 1
            sentence = [random.choice(for_start)]
            continue
        lst = list()
        for i in words[sentence[counter - 1]]:
            if i in middle:
                lst.append(i)
            if counter > 4:
                for i in words[sentence[counter - 1]]:
                    if i in for_end:
                        lst.append(i)
        try:
            word = random.choice(lst)
        except IndexError:
            counter = 1
            sentence = [random.choice(for_start)]
            continue
        sentence.append(word)
        counter += 1
        if word in for_end:
            break
    return ' '.join(sentence)


def markov(sen, words, for_end, for_start, middle):
    res = list()
    for i in range(sen):
        res.append(sentence(words, for_end, for_start, middle))
    res = ' '.join(res)
    return res


def text_out(txt):
    with open('output.txt', 'w') as f_out:
        f_out.write(txt)


def main():
    sen = int(input('Количество предложений: '))
    txt = text_in()
    words, for_end, for_start, middle = chain(txt)
    txt = markov(sen, words, for_end, for_start, middle)
    text_out(txt)


if __name__ == '__main__':
    main()