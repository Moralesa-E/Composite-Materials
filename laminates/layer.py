from materials.compound import Compound
from deformations.deformations import Deformations
from forces.stress import Stress
from deformations.delta_dimensions import DeltaDimensions

import numpy as np


class Layer:
    def __init__(
        self,
        composite: Compound,
        width: float = 0,
        length: float = 0,
        thickness: float = 0,
    ) -> None:
        self.__composite = composite
        self.__width = width
        self.__lengh = length
        self.__thickness = thickness
        self.__dimentions_vector = np.array([[length], [width], [thickness]])

    def get_deformations(self, stress: Stress, fiber_angle: float = None):
        stress_vector = stress.get_vector()
        if fiber_angle:
            flexibility_matrix = self.__composite.transform_slt2sxy(theta=fiber_angle)
        else:
            flexibility_matrix = self.__composite.get_sxy()
        return Deformations.get_deformation_vector(
            flexibility_matrix=flexibility_matrix, stress_vector=stress_vector
        )

    def get_delta_dimensions(self, stress: Stress, fiber_angle: float = None):
        deformations_vector = self.get_deformations(stress, fiber_angle)
        dx = deformations_vector[0] * self.__lengh
        dy = deformations_vector[1] * self.__width
        return np.array([dx, dy])

    def get_final_dimensions(self, stress: Stress, fiber_angle: float = None):
        delta_dimentions = self.get_delta_dimensions(
            stress=stress, fiber_angle=fiber_angle
        )
        lfx = delta_dimentions[0] + self.__lengh
        lfy = delta_dimentions[1] + self.__width
        return np.array([lfx, lfy])

    def get_deformations_by_delta_dimensions(self, delta_dimentions: DeltaDimensions):
        delta_dimentions_vector = delta_dimentions.get_vector()
        return Deformations.by_dimensions_and_delta_dimensions(
            dimensions=self.__dimentions_vector,
            delta_dimensions=delta_dimentions_vector,
        )

    def get_stress_vector(
        delta_dimentions: DeltaDimensions, temperature: float, humudity: float
    ):
        pass
