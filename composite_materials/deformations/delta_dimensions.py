import numpy as np


class DeltaDimensions:
    def __init__(self, dx: float = 0, dy: float = 0, tao_xy: float = 0) -> None:
        self.__dx = dx
        self.__dy = dy
        self.__tao_xy = tao_xy
        self.__vector = np.array([[dx], [dy], [tao_xy]])

    def get_vector(self):
        return self.__vector
