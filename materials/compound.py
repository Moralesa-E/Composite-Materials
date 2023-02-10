from calculations.elastic_constants import ElasticConstants
from calculations.transformations import Transformations
from fiber import Fiber
from matrix import Matrix
import pandas as pd
import numpy as np


class Compound:

    name: str
    fiber: Fiber
    matrix: Matrix
    vf: float
    vm: float
    eclt: float
    ectt: float
    clhe: float
    cthe: float
    e1: float
    e2: float
    nu12: float
    nu21: float
    g12: float
    slt: np.array
    qlt: np.array

    def __init__(self, name: str, fiber: Fiber = None, matrix: Matrix = None, vf: float = None, vm: float = None, eclt: float = None, ectt: float = None, clhe: float = None, cthe: float = None) -> None:

        self.name = name
        self.fiber = fiber
        self.matrix = matrix
        self.vf = vf
        self.vm = vm
        self.eclt = eclt
        self.ectt = ectt
        self.clhe = clhe
        self.cthe = cthe

    def add_elast_const(self, e1: float = None, e2: float = None, nu12: float = None, nu21: float = None, g12: float = None) -> None:
        self.e1 = e1
        self.e2 = e2
        self.nu12 = nu12
        self.nu21 = nu21
        self.g12 = g12

    def calc_elast_const(self) -> None:

        ef, nuf, gf = self.fiber.extract_f3()
        em, num, gm = self.matrix.extract_f3()
        elas_const = ElasticConstants()
        e1, e2, nu12, nu21, g12 = elas_const.get_by_props(
            vf=self.vf, vm=self.vm, ef=ef, em=em, nuf=nuf, num=num, gf=gf, gm=gm)

        self.e1 = e1[0]
        self.e2 = e2[0]
        self.nu12 = nu12[0]
        self.nu21 = nu21[0]
        self.g12 = g12

        self.calc_slt()

    def add_elast_const(self, e1: float, e2: float, nu12: float, nu21: float, g12: float) -> None:
        self.e1 = e1
        self.e2 = e2
        self.nu12 = nu12
        self.nu21 = nu21
        self.g12 = g12

        self.calc_slt()

    def calc_slt(self) -> None:
        self.slt = Transformations().slt(el=self.e1, et=self.e2,
                                         nul=self.nu12, nut=self.nu21, glt=self.g12)
        print(self.slt)

    def calc_qlt(self) -> None:
        self.qlt = Transformations().qlt(el=self.e1, et=self.e2,
                                         nul=self.nu12, nut=self.nu21, glt=self.g12)
        print(self.qlt)

    def calc_sxy(self, theta: float) -> None:
        sxy = Transformations().slt_to_sxy(slt=self.slt, theta=theta)
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
            "g12": self.g12
        }

        return pd.DataFrame([dic])
