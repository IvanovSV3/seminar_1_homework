# Напишите программу, 
# которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.

coordinates_point_x1 = float(input('введите координату Х1 - '))
coordinates_point_y1 = float(input('введите координату Y1 - '))
coordinates_point_x2 = float(input('введите координату Х2 - '))
coordinates_point_y2 = float(input('введите координату Y2 - '))
print(coordinates_point_x1,coordinates_point_y1 , coordinates_point_x2, coordinates_point_y2)

lene_1_2 = (coordinates_point_x1 - coordinates_point_x2) * (coordinates_point_x1 - coordinates_point_x2)
print("Квадрат первой стороны = ", lene_1_2)
lene_2_2 = (coordinates_point_y1 - coordinates_point_y2) * (coordinates_point_y1 - coordinates_point_y2)
print("Квадрат второй стороны = ", lene_2_2)

distance = (lene_1_2 + lene_1_2) ** 0.5
print("Растояние между точками = ", "{:.3f}".format(distance))
