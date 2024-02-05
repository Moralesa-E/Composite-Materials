class ElasticConstants:
    @classmethod
    def get_by_props(
        cls,
        vf: float,
        vm: float,
        ef: float,
        em: float,
        nuf: float,
        num: float,
        gf: float,
        gm: float,
    ) -> tuple:
        e1 = cls.e1(ef, vf, em, vm)
        e2 = cls.e2(ef, vf, em, vm)
        nu12 = cls.mu12(nuf, vf, num, vm)
        nu21 = cls.mu21(nuf, vf, num, vm)
        g12 = cls.g12(gf, vf, gm, vm)

        return (e1, e2, nu12, nu21, g12)

    @classmethod
    def e1(cls, ef: float, vf: float, em: float, vm: float) -> float:
        return ef * vf + em * vm

    @classmethod
    def e2(cls, ef: float, vf: float, em: float, vm: float) -> float:
        return 1 / ((vf / ef) + (vm / em))

    @classmethod
    def mu12(cls, nuf: float, vf: float, num: float, vm: float) -> float:
        return nuf * vf + num * vm

    @classmethod
    def mu21(cls, nuf: float, vf: float, num: float, vm: float) -> float:
        return 1 / ((vf / nuf) + (vm / num))

    @classmethod
    def g12(cls, gf: float, vf: float, gm: float, vm: float) -> float:
        return 1 / ((vf / gf) + (vm / gm))
