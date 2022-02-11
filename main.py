import os

cook_book = {}


def _get_all_files():
    full_path = _get_path()
    all_files = tuple(os.listdir(full_path))
    return all_files


def _get_path():
    dir_path = os.getcwd()
    folder = 'tmp'
    full_path = os.path.join(dir_path, folder)
    return full_path


def _iteration_count(file):
    with open(file) as recepies:
        lines = list(recepies.readlines())
        iter_count = 1
        for i in lines:
            if i == '\n':
                iter_count += 1
    return iter_count


def working_with_file(file):
    with open(os.path.join(_get_path(), file), 'rt', encoding='UTF-8') as recepies:
        for i in range(_iteration_count(os.path.join(_get_path(), file))):
            dish = recepies.readline().strip()
            ingredient_num = int(recepies.readline().strip())
            all_ingredients = []
            for ingredient in range(ingredient_num):
                line_dict = {}
                line = recepies.readline().strip().split('|')
                line_dict['ingredient_name'] = line[0].strip()
                line_dict['quantity'] = int(line[1].strip())
                line_dict['measure'] = line[2].strip()
                all_ingredients.append(line_dict)
            cook_book[dish] = all_ingredients
            recepies.readline().strip()
    readable_print(cook_book)


def readable_print(cook_book):
    for dish, ingredients in cook_book.items():
        print(f'{dish}:')
        for type in ingredients:
            print(f"{type['ingredient_name']}: {type['quantity']} {type['measure']}")
        print()


def file_cycle(file_list=_get_all_files()):
    for file in file_list:
        working_with_file(file)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        recepie = cook_book[dish]
        for ingredient in recepie:
            amount = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
            if ingredient['ingredient_name'] not in shop_list:
                shop_list[ingredient['ingredient_name']] = amount
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] += amount['quantity']
    print(f'We habe to buy the following products to cook {dishes} for {person_count} pesrons:')
    for key, ingr in shop_list.items():
        print(key, end='')
        for i in ingr.values():
            print(f' {i}', end='')
        print()
    return shop_list

def main():
    file_cycle() # Firstly, reading all files in local /tmp assuming files are only there
    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Омлет', 'Фахитос'], 3)

main()
