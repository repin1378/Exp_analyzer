from random import uniform

import pandas
from tkinter import filedialog

print("Программа генерации бинарного случайного процесса 2-го порядка")
# фунция инверсии
def invers(x):
    if x == 1:
        return 0
    else:
        return 1


# Ввод а (вероятность появления случайного события; 0 ≤ а ≤ 1)
a=float(input("Введите значение переменной а (вероятность появления случайного события 0 ≤ а ≤ 1: "))
#  print("a_old:", a_old)

if a<0 or a>1 :
    print("Не верно введено значение a")
    exit()
else:
    print("Знаение a корректно")
print("a:", a)


# Ввод b (вероятность появления случайного события; 0 ≤ b ≤ 1)
b=float(input("Введите значение переменной а (вероятность появления случайного события 0 ≤ b ≤ 1: "))
# print("b_old:", b_old)

if b<0 or b>1 :
    print("Не верно введено значение b")
    exit()
else:
    print("Знаение b корректно")
print("b:", b)


# Длина формируемого процесса N
N=int(input("Введите значение переменной N длина формируемого процесса: "))

if N<2 :
    print("Не верно введено значение N. Знаение не может быть меньше 2")
    exit()
else:
    print("Знаение b корректно")
    print("N:", N)


# получение случайного равномерно распределенного в диапазоне [0-1] числа u с помощью модуля random.uniform языка
u=uniform(0,1)
# print("u:",u)

# получение случайного равномерно распределенного в диапазоне [0-1] числа u с помощью модуля random.uniform языка
v=uniform(0,1)
# print("v:",v)

# определение z(0):   z(0) = 1, если u ≤ а ; иначе z(0) = 0;
if u<=a:
    Z0=1
else:
    Z0=0

# print("z(0) = ",Z0)

# определение z(-1):   z(-1) = 1, если v ≤ b ; иначе z(-1) = 0;
if v<=b:
    Z_1=1
else:
    Z_1=0

# print("z(-1) = ",Z_1)

# генерация спсиков u(k) и v(k)
uk = [uniform(0,1) for x in range(N)]
# print("uk:", uk)

vk = [uniform(0,1) for x in range(N)]
# print("vk:", vk)

# генерация списков е1(k) и е2(k)
e1 = [0]*N
for i in range(N):
    if uk[i] <= a:
        e1[i] = 1
    else:
        e1[i] = 0

# print("e1:", e1)

e2 = [0]*N
for i in range(N):
    if vk[i] <= b:
        e2[i] = 1
    else:
        e2[i] = 0

# print("e2:", e2)

# Реализации бинарного процесс z(k)
z = [0]*N
z[0] = Z0 & invers(e1[0]) & invers(e2[0]) | invers(Z0) & e1[0] & e2[0] | Z_1 & invers(e1[0]) & e2[0] | invers(Z_1) & e1[0] & invers(e2[0])
z[1] = z[0] & invers(e1[1]) & invers(e2[1]) | invers(z[0]) & e1[1] & e2[1] | Z0 & invers(e1[1]) & e2[1] | invers(Z0) & e1[1] & invers(e2[1])
number = 2
while number < N:
    z[number] = z[number-1] & invers(e1[number]) & invers(e2[number]) | invers(z[number-1]) & e1[number] & e2[number] | z[number-2] & invers(e1[number]) & e2[number] | invers(z[number-2]) & e1[number] & invers(e2[number])
    number += 1

# print("Итоговый спсиок", z)

# Имя листа
sheet="a="+str(a)+";"+"b="+str(b)+";"+"N="+str(N);


# Запись в  файл

path = filedialog.asksaveasfile(initialdir="/", title="Save file", defaultextension=".xlsx",
                                filetypes=(("excel files", "*.xlsx "), ("all files", "*.*")))



df = pandas.DataFrame({"z function":z})
df.to_excel(excel_writer=path.name, sheet_name=sheet, index=False, header=None)
