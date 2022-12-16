# Напишите программу для. проверки 
# истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

x = int(input("введите значения X  Истина 0 или Лож 1 "))
if x == 1:
    x = True
else:
    x = False
y = int(input("введите значения Y  Истина 0 или Лож 1 "))
if y == 1:
    x = True
else:
    y = False
z = int(input("введите значения Y  Истина 0 или Лож 1 "))
if z == 1:
    z = True
else:
    z = False
                        # print(x,y,z)

if (not x and not y and not z) == True:
    right_side = True
else:
    right_side = False
print("правая сторна", right_side)

if  not (x or y or z) == True:
    left_side = True
else:
    left_side = False
print("левая сторна", left_side)

print("--------------------")

if left_side == right_side:
    print("выражение истино")
else:
    print("выражение ложно")