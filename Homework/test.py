from collections import namedtuple

# Оголошуємо іменований кортеж Cat
Cat = namedtuple('Cat', ['nickname', 'age', 'owner'])

def convert_list(cats):
    if isinstance(cats, list) and all(isinstance(cat, Cat) for cat in cats):
        # Якщо cats - список іменованих кортежів, перетворимо його на список словників
        return [{'nickname': cat.nickname, 'age': cat.age, 'owner': cat.owner} for cat in cats]
    elif isinstance(cats, list) and all(isinstance(cat, dict) for cat in cats):
        # Якщо cats - список словників, перетворимо його на список іменованих кортежів
        return [Cat(cat['nickname'], cat['age'], cat['owner']) for cat in cats]
    else:
        raise ValueError("Неправильний тип вхідного параметру cats")

# Приклади використання функції:
cats_namedtuple = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
cats_dict = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]

# Перетворення іменованих кортежів в словники
result_dict = convert_list(cats_namedtuple)
print(result_dict)

# Перетворення словників в іменовані кортежі
result_namedtuple = convert_list(cats_dict)
print(result_namedtuple)


