from math import sin, cos, pi
import numpy as np

# Matriz de transformacion T para esfuerzos 
def MT(Theta):
    Theta = Theta*(pi/180)
    T = np.array([  [(cos(Theta))**2,       (sin(Theta))**2,         2*sin(Theta)*cos(Theta)],
                    [(sin(Theta))**2,       (cos(Theta))**2,        -2*sin(Theta)*cos(Theta)],
                    [-sin(Theta)*cos(Theta), sin(Theta)*cos(Theta), ((cos(Theta))**2-(sin(Theta))**2)]])
    print(T)
    return T

# Matriz de transformacion T' para esfuerzos
def MTp(Theta):
    Theta = Theta*(pi/180)
    Tp = np.array([  [(cos(Theta))**2,      (sin(Theta))**2,       -2*sin(Theta)*cos(Theta)],
                    [(sin(Theta))**2,       (cos(Theta))**2,        2*sin(Theta)*cos(Theta)],
                    [sin(Theta)*cos(Theta), -sin(Theta)*cos(Theta), ((cos(Theta))**2-(sin(Theta))**2)]])
    print(Tp)
    return Tp

# Matriz de transformacion D para esfuerzos
def MD(Theta):
    Theta = Theta*(pi/180)
    D = np.array([  [(cos(Theta))**2,           (sin(Theta))**2,         sin(Theta)*cos(Theta)],
                    [(sin(Theta))**2,           (cos(Theta))**2,        -sin(Theta)*cos(Theta)],
                    [-2*sin(Theta)*cos(Theta), 2*sin(Theta)*cos(Theta), ((cos(Theta))**2-(sin(Theta))**2)]])
    print(D)
    return D

# Matriz de transformacion D' para esfuerzos
def MDp(Theta):
    Theta = Theta*(pi/180)
    Dp = np.array([  [(cos(Theta))**2,      (sin(Theta))**2,       -sin(Theta)*cos(Theta)],
                    [(sin(Theta))**2,       (cos(Theta))**2,        sin(Theta)*cos(Theta)],
                    [2*sin(Theta)*cos(Theta), -2*sin(Theta)*cos(Theta), ((cos(Theta))**2-(sin(Theta))**2)]])
    print(Dp)
    return Dp


def Slt(El, Et, vl, vt, Glt):
    Slt = np .array([   [1/El,  -vt/Et, 0],
                        [-vl/El, 1/Et,  0],
                        [0,      0,   1/Glt]])
    return Slt

def Qlt(El, Et, vl, vt, Glt):
    Qlt = np .array([   [El/(1-vl*vt),     (vt*El)/(1-vl*vt), 0],
                        [(vl*Et)/(1-vl*vt), Et/(1-vl*vt),     0],
                        [0,                 0,              Glt]])
    return Qlt

def Qxy(El, Et, vl, vt, Glt):
    Qlt = np .array([   [El/(1-vl*vt),     (vt*El)/(1-vl*vt), 0],
                        [(vl*Et)/(1-vl*vt), Et/(1-vl*vt),     0],
                        [0,                 0,              Glt]])
    return Qlt