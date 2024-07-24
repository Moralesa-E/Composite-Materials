from composite_materials.materials.compound import Compound
from composite_materials.materials.fiber import Fiber
from composite_materials.materials.matrix import Matrix
from composite_materials.calculations.transformations import Transformations
from composite_materials.laminates.layer import Layer
from composite_materials.forces.stress import Stress
from composite_materials.deformations.deformations import Deformations
from composite_materials.deformations.delta_dimensions import DeltaDimensions

import pytest
import numpy as np


@pytest.fixture
def fiber_1():
    fiber_properties = {
        "name": "carbon",
        "elastic_module": 250,  # GPa
        "poisson_relation": 0.4,
        "cutting_module": 8.32,  # GPa
    }
    return Fiber(**fiber_properties)


@pytest.fixture
def matrix_1():
    matrix_properties = {
        "name": "epóxico",
        "elastic_module": 5.8,  # GPa
        "poisson_relation": 0.38,
        "cutting_module": 8.1,  # GPa
    }
    return Matrix(**matrix_properties)


@pytest.fixture
def compound_1(fiber_1, matrix_1):
    compound = Compound()
    compound.by_materials(fiber=fiber_1, vf=0.1, matrix=matrix_1, vm=0.9)
    return compound


@pytest.fixture
def compound_2():
    compound_properties = {
        "name": "vidrio - epoxico",
        "e1": 65.4,  # GPa
        "e2": 12.47,  # GPa
        "nu12": 0.254,
        "nu21": 0.254,
        "g12": 4.8,  # GPa
    }
    compound = Compound()
    compound.by_elastic_constants(**compound_properties)
    return compound


@pytest.fixture
def compound_3():
    compound_properties = {
        "name": "carbon - epóxico",
        "e1": 164.82,  # GPa
        "e2": 40.25,  # GPa
        "nu12": 0.286,
        "nu21": 0.286,
        "g12": 8.1,  # GPa
    }
    compound = Compound()
    compound.by_elastic_constants(**compound_properties)
    return compound


@pytest.fixture
def layer_1(compound_2):
    layer = Layer(
        composite=compound_2, length=85 / 1000, width=40 / 1000, thickness=0.5 / 1000
    )
    return layer


@pytest.fixture
def stress_1():
    stress_properties = {
        "sx": 95 / 1000,  # GPa
        "sy": 0,  # GPa
        "txy": 0,  # GPa
    }
    return Stress(**stress_properties)


def test_get_elastic_constants(compound_1):
    """Test get_elastic_constants method from Compound class."""
    elastic_constants = compound_1.get_elastic_constants()

    expected_elastic_constants = {
        "name": "carbon - epóxico",
        "e1": 30.22,  # GPa
        "e2": 6.43,  # GPa
        "nu12": 0.38,
        "nu21": 0.38,
        "g12": 8.12,  # GPa
    }

    assert elastic_constants == expected_elastic_constants


def test_slt(compound_2):
    slt = compound_2.get_stl()

    expected_slt = [[0.02, -0.02, 0], [0, 0.08, 0], [0, 0, 0.21]]

    assert np.array_equal(slt, expected_slt)


def test_slt_to_sxy(compound_2):
    sxy = compound_2.transform_slt2sxy(theta=10)

    expected_sxy = [[0.02, -0.02, 0.02], [-0.01, 0.08, -0.01], [0.03, 0, 0.2]]

    assert np.array_equal(sxy, expected_sxy)


def test_qlt(compound_3):
    qlt = compound_3.get_qlt()

    expected_qlt = [[179.50, 51.34, 0], [12.54, 43.84, 0], [0, 0, 8.10]]

    assert np.array_equal(qlt, expected_qlt)


def test_qlt_to_qxy(compound_3):
    qxy = compound_3.transform_qlt2qxy(theta=-90)

    expected_qxy = [[43.84, 12.54, 0], [51.34, 179.50, 0], [0, 0, 8.10]]

    assert np.array_equal(qxy, expected_qxy)


def test_layer_deformation(layer_1, stress_1):
    deformation = layer_1.get_deformations(stress_1, fiber_angle=0)
    print("-" * 100)
    print(deformation)
    print("-" * 100)

    expected_deformation = {
        "epsilon_x": 0.0004,
        "epsilon_y": -0.0001,
        "gamma_xy": 0.0003,
    }

    assert np.array_equal(deformation, expected_deformation)
