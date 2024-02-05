import numpy as np
from transformations import Transformations


class Calculations(Transformations):
    def strains_xy(self, s_xy: np.array, sig_xy) -> np.array:
        return s_xy * sig_xy
