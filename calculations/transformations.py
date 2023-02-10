from math import sin, cos, pi
import numpy as np


class Transformations:

    def t(self, theta: float) -> np.array:
        """
        Matriz de transformacion T para esfuerzos
        """
        theta = theta*(pi/180)
        t = np.array([[(cos(theta))**2,       (sin(theta))**2,         2*sin(theta)*cos(theta)],
                      [(sin(theta))**2,       (cos(theta)) **
                       2,        -2*sin(theta)*cos(theta)],
                      [-sin(theta)*cos(theta), sin(theta)*cos(theta), ((cos(theta))**2-(sin(theta))**2)]])
        print(t)
        return t

    def tp(self, theta: float) -> np.array:
        """
        Matriz de transformacion T' para esfuerzos
        """
        theta = theta*(pi/180)
        tp = np.array([[(cos(theta))**2,      (sin(theta))**2,       -2*sin(theta)*cos(theta)],
                       [(sin(theta))**2,       (cos(theta)) **
                        2,        2*sin(theta)*cos(theta)],
                       [sin(theta)*cos(theta), -sin(theta)*cos(theta), ((cos(theta))**2-(sin(theta))**2)]])
        print(tp)
        return tp

    def d(self, theta: float) -> np.array:
        """
        Matriz de transformacion D para esfuerzos
        """
        theta = theta*(pi/180)
        d = np.array([[(cos(theta))**2,           (sin(theta))**2,         sin(theta)*cos(theta)],
                      [(sin(theta))**2,           (cos(theta))
                       ** 2,        -sin(theta)*cos(theta)],
                      [-2*sin(theta)*cos(theta), 2*sin(theta)*cos(theta), ((cos(theta))**2-(sin(theta))**2)]])
        print(d)
        return d

    def dp(self, theta: float) -> np.array:
        """
        Matriz de transformacion D' para esfuerzos
        """
        theta = theta*(pi/180)
        dp = np.array([[(cos(theta))**2,      (sin(theta))**2,       -sin(theta)*cos(theta)],
                       [(sin(theta))**2,       (cos(theta))
                        ** 2,        sin(theta)*cos(theta)],
                       [2*sin(theta)*cos(theta), -2*sin(theta)*cos(theta), ((cos(theta))**2-(sin(theta))**2)]])
        print(dp)
        return dp

    def slt(self, el: float, et: float, nul: float, nut: float, glt: float) -> np.array:
        slt = np .array([[1/el,  -nut/et, 0],
                         [-nul/el, 1/et,  0],
                         [0,      0,   1/glt]])
        return slt

    def slt_to_sxy(self, slt: np.array, theta: float) -> np.array:
        return self.d(theta)*slt*self.tp(theta)

    def qlt_to_qxy(self, qlt: np.array, theta: float) -> np.array:
        return self.t(theta=theta)*qlt*self.dp(theta=theta)

    def qlt(self, el: float, et: float, nul: float, nut: float, glt: float) -> np.array:
        qlt = np .array([[el/(1-nul*nut),     (nut*el)/(1-nul*nut), 0],
                         [(nul*et)/(1-nul*nut), et/(1-nul*nut),     0],
                         [0,                 0,              glt]])
        return qlt
