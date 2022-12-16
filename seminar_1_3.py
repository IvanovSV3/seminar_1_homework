# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти 
# плоскости, в которой находится эта точка (или на какой оси она находится).

coordinates_point_x = float(input('введите координату Х не равную "0" - '))
while coordinates_point_x == 0:
    print('ошибка ввода, введите координату Х не равную "0"')
    exit(0)
coordinates_point_y = float(input('введите координату y не равную "0" - '))
while coordinates_point_y == 0:
    print('ошибка ввода, введите координату Y не равную "0"')
    exit(0)

if coordinates_point_x > 0 and coordinates_point_y > 0:
    print('точка находится в четверте I')
elif coordinates_point_x < 0 and coordinates_point_y > 0:
    print('точка находится в четверте II')
elif coordinates_point_x < 0 and coordinates_point_y < 0:
    print('точка находится в четверте III')
else:
    print('точка находится в четверте IV')