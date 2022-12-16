# Напишите программу, которая 
# по заданному номеру четверти, показывает диапазон
#  возможных координат точек в этой четверти (x и y)

number_quarter = int(input("введите номер четверти от 1 до 4 "))
if number_quarter !=1 and number_quarter !=2 and number_quarter !=3 and number_quarter != 4:
    print("ошибка ввода, повторите")
    exit(0)

if number_quarter ==1:
    print('X > 0; Y > 0')
elif number_quarter ==2:
    print('X < 0; Y > 0')
elif number_quarter ==3:
    print('X < 0; Y < 0')
else:
    print('X > 0; Y < 0')