#константы a=l b=t
import matplotlib.pyplot as plt
import numpy
import numpy as np
from matplotlib import pylab, cm
from mpl_toolkits.mplot3d import Axes3D
from math import *

k_T = 6500
c_T = 4190
p = 1000
T_T = 80
L = 1
D = 0.05
u = 0.2
t0 = L / u
t_max = 10
da = 0.3
db = 0.2
x=[]
y=[]
z=[]

def t_i(a, b) :
     return (a+b)
def l_i(a, b) :
     return u * (a - b)
#краевые условия
def T0 (l):
     return 30+l
def Tin (t):
    return 35-5*cos(t)

# T для нового шага
def nextT(prevT):
     return prevT + ((T_T - prevT) * (4 * k_T * da) / (c_T * p * D ))


def calcAndSavePart(a, b, t):
    x.append(t_i(a, b))
    y.append(l_i(a, b))
    z.append(t)# посмотреть синтаксис добавления в лист
    return nextT(t)

#первый шаг
b = -t0/2
while(b <= 0):
    #T начальное для текущего b
    T =T0(-2 * u * b)
    #Расчёт набора T по методу Эйлера для текущего b
    a=-b
    while a<=(t0+b):
        T = calcAndSavePart(a, b, T)
        a+=da
    b += db
#второй шаг
while (b <= (t_max-t0)/2):
    T =  Tin(2 * b)
    a = b
    while a<=(t0+b):
        T = calcAndSavePart(a, b, T)
        a+=da
    b += db
#третий шаг
while (b <= t_max/2):
    T =  Tin(2 * b)
    a = b
    while a <= (t_max - b):
        T = calcAndSavePart(a, b, T)
        a += da
    b += db


axes = Axes3D(pylab.figure())
axes.plot_trisurf(y, x, z, cmap='inferno', edgecolor='none',antialiased=False)
axes.set_xlabel('l')
axes.set_ylabel('τ')
axes.set_zlabel('T')

plt.gcf().canvas.set_window_title("4 Лабораторная")
pylab.show()