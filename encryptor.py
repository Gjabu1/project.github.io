import pyperclip

rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
       'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ']
code = ['д', 'ы', 'е', 'я', 'с', 'ч', 'ъ', 'г', 'а', 'о', 'т', 'в', 'р', 'и', 'ю', 'х', 'щ', '#', 'з', 'ь', 'к', 'н',
        'э', 'й', 'л', 'ж', 'у', 'ш', 'ф', 'ё', 'ц', 'п', 'б', 'м']
encrypt = dict(zip(rus, code))
decrypt = dict(zip(code, rus))


def del_bad(x):
    x = x.lower()
    bad = ",.!?-+()<>–«»"
    bad = list(bad)
    text = []
    for i in x:
        if i not in bad:
            text.append(i)
    text = ''.join(text)
    x = ' '.join(text.split())
    return x


def def_encrypt(x):
    x = del_bad(x)
    global encrypt
    text = []
    for i in x:
        text.append(encrypt[i])
    pyperclip.copy(''.join(text))


def def_decrypt(x):
    global decrypt
    text = []
    for i in x:
        text.append(decrypt[i])
    pyperclip.copy(''.join(text))

# def_encrypt(input())
# def_decrypt(input())
