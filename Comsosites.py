import numpy as np


def Sort(Ex, Ey, Ez, Nyz, Nzx, Nxy, Gyz, Gzx, Gxy):
    S = np.array([  [1/Ex, -Nxy/Ey, -Nzx/Ez, 0, 0, 0],
                    [-Nxy/Ex, 1/Ey, -Nyz/Ez, 0, 0, 0],
                    [-Nzx/Ex, -Nyz/Ey, 1/Ez, 0, 0, 0],
                    [0,       0,       0, 1/Gyz,     0,     0],
                    [0,       0,       0,     0, 1/Gzx,     0],
                    [0,       0,       0,     0,     0, 1/Gxy]])
    return S

Largo = 30/100
Ancho = Largo

Espesor = 0.1/100
F1 = 80e3
F2 = -5e3

E1 = 187.25e9
nu23 = 0.467
G23 = 3.72e9

E2 = 25.84e9
nu12 = 0.278
G12 = 4.1e9

#=============== Solution

Sigma1 = F1/(Ancho*Espesor)
Sigma2 = F2/(Largo*Espesor)

Sigma = np.array([[Sigma1], [Sigma2],[0] ,[0] ,[0] ,[0]])

S = Sort(E1,E2,E2,nu23,nu12,nu12,G23,G12,G12)
Epsilon = np.dot(S, Sigma)
dx = Epsilon[0]*Largo
dy = Epsilon[1]*Ancho
dz = Epsilon[2]*Espesor

print(Epsilon)
print(dx)
print(dy)
print(dz)