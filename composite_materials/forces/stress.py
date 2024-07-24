import numpy as np


class Stress:
    __sx: float
    __sy: float
    __txy: float

    def __init__(self, sx: float, sy: float, txy: float) -> None:
        self.__sx = sx
        self.__sy = sy
        self.__txy = txy

    def get_vector(self) -> np.array:
        return np.array([[self.__sx], [self.__sy], [self.__txy]])
