from calculations.elastic_constants import ElasticConstants
from calculations.transformations import Transformations
from materials.fiber import Fiber
from materials.matrix import Matrix
import pandas as pd
import numpy as np


class Compound:
    name: str
    fiber: Fiber
    matrix: Matrix
    vf: float
    vm: float
    e1: float
    e2: float
    nu12: float
    nu21: float
    g12: float
    slt: np.array
    qlt: np.array
    theta: float
    sxy: np.array
    qxy: np.array
    alpha_vector: float
    beta_vector: float
    e_alpha_vector: float
    e_beta_vector: float

    def by_materials(
        self, fiber: Fiber, vf: float, matrix: Matrix, vm: float, fiber_angle: float
    ) -> None:
        self.fiber = fiber
        self.matrix = matrix
        self.vf = vf
        self.vm = vm
        self.theta = fiber_angle
        self.__create_name_from_materials()
        self.calc_elast_const()
        self.sxy = self.transform_slt2sxy(theta=fiber_angle)

    def __create_name_from_materials(self):
        name_fiber = self.fiber.get_name()
        name_matrix = self.matrix.get_name()
        self.name = f"{name_fiber} - {name_matrix}"

    def by_elastic_constans(
        self,
        name: str,
        e1: float,
        e2: float,
        nu12: float,
        nu21: float,
        g12: float,
        fiber_angle: float,
        alpha_1: float = 0,
        alpha_2: float = 0,
        beta_1: float = 0,
        beta_2: float = 0,
    ) -> None:
        self.name = name
        self.e1 = e1
        self.e2 = e2
        self.nu12 = nu12
        self.nu21 = nu21
        self.g12 = g12
        self.theta = fiber_angle
        self.alpha_vector = np.array([[alpha_1], [alpha_2], [0]])
        self.beta_vector = np.array([[beta_1], [beta_2], [0]])
        self.__calc_slt()
        self.__calc_qlt()
        self.sxy = self.transform_slt2sxy(theta=fiber_angle)
        self.__calc_ealpha()
        self.__calc_ebeta()

    def __calc_ealpha(self):
        self.e_alpha_vector = np.dot(self.qlt, self.alpha_vector)
        print(self.e_alpha_vector)

    def __calc_ebeta(self):
        self.e_beta_vector = np.dot(self.qlt, self.beta_vector)
        print(self.e_beta_vector)

    def calc_elast_const(self) -> None:
        ef, nuf, gf = self.fiber.extract_f3()
        em, num, gm = self.matrix.extract_f3()
        e1, e2, nu12, nu21, g12 = ElasticConstants.get_by_props(
            vf=self.vf, vm=self.vm, ef=ef, em=em, nuf=nuf, num=num, gf=gf, gm=gm
        )

        self.e1 = e1
        self.e2 = e2
        self.nu12 = nu12
        self.nu21 = nu21
        self.g12 = g12

        self.__calc_slt()
        self.__calc_qlt()
        self.__calc_ealpha()
        self.__calc_ebeta()

    def __calc_slt(self) -> None:
        self.slt = Transformations.slt(
            el=self.e1, et=self.e2, nul=self.nu12, nut=self.nu21, glt=self.g12
        )
        print(self.slt)

    def __calc_qlt(self) -> None:
        self.qlt = Transformations.qlt(
            el=self.e1, et=self.e2, nul=self.nu12, nut=self.nu21, glt=self.g12
        )
        print(self.qlt)

    def calc_sxy(self, theta: float) -> None:
        sxy = Transformations.slt_to_sxy(slt=self.slt, theta=theta)
        return sxy

    def get_mech_props(self) -> tuple:
        return (self.name, self.e1, self.e2, self.nu12, self.nu21, self.g12)

    def mech_props_to_pd(self) -> pd.DataFrame:
        dic = {
            "name": self.name,
            "vf": self.vf,
            "vm": self.vm,
            "e1": self.e1,
            "e2": self.e2,
            "nu12": self.nu12,
            "nu21": self.nu21,
            "g12": self.g12,
        }

        return pd.DataFrame([dic])

    def get_qlt(self):
        return self.qlt

    def get_stl(self):
        return self.slt

    def get_sxy(self):
        return self.sxy

    def transform_slt2sxy(self, theta: float):
        return Transformations.slt_to_sxy(slt=self.slt, theta=theta)
