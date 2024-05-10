from materials.compound import Compound
from materials.fiber import Fiber
from materials.matrix import Matrix
from calculations.transformations import Transformations
from laminates.layer import Layer
from forces.stress import Stress
from deformations.deformations import Deformations
from deformations.delta_dimensions import DeltaDimensions

import pytest
import numpy as np


def test_get_elastic_constants():
    fiber_properties = {
        "name": "carbon",
        "elastic_module": 250,
        "poisson_relation": 0.4,
        "cutting_module": 8.32,
    }

    matrix_properties = {
        "name": "epóxico",
        "elastic_module": 5.8,
        "poisson_relation": 0.38,
        "cutting_module": 8.1,
    }

    fiber = Fiber(**fiber_properties)
    matrix = Matrix(**matrix_properties)

    compound = Compound()
    compound.by_materials(fiber=fiber, vf=0.1, matrix=matrix, vm=0.9)
    elastic_constants = compound.get_elastic_constants()

    expected_elastic_constants = {
        "name": "carbon - epóxico",
        "e1": 30.22,
        "e2": 6.43,
        "nu12": 0.38,
        "nu21": 0.38,
        "g12": 8.12,
    }

    assert elastic_constants == expected_elastic_constants


# def test_qlt():
#     compound_1 = Compound()
#     compound_1.by_elastic_constants(
#         e1=164.82, e2=40.25, nu12=0.286, nu21=0.286, g12=8.1, name="vidrio - polimerica"
#     )
#     compound_1_qlt = compound_1.get_qlt()
#     print(Transformations.qlt_to_qxy(qlt=compound_1_qlt, theta=-90))


def test_slt_to_sxy():
    compound_properties = {
        "name": "vidrio - epoxico",
        "e1": 65.4,
        "e2": 12.47,
        "nu12": 0.254,
        "nu21": 0.254,
        "g12": 4.8,
    }

    compound = Compound()
    compound.by_elastic_constants(**compound_properties)

    slt = compound.get_stl()
    sxy = compound.transform_slt2sxy(theta=10)

    expected_slt = [[0.02, -0.02, 0], [0, 0.08, 0], [0, 0, 0.21]]
    expected_sxy = [[0.02, -0.02, 0.02], [-0.01, 0.08, -0.01], [0.03, 0, 0.2]]

    assert np.array_equal(slt, expected_slt)
    assert np.array_equal(sxy, expected_sxy)
    # stress_1 = Stress(sx=0.095, sy=0, txy=0)
    # layer_1 = Layer(
    #     composite=compound, width=40 / 1000, length=85 / 1000, thickness=0.5 / 1000
    # )
    # print(layer_1.get_deformations(stress=stress_1))
    # print(layer_1.get_delta_dimensions(stress=stress_1))
    # print(layer_1.get_final_dimensions(stress=stress_1))
    # print(layer_1.get_delta_dimensions(stress=stress_1, fiber_angle=45))


# def test_all_layer():
#     compound_1 = Compound()
#     compound_1.by_elastic_constants(
#         e1=131,
#         e2=8.7,
#         nu12=0.28,
#         nu21=0.02,
#         g12=5,
#         name="vidrio - peek",
#         fiber_angle=0,
#         alpha_1=-0.2e-6,
#         alpha_2=24e-6,
#         beta_1=0,
#         beta_2=0.3,
#     )
#     d_1 = DeltaDimensions(dx=5)
#     layer_1 = Layer(
#         composite=compound_1, length=250 / 1000, width=50 / 1000, thickness=2 / 1000
#     )

#     print(layer_1.get_deformations_by_delta_dimensions(d_1))


# if __name__ == "__main__":
#     # test_compound()
#     # test_qlt()
#     # test_layer()
#     test_all_layer()
