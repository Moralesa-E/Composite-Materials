import numpy as np
from composite_materials.materials.compound import Compound


class Deformations:
    @staticmethod
    def get_deformation_vector(flexibility_matrix, stress_vector) -> np.ndarray:
        return np.dot(flexibility_matrix, stress_vector)

    @staticmethod
    def by_dimensions_and_delta_dimensions(
        dimensions: np.array, delta_dimensions: np.array
    ):
        return delta_dimensions / dimensions
