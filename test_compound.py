from materials.compound import Compound
from materials.fiber import Fiber
from materials.matrix import Matrix
from calculations.transformations import Transformations
from laminates.layer import Layer
from forces.stress import Stress
from deformations.deformations import Deformations
from deformations.delta_dimentions import DeltaDimentions


def test_compound():
    fiber_1 = Fiber(name="carbon", elastic_mod=250, poisson_rel=0.4, cutting_mod=8.32)
    matrix_1 = Matrix(
        name="epóxico", elastic_mod=5.8, poisson_rel=0.38, cutting_mod=8.1
    )
    compound_1 = Compound()
    compound_1.by_materials(fiber=fiber_1, vf=0.1, matrix=matrix_1, vm=0.9)
    print(compound_1.mech_props_to_pd())


def test_qlt():
    compound_1 = Compound()
    compound_1.by_elastic_constans(
        e1=164.82, e2=40.25, nu12=0.286, nu21=0.286, g12=8.1, name="vidrio - polimerica"
    )
    compound_1_qlt = compound_1.get_qlt()
    print(Transformations.qlt_to_qxy(qlt=compound_1_qlt, theta=-90))


def test_layer():
    compound_1 = Compound()
    compound_1.by_elastic_constans(
        e1=65.4,
        e2=12.47,
        nu12=0.254,
        nu21=0.254,
        g12=4.8,
        name="vidrio - epoxico",
        fiber_angle=0,
    )
    # d_1 = Transformations.d(theta=0)
    # tp_1 = Transformations.tp(theta=0)
    # compound_1_stl = compound_1.get_stl()
    sxy = compound_1.transform_slt2sxy(theta=0)
    print(sxy)
    stress_1 = Stress(sx=0.095, sy=0, txy=0)
    layer_1 = Layer(
        composite=compound_1, width=40 / 1000, lengh=85 / 1000, thickness=0.5 / 1000
    )
    print(layer_1.get_deformations(stress=stress_1))
    print(layer_1.get_delta_dimentions(stress=stress_1))
    print(layer_1.get_final_dimentions(stress=stress_1))
    print(layer_1.get_delta_dimentions(stress=stress_1, fiber_angle=45))


def test_all_layer():
    compound_1 = Compound()
    compound_1.by_elastic_constans(
        e1=131,
        e2=8.7,
        nu12=0.28,
        nu21=0.02,
        g12=5,
        name="vidrio - peek",
        fiber_angle=0,
        alpha_1=-0.2e-6,
        alpha_2=24e-6,
        beta_1=0,
        beta_2=0.3,
    )
    d_1 = DeltaDimentions(dx=5)
    layer_1 = Layer(
        composite=compound_1, lengh=250 / 1000, width=50 / 1000, thickness=2 / 1000
    )

    print(layer_1.get_deformations_by_delta_dimentions(d_1))


if __name__ == "__main__":
    # test_compound()
    # test_qlt()
    # test_layer()
    test_all_layer()
