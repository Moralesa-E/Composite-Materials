from math import sin, cos, pi
import numpy as np


class Transformations:

    def t(self, theta: float) -> np.array:
        """
        Matriz de transformacion T para esfuerzos
        """
        theta = theta*(pi/180)
        t = np.array([[(cos(theta))**2,       (sin(theta))**2,         2*sin(theta)*cos(theta)],
                      [(sin(theta))**2,       (cos(theta))**2,        -2*sin(theta)*cos(theta)],
                      [-sin(theta)*cos(theta), sin(theta)*cos(theta), ((cos(theta))**2-(sin(theta))**2)]])
        print(t)
        return t

    def tp(self, theta: float) -> np.array:
        """
        Matriz de transformacion T' para esfuerzos
        """
        theta = theta*(pi/180)
        tp = np.array([[(cos(theta))**2,      (sin(theta))**2,       -2*sin(theta)*cos(theta)],
                       [(sin(theta))**2,       (cos(theta))**2,        2*sin(theta)*cos(theta)],
                       [sin(theta)*cos(theta), -sin(theta)*cos(theta), ((cos(theta))**2-(sin(theta))**2)]])
        print(tp)
        return tp

    def d(self, theta: float) -> np.array:
        """
        Matriz de transformacion D para esfuerzos
        """
        theta = theta*(pi/180)
        d = np.array([[(cos(theta))**2,           (sin(theta))**2,         sin(theta)*cos(theta)],
                      [(sin(theta))**2,           (cos(theta))**2,        -sin(theta)*cos(theta)],
                      [-2*sin(theta)*cos(theta), 2*sin(theta)*cos(theta), ((cos(theta))**2-(sin(theta))**2)]])
        print(d)
        return d

    def mdp(self, theta: float) -> np.array:
        """
        Matriz de transformacion D' para esfuerzos
        """
        theta = theta*(pi/180)
        dp = np.array([[(cos(theta))**2,      (sin(theta))**2,       -sin(theta)*cos(theta)],
                       [(sin(theta))**2,       (cos(theta))**2,        sin(theta)*cos(theta)],
                       [2*sin(theta)*cos(theta), -2*sin(theta)*cos(theta), ((cos(theta))**2-(sin(theta))**2)]])
        print(dp)
        return dp

    def slt(self, el: float, et: float, vl: float, vt: float, glt: float) -> np.array:
        slt = np .array([[1/el,  -vt/et, 0],
                         [-vl/el, 1/et,  0],
                         [0,      0,   1/glt]])
        return slt

    def qlt(self, el: float, et: float, vl: float, vt: float, glt: float) -> np.array:
        qlt = np .array([[el/(1-vl*vt),     (vt*el)/(1-vl*vt), 0],
                         [(vl*et)/(1-vl*vt), et/(1-vl*vt),     0],
                         [0,                 0,              glt]])
        return qlt

    def qxy(self, el: float, et: float, vl: float, vt: float, glt: float) -> np.array:
        qxy = np .array([[el/(1-vl*vt),     (vt*el)/(1-vl*vt), 0],
                         [(vl*et)/(1-vl*vt), et/(1-vl*vt),     0],
                         [0,                 0,              glt]])
        return qxy

    def slt_to_sxy(self, slt: np.array, theta: float) -> np.array:

        return self.md(theta)*slt*self.mtp(theta)