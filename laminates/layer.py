from materials.compound import Compound
from deformations.deformations import Deformations
from forces.stress import Stress
from deformations.delta_dimentions import DeltaDimentions

import numpy as np


class Layer:
    def __init__(
        self,
        composite: Compound,
        width: float = 0,
        lengh: float = 0,
        thickness: float = 0,
    ) -> None:
        self.__composite = composite
        self.__width = width
        self.__lengh = lengh
        self.__thickness = thickness
        self.__dimentions_vector = np.array([[lengh], [width], [thickness]])

    def get_deformations(self, stress: Stress, fiber_angle: float = None):
        stress_vector = stress.get_vector()
        if fiber_angle:
            flexibility_matrix = self.__composite.transform_slt2sxy(theta=fiber_angle)
        else:
            flexibility_matrix = self.__composite.get_sxy()
        return Deformations.get_deformation_vector(
            flexibility_matrix=flexibility_matrix, stress_vector=stress_vector
        )

    def get_delta_dimentions(self, stress: Stress, fiber_angle: float = None):
        deformations_vector = self.get_deformations(stress, fiber_angle)
        dx = deformations_vector[0] * self.__lengh
        dy = deformations_vector[1] * self.__width
        return np.array([dx, dy])

    def get_final_dimentions(self, stress: Stress, fiber_angle: float = None):
        delta_dimentions = self.get_delta_dimentions(
            stress=stress, fiber_angle=fiber_angle
        )
        lfx = delta_dimentions[0] + self.__lengh
        lfy = delta_dimentions[1] + self.__width
        return np.array([lfx, lfy])

    def get_deformations_by_delta_dimentions(self, delta_dimentions: DeltaDimentions):
        delta_dimentions_vector = delta_dimentions.get_vector()
        return Deformations.by_dimentions_and_detal_dimentions(
            dimentions=self.__dimentions_vector,
            delta_dimentions=delta_dimentions_vector,
        )
    
    def get_stress_vector(delta_dimentions: DeltaDimentions, temperature: float, humudity: float):
        pass