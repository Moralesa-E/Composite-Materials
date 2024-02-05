import numpy as np
from materials.compound import Compound


class Deformations:
    @staticmethod
    def get_deformation_vector(flexibility_matrix, stress_vector):
        return np.dot(flexibility_matrix, stress_vector)

    @staticmethod
    def by_dimentions_and_detal_dimentions(
        dimentions: np.array, delta_dimentions: np.array
    ):
        return delta_dimentions / dimentions
