

class ElasticConstants:

    def get_by_props(self, vf: float, vm: float, ef: float, em: float, nuf: float, num: float, gf: float, gm: float) -> tuple:
        e1 = self.e1(ef, vf, em, vm),
        e2 = self.e2(ef, vf, em, vm),
        nu12 = self.mu12(nuf, vf, num, vm),
        nu21 = self.mu21(nuf, vf, num, vm),
        g12 = self.g12(gf, vf, gm, vm)

        return (e1, e2, nu12, nu21, g12)

    def e1(self, ef: float, vf: float, em: float, vm: float) -> float:
        return ef*vf + em*vm

    def e2(self, ef: float, vf: float, em: float, vm: float) -> float:
        return 1/((vf/ef)+(vm/em))

    def mu12(self, nuf: float, vf: float, num: float, vm: float) -> float:
        return nuf*vf + num*vm

    def mu21(self, nuf: float, vf: float, num: float, vm: float) -> float:
        return 1/((vf/nuf)+(vm/num))

    def g12(self, gf: float, vf: float, gm: float, vm: float) -> float:
        return 1/((vf/gf)+(vm/gm))
