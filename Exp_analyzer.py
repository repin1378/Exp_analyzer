import math
from tkinter import filedialog

import numpy as geek
import sys
from datetime import datetime

#==========================Переменные========================

#Задание параметров CUSUM алгоритма
import pandas

k0 = 0  #лямбда 0
k1 = 0  #лямбда 1
h = 0   #решающий порог

#Задание хар-к имитационного эксперимента
L = 0   #количество повторных запусков
k =0    #лябда в эксп распределении
#=============================================================

current_datetime = datetime.now()
print('Запуск программы:',current_datetime)
data_str = current_datetime.strftime("%d-%m-%Y_%H-%M-%S")
file_name = 'result_' + data_str + '.txt'
file = open(file_name, "w")

#==========================Консольный ввод и проверка========================

#Ввод k0 и проверка
k0 = float(input("Введите лямбда 0:"))

if k0 <= 0:
    print("Лямбда 0 должна быть больше 0")
    sys.exit("Перезапустите программу и введите корректное значение")

#Ввод k1 и проверка
k1 = float(input("Введите лямбда 1:"))

if k1 <= 0:
    print("Лямбда 1 должна быть больше 0")
    sys.exit("Перезапустите программу и введите корректное значение")

if k0 == k1:
    print("Лямбда 0 Лямда 1 не должны быть равны")
    sys.exit("Перезапустите программу и введите корректное значение")

#Ввод h и проверка
h = float(input("Введите решающий порог:"))

if h <= 0:
    print("Решающий порог должен быть больше 0")
    sys.exit("Перезапустите программу и введите корректное значение")

#Ввод L и проверка
L = float(input("Введите количество повторных запусков:"))

if L <= 0:
    print("Количество повторных запусков должно быть больше 0:")
    sys.exit("Перезапустите программу и введите корректное значение")

#Ввод k и проверка
k = float(input("Введите лямбда:"))

if k <= 0:
    print("Лямбда должна быть больше 0")
    sys.exit("Перезапустите программу и введите корректное значение")

#============================================================================
print ("НАЧАЛО РАСЧЕТА:")
file.write("НАЧАЛО РАСЧЕТА:\n")

print("Лямбда 0: ", k0)
k0_str = str(k0)
k0_out = "Лямбда 0: " + k0_str + "\n"
file.write(k0_out)

print("Лямбда 1: ", k1)
k1_str = str(k1)
k1_out = "Лямбда 1: " + k1_str + "\n"
file.write(k1_out)

print("Решающий порог: ", h)
h_str = str(h)
h_out = "Решающий порог: " + h_str + "\n"
file.write(h_out)

print("Количество повторных запусков: ", L)
L_str = str(L)
L_out = "Количество повторных запусков: " + L_str + "\n"
file.write(L_out)

print("Лямбда: ", k)
k_str = str(k)
k_out = "Лямбда: " + k_str + "\n"
file.write(k_out)

#===============================Генерация временного ряда=====================

T = 0
summ = 0
summx2 = 0
T_mas = []
mas = []                                           #список gi
while len(T_mas) < L:
    i = 0
    g = 0                                          #g0 = 0
    buf = 0                                        #сбросить значение gi перед циклом
    mas.clear()                                    #почистить список gi
    mas.append(0)                                  #g0 = 0
    while buf < h:
        ravn = geek.random.rand(1)             #список из одного элемента с равномерным распредлением
        r = ravn[0]                                #извлечь элемент из списка
        x = (-1/k)*math.log(r)                      #xi = (-1/лямбда)*ln(ri)
        delta = math.log(k1/k0)-((k1-k0)*x)         #deltagi = ln(лямбда1/лямбда0) - (лямбда1-лямбда0)*xi
        buf = mas[-1] + delta                       #gi = g(i-1)+deltagi
        if buf >= 0:                                #условие добавления в список
            mas.append(buf)
        else:
            mas.append(0)
        i = i + 1
        if mas[-1] >= h:                            #условие добавления в список
            mas_buf = mas
    T = len(mas)
    T_mas.append(T)
    summ = summ + T
    summx2 = summx2 + T*T


#==================Обработка результатов (мат ожидание и дисперсия)===================
T_grade = summ/L
print("Мат ожидание:", T_grade)
T_grade_str = str(T_grade)
T_grade_out = "Мат ожидание: " + T_grade_str + "\n"
file.write(T_grade_out)

Q_buff = summx2/L
Q_grade = Q_buff - T_grade**2
print("Дисперсия:", Q_grade)
Q_grade_str = str(Q_grade)
Q_grade_out = "Дисперсия: " + Q_grade_str + "\n"
file.write(Q_grade_out)

q_grade = Q_grade/(L**(0.5))
print("Мат отклонение:", q_grade)
q_grade_str = str(q_grade)
q_grade_out = "Мат отклонение: " + q_grade_str + "\n"
file.write(q_grade_out)

#=====================================================================================
file.close()
input('Нажмите Enter чтобы завершить программу...')









