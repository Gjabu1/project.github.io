rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
       'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
rus_code = ['р', 'х', 'ё', 'з', 'к', 'н', 'ь', 'я', 'б', 'п', 'л', 'щ', 'ч', 'ф', 'у', 'т', 'ш', 'ю', 'д', 'и', 'ж', 'в', 'с', 'м', 'о', 'й', 'ъ', 'ы', 'ц', 'г', 'э', 'а', 'е']
rus_in = dict(zip(rus, rus_code))
rus_out = dict(zip(rus_code, rus))
def encryptor(text, code):
    text = text.lower()

    def in_encryptor(text):
        answer = []
        global rus
        global rus_in

        for i in text:
            if i in rus:
                answer.append(rus_in[i])
            else:
                answer.append(i)

        file = open('текст.txt', 'w', encoding='utf-8')
        file.write(''.join(answer))

    def out_encryptor(text):
        answer = []
        global rus
        global rus_out

        for i in text:
            if i in rus:
                answer.append(rus_out[i])
            else:
                answer.append(i)

        file = open('текст.txt', 'w', encoding='utf-8')
        file.write(''.join(answer))

    if code == 0:
        in_encryptor(text)
    elif code == 1:
        out_encryptor(text)

file = open('текст.txt', encoding='utf-8')
text = file.read()