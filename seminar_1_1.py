# Напишите программу, которая 
# принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным

number = input('ведите число от 1 до 7 -  ')
number = int(number)
if number > 7 or number <1:
    print('ошибка ввода!!! - ведите число от 1 до 7 -  ')
else:
    if number == 1 or number == 2 or number ==3 or number == 4 or number == 5:
        print(number,"день не выходной")
    else:
        print(number,'день выходной')