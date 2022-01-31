import math
 
print("Введите координаты точки: ")
x = float(input("x = "))
y = float(input("y = "))
print("Введите радиус окружности и координаты центра : ")
r = float(input("R = "))
xk = float(input("x(k) = "))
yk = float(input("y(k) = "))
 
 
if math.sqrt ((x - xk)**2  + (y - yk)**2 ) < r: 
    print("Точка лежит внутри окружности")
if math.sqrt ((x - xk)**2  + (y - yk)**2 ) > r: 
    print("Точка лежит снаружи окружности")
if math.sqrt ((x - xk)**2  + (y - yk)**2 ) == r: 
    print("Точка лежит на окружности")