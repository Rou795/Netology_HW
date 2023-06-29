cook_book = {}
receipts = []
receipt = ''
# Создание списка рецептов с разделением по блюдам
with open('Cook_Book.txt') as f:
    for line in f.readlines():
        if line.isspace():
            receipts.append(receipt)
            receipt = ''
        else:
            receipt += line
    receipts.append(receipt)
# Создание требуемого словаря

for receipt in receipts:
    receipt_list = receipt.split('\n')
    cook_book[receipt_list[0]] = []
    for index in range(2, len(receipt_list)):
        if receipt_list[index]:
            ingredient_list = receipt_list[index].split('|')
            ingredient_dict = {}
            ingredient_dict['ingredient_name'] = ingredient_list[0].strip()
            ingredient_dict['quantity'] = ingredient_list[1].strip()
            ingredient_dict['measure'] = ingredient_list[2].strip()
            cook_book[receipt_list[0]].append(ingredient_dict)
# Реализация требуемой функции через адресацию по dish в словаре cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    for dish in dishes:
        for el in cook_book[dish]:
            if not(el['ingredient_name'] in shop_dict.keys()):
                shop_dict[el['ingredient_name']] = dict(measure=el['measure'], \
                                                        quantity=int(el['quantity']) * person_count)
            else:
                shop_dict[el['ingredient_name']]['quantity'] += int(el['quantity']) * person_count
    return shop_dict


print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
