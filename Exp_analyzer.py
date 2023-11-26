import math

import numpy as geek


#Задание параметров CUSUM алгоритма
import sys

k0 = 0
k1 = 0
h = 0
#Задание хар-к имитационного эксперимента
L = 0
k =0

#Ввод k0 и проверка
k0 = float(input("Введите интенсивность 0:"))

if k0 <= 0:
    print("Интенсивность 0 должна быть больше или равна 0")
    sys.exit("Перезапустите программу и введите корректное значение")

#Ввод k1 и проверка
k1 = float(input("Введите интенсивность 0:"))

if k1 <= 0:
    print("Интенсивность 1 должна быть больше или равна 0")
    sys.exit("Перезапустите программу и введите корректное значение")

#Ввод h и проверка
h = float(input("Введите решающий порог:"))

if h <= 0:
    print("Решающий порог должен быть больше или равна 0")
    sys.exit("Перезапустите программу и введите корректное значение")

#Ввод L и проверка
L = float(input("Введите длину выбоки:"))

if L <= 0:
    print("Длина выборки должна быть больше или равна 0:")
    sys.exit("Перезапустите программу и введите корректное значение")

#Ввод k и проверка
k = float(input("Введите интенсивность:"))

if k1 <= 0:
    print("Интенсивность должна быть больше или равна 0")
    sys.exit("Перезапустите программу и введите корректное значение")

#Генерация и реализация цикла
#array = geek.random.rand(5)

j = 0
T = 0
summ = 0
T_mas = []
while j < L:
    i = 1
    g = 0
    buf = 0
    mas = []
    mas.append(0)
    while mas[i] < h:
        r = geek.random.rand(1)
        x = (-1/k)*math.log1p(r)
        delta = math.log1p(k1/k0)-(k1-k0)*x
        buf = g + delta
        mas.append(buf)
        g = max(mas)
        max.pop()
        mas.append(g)
        i = i + 1
    T = i
    T_mas.append(T)
    summ = summ + T
    j = j + 1


#Обработка результатов
T_grade = summ/L

s = 0
summ_dif = 0
for s in T_mas:
    summ_dif = s**2 - T_grade**2

Q_grade = summ_dif/L

q_grade = Q_grade/(L**(0.5))










