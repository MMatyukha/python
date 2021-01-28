#1------------------------------------
my_list = [2, 2.5, 'False',(4,5)]
for i in range(len(my_list)):
    print(type(my_list[i]))

#2------------------------------------

x = int(input("Введите количество элементов списка "))
my_list = []
i = 0
y = 0
while i < x:
    my_list.append(input("Введите следующее значение списка "))
    i += 1

for z in range(int(len(my_list)/2)):
        my_list[y], my_list[y + 1] = my_list [y + 1], my_list[y]
        y += 2
print(my_list)

#3--------------------------------------------------------------
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
month = int(input('Введите номер  месяца '))
if month in (12,1,2):
        print(seasons_dict.get(1),end='-')
        print(seasons_list[0])
elif month in (3,4,5):
    print(seasons_dict.get(2),end='-')
    print(seasons_list[1])
elif month in (6,7,8):
    print(seasons_dict.get(3),end='-')
    print(seasons_list[2])

elif month in (9,10,11):
    print(seasons_dict.get(4),end='-')
    print(seasons_list[3])
else:
        print("Такого месяца не существует")

#4-------------------------------------------
my_str = input("введите строку ")
my_word = []
num = 1
for x in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word [x]}")
        num += 1
    else:
        print(f" {num} {my_word [x] [0:9]}")
        num += 1


#5--------------------------------------------------
my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
x = int(input("Введите число "))
while x != 99:
    for i in range(len(my_list)):
        if my_list[i] == x:
            my_list.insert(i + 1, x)
            break
        elif my_list[0] < x:
            my_list.insert(0, x)
        elif my_list[-1] > x:
            my_list.append(x)
        elif my_list[i] > x and my_list[i + 1] < x:
            my_list.insert(i + 1, x)
    print(f"текущий список - {my_list}")
    x = int(input("Введите число "))

#6------------------------------------------------
goods = int(input("Введите количество товара "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= goods:
    my_dict = dict({'название': input("введите название "), 'цена': input("Введите цену "),
                    'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    my_list.append((n, my_dict))
    n += 1
    my_analys = dict(
        {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
         'ед': my_dict.get('ед')})
print(my_list)
print(my_analys)


