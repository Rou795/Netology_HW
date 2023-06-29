# Располагаю информацию из файлов в словари. В качестве ключа использую имя файла,
# текст предваряется кол-ом строк

with open('1.txt') as f:
    txt_1 = f.readlines()
    txt_1.insert(0, [len(txt_1)])
    dict_1_txt = {'1.txt': txt_1}
with open('2.txt') as f:
    txt_2 = f.readlines()
    txt_2.insert(0, [len(txt_2)])
    dict_2_txt = {'2.txt': txt_2}
with open('3.txt') as f:
    txt_3 = f.readlines()
    txt_3.insert(0, [len(txt_3)])
    dict_3_txt = {'3.txt': txt_3}

text_list = []
text_list.append(dict_1_txt)
text_list.append(dict_2_txt)
text_list.append(dict_3_txt)

# Сортировка по кол-ву строк

text_list_sorted = sorted(text_list, key=lambda text: list(text.values())[0])

# Блок по созданию итогового текста, по строчно добавляем соответствующие строки вытаскивая их из словарей

text = ''
for part in text_list_sorted:
    text += list(part.keys())[0] + '\n'
    text += str(list(part.values())[0][0][0]) + '\n'
    for index in range(1, len(list(part.values())[0])):
        text += list(part.values())[0][index]
    text += '\n'

with open('final.txt', 'w') as f:
    f.write(text)
