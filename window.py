import numpy as np
from scipy.spatial import distance_matrix

x1=np.random.normal(size=100)
x2=np.random.normal(size=100)

def okna(u,v):
    return np.sqrt(sum((u+v)**2))

def CoreTriangle(r):
    if (abs(r) <=1):
        return (1-abs(r))
    else:
        return 0
def CoreRectangular(r):
    if(abs(r) <= 1):
        return 0.5
    else:
        return 0


def CoreQuartic(r):
    if (abs(r) <= 1):
        return((15/16)*(1 - (r^2))**2)
    else: 
        return 0

def CoreGaussian(r):
    return(((2*pi)^(-0.5))*exp(-0.5*(r^2)))

def CoreEpanechnikova(r):
    if(abs(r) <= 1):
        return((3/4)*(1 - (r^2)))
    else: 
        return 0    
    
h = 0.4 # изначально взяли 0.4
distances_weighted = distance_matrix(NA, l, 2) # что такое NA?
for i in range(1,l):
    distances_weighted[i, 1] = okna(xl[i, 1:n], u) # расстояния от классифицируемого объекта u до каждого i-го соседа
    z = distances_weighted[p, 1] / h # аргумент функции ядра
    cores = c(CoreRectangular(z), CoreTriangle(z), CoreQuartic(z), CoreGaussian(z), CoreEpanechnikova(z))
    distances_weighted[i, 2] = cores[1] # подсчёт веса для прямоугольного ядра
      
      