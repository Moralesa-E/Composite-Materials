import numpy as np


class MediumPlane:
    __e0x: float
    __e0y: float
    __g0xy: float
    __kx: float
    __ky: float
    __kxy: float

    def __init__(
        self, e0x: float, e0y: float, g0xy: float, kx: float, ky: float, kxy: float
    ) -> None:
        self.__e0x = e0x
        self.__e0y = e0y
        self.__g0xy = g0xy
        self.__kx = kx
        self.__ky = ky
        self.__kxy = kxy

    def get_strains(self) -> np.array:
        return np.array([[self.__e0x], [self.__e0y], [self.__g0xy]])

    def get_curvatures(self) -> np.array:
        return np.array([[self.__kx], [self.__ky], [self.__kxy]])
