''' З допомогою datetime заміряємо тривалістьвиконання оперції'''
# from datetime import datetime

# def for_generator():
    
#     my_list = []
    
#     for i in range(0, 1000000):
#         my_list.append(i)

# def comprehensions_generator():

#     my_list = [i for i in range(0, 1000000)]

# n = 300
# for_times = []
# comprehensions_times = []

# for i in range(0, n):
    
#     start = datetime.now().timestamp()
#     for_generator()
#     end = datetime.now().timestamp()
#     result = end - start
#     for_times.append(result)

#     start = datetime.now().timestamp()
#     comprehensions_generator()
#     end = datetime.now().timestamp()
#     result = end - start
#     comprehensions_times.append(result)

# print(sum(for_times) / n)
# print(sum(comprehensions_times) / n)

''' Розрахунок кількості днів до вказаної дати і запис інфрмації у файл '''
# from datetime import datetime

# def get_days():
#     global delta_days
#     global target_date

#     user_input = input("Введіть дату в форматі dd.mm: ")
#     user_date = datetime.strptime(user_input, '%d.%m' )     # метод переведення строки в час
#     current_date = datetime.now()                           # метод виведення поточного часу
#     user_date = user_date.replace(year=current_date.year)   # метод заміни певного показника (year)
#     delta_days = user_date - current_date
#     target_date = datetime.strftime(user_date, '%d-%B-%Y')  # метод переведення об'єкт часму в строку
    
#     if delta_days.days > 0:
#         print(f'{delta_days.days} days left befor {target_date}') 
#     else:
#         user_date = user_date.replace(year=current_date.year + 1)
#         delta_days = user_date - current_date 
#         print(f'{delta_days.days} days left befor {target_date}')
   
# def make_backup(a, b):
#     current_time = datetime.now()
#     with open(f'backup_{current_time.timestamp()}.txt', 'w') as fh:
#         fh.write(f"{a.days} days left befor, {b}")


# if __name__ == '__main__':
#     get_days()
#     make_backup(delta_days, target_date)
    
"Отримання списка випадкових днів народження (random)"
# from datetime import datetime, timedelta
# import random

# def get_random_birthdays(n):
#     current_date = datetime.now()
#     oldest_dayt = current_date - timedelta(days = 365 * 85)
#     birthdays_list = []
#     for i in range(n):
#         fake_year = random.randrange(oldest_dayt.year, current_date.year)
#         fake_month = random.randint(1, 12)
#         fake_day = random.randint(1, 31)
#         try: 
#             fake_dirthday = datetime(year=fake_year, month=fake_month, day=fake_day)
#         except ValueError:
#             continue
#         birthdays_list.append(fake_dirthday.date())
#     return birthdays_list
        

# if __name__ == '__main__':
#     birthdays_list = get_random_birthdays(5)
#     print(random.sample(birthdays_list, k = 5 )) # random.choice - вибирає один елемент зі списку, 
                                                 # random.choices - вибирає k елемент зі списку, 
                                                 # random.sample - виводить унікальні значення але k не має бути більшим за кількість виведених елементів 
                                                 # random.shuffle - перемішує список

''' Cillection '''
# from collections import namedtuple

# person_1 = ('Bob', 30, 'Kyiv')

# print(f'Simple Tuple: Name {person_1[0]} Age {person_1[1]} City {person_1[2]}')

''' Створення уніфікоіваного іменованого кортежу '''

# Person = namedtuple('Person', ['name', 'age', 'caty'])

# person_2 = Person('Nike', 40, 'Lviv')
# person_3 = Person('Olena', 30, 'Odesa')

# print(f'Named Tuple: Name {person_2.name} Age {person_2[1]} City {person_2.caty}') # дозволяє звертатися і по назві   
                                                                                    # і по індексу 

''' Counter '''
# from collections import Counter

# text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean dictum sollicitudin libero in accumsan. Vestibulum tincidunt nisi fringilla ligula faucibus blandit. Integer vitae porttitor odio. Mauris aliquam velit nec sem scelerisque cursus. Suspendisse malesuada, mauris non iaculis euismod, nisl ex facilisis nisi, ut molestie orci neque id tortor. Vivamus aliquet magna ut pellentesque blandit. Morbi eu turpis ex. Duis vitae sodales nulla, nec tincidunt nulla. Mauris interdum, ex sit amet congue facilisis, felis dolor fringilla orci, a tincidunt magna augue et sem. Lorem ipsum dolor sit amet, consectetur adipiscing elit. In et dui eu felis hendrerit faucibus eu et eros. Suspendisse magna nisl, dapibus nec nisi et, hendrerit dictum nibh. Donec mauris justo, pulvinar ut lobortis vitae, lacinia a dui. Suspendisse dolor lectus, ornare quis elit eu, lobortis feugiat libero.'''

''' Звичайний спосіб '''
# def get_count_chars(text):
#     count_dict = {}
#     for i in text:
#         num = count_dict.get(i)
#         if num:
#             count_dict[i] = num + 1
#         else:
#             count_dict[i] = 1
#     print(count_dict)

# get_count_chars(text)

''' аналогічне сортування за допомогою Counter '''
# counter = Counter(text)
# print(counter) 
# print(counter.most_common(5))  # виводить 5 найбільш повторюваних
# print(sorted(counter))           # виводить відсортований список елементів

''' defaultdict 
- спеціальний словник, який створює значення для ключів, яктх в словнику не було за запитом '''

# from collections import defaultdict

# text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean dictum sollicitudin libero in accumsan. Vestibulum tincidunt nisi fringilla ligula faucibus blandit. Integer vitae porttitor odio. Mauris aliquam velit nec sem scelerisque cursus. Suspendisse malesuada, mauris non iaculis euismod, nisl ex facilisis nisi, ut molestie orci neque id tortor. Vivamus aliquet magna ut pellentesque blandit. Morbi eu turpis ex. Duis vitae sodales nulla, nec tincidunt nulla. Mauris interdum, ex sit amet congue facilisis, felis dolor fringilla orci, a tincidunt magna augue et sem. Lorem ipsum dolor sit amet, consectetur adipiscing elit. In et dui eu felis hendrerit faucibus eu et eros. Suspendisse magna nisl, dapibus nec nisi et, hendrerit dictum nibh. Donec mauris justo, pulvinar ut lobortis vitae, lacinia a dui. Suspendisse dolor lectus, ornare quis elit eu, lobortis feugiat libero.'''

''' Звичайний спосіб '''
# def get_word_list(text):
#     word_list = text.split(' ')
#     word_dikt = {}
#     for i in word_list:
#         word = word_dikt.get(i[0])
#         if word:
#             word.append(i)
#         else:
#             word_dikt[i[0]] = [i]
#     print(word_dikt)

# get_word_list(text)

''' аналогічне сортування за допомогою defaultdict '''

# def get_word_list_dd(text):
#     word_list = text.split(' ')
#     word_dikt = defaultdict(list)
#     for i in word_list:
#         word = i[0]
#         word_dikt[word].append(i)
#     print(word_dikt)

# get_word_list_dd(text)
 
''' deque '''

# from collections import deque

# def main():
#     queue = deque(maxlen=10)
#     for i in range(20):
#         # queue.append(i)     # deque([10, 11, 12, 13, 14, 15, 16, 17, 18, 19], maxlen=10)
#         queue.appendleft(i) # deque([19, 18, 17, 16, 15, 14, 13, 12, 11, 10], maxlen=10)
#     print(queue)
#     start = queue.popleft() # 19 бере елемент з початку черги 
#     end = queue.pop()       # 10 бере елемент з кінця черги
#     print(start)
#     print(end)

# main()
#####
# from collections import deque

# def main():
#     user_inputs = deque(maxlen = 10) # обмеження кількості збережених елементів - 10
#     while True:
#         user_input = input('>>> ')
#         user_inputs.append(user_input)
#         if user_input == 'q':
#             break
#         print(f'User steps: {user_inputs}')
#     print('Good buy !')
    
# main()

''' Comprehension '''
''' використання звичайного способу '''
# def get_numbers(x):
#     numbers = []
#     for i in range(x):
#         num = i ** 2
#         if num % 2:
#             numbers.append(num)
#     print(numbers)

# get_numbers(20)

''' аналогічно з використанням Comprehension '''
# def get_numbers_short(x):
#     numbers = [i**2 for i in range(x) if i%2] # [1, 9, 25, 49, 81, 121, 169, 225, 289, 361] <class 'list'> список
#     print(numbers, type(numbers))

# get_numbers_short(20)
###
# def get_numbers_short(x):
#     numbers = {i**2 for i in range(x) if i%2} # {1, 121, 225, 289, 9, 169, 361, 81, 49, 25} <class 'set'> множини
#     print(numbers, type(numbers))

# get_numbers_short(20)
###
# def get_numbers_short(x):
#     numbers = {f'{i}^2': i**2 for i in range(x) if i%2} # {'1^2': 1, '3^2': 9, '5^2': 25, '7^2': 49, '9^2': 81, 
#                                                         #'11^2': 121,  '13^2': 169, '15^2': 225, '17^2': 289, '19^2': 361}   
                                                          # <class 'dict'> словник
#     print(numbers, type(numbers))

get_numbers_short(20)
