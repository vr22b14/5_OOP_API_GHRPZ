### =====
### C:\Users\Romanov\Documents\000_MyDocs\00_doc_VR1_psw111\Netology_VR3\5_OOP_API_Repo\5_OOP_API_RPZ\PYAPI-78_5_2_task5_VR\main.py
### =====

with open('recipes.txt', 'r', encoding='UTF-8') as recipes:
    cook_book = {}
    for rec in recipes:
        if rec == '\n':
            continue
        else:
            list_dict = []
            name_recipes = rec.strip()
            count_ing = int(recipes.readline())
            for ing in range(count_ing):
                ingredient = recipes.readline().split('|')
                ing_dict = {'ingredient_name': ingredient[0],
                            'quantity': ingredient[1],
                            'measure': ingredient[2].strip()}
                list_dict.append(ing_dict)
                cook_book[name_recipes] = list_dict
    print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    amount_ingredients = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for i in cook_book.get(dish):
                ### dict_count = {'quantity': int(i.get('quantity')) * person_count, 'measure': i.get('measure')}
                dict_count = {'measure': i.get('measure'), 'quantity': int(i.get('quantity')) * person_count}
                amount_ingredients[i.get('ingredient_name')] = dict_count
    print(amount_ingredients)


print('=====')

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)