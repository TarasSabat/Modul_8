from datetime import date, datetime, timedelta
from collections import defaultdict

USERS = [{"name": "Bill", "birthday": datetime(year=2023, month=10, day=29).date()},
    {"name": "Andrew", "birthday": datetime(year=2023, month=11, day=2).date()},
    {"name": "Jill", "birthday": datetime(year=2023, month=11, day=4).date()},
    {"name": "Till", "birthday": datetime(year=2023, month=11, day=5).date()},
    {"name": "Jan", "birthday": datetime(year=2023, month=11, day=6).date()},
    {"name": "A", "birthday": datetime(year=2023, month=11, day=7).date()},
    {"name": "B", "birthday": datetime(year=2023, month=11, day=8).date()},
    {"name": "C", "birthday": datetime(year=2023, month=11, day=10).date()}
]

date_today = date.today()
# day_today = date_today.strftime('%A') # строка день неділі

greeting = defaultdict(list)   # добавляння до одного ключа декількох значень 


def get_birthdays_per_week(users):
    d_0 = date_today - date_today
    d_7 = timedelta(days=7)
    # interval = timedelta(days=7)
    # d_7 = d_0 + interval
    this_year = False    
    if not users:
        return print('Список порожній')

    for el in users:
        time_delta =  el['birthday'] - date_today
        if time_delta <= d_0:  
            continue  
        elif time_delta >= d_7:
            this_year = True
            continue
        else:
            day_birthday = el['birthday'].strftime('%A') # строка день тижня дня народження
            if day_birthday == 'Saturday' or day_birthday == 'Sunday':
                greeting["Monday"].append(el["name"]) 
            else:
                greeting[day_birthday].append(el["name"])
    
    if not greeting and this_year == False:
        return print('Днів народжень цього року вже немає')
    else:
        print(greeting)
        greeting_dict = {} 
        for key, value in greeting.items():
            new_value = [f"'{name}'" for name in value]
            greeting_dict[key] = new_value
        return greeting_dict


print(get_birthdays_per_week(USERS))


# функція повертає словник користувачів- {'Monday': ['Bill', 'Jan'], 'Wednesday': ['Kim']}
