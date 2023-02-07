from elastic_constants import ElasticConstants
import pandas as pd

class Compound:

    name: str
    ef: float
    em: float
    nuf: float
    num: float
    gf: float
    gm: float
    vf: float
    vm: float 
    e1: float
    e2: float
    nu12: float
    nu21: float
    g12: float

    def __init__(self, name: str, ef: float, em: float, nuf: float, num: float, gf: float, gm: float) -> None:
        self.name = name
        self.ef = ef
        self.em = em
        self.nuf = nuf
        self.num = num
        self.gf = gf
        self.gm = gm
        self.vf = None
        self.vm = None

    def add_elast_const(self, vf: float, vm: float) -> None:
        print(self.ef)
        self.vf = vf
        self.vm = vm
        elas_const = ElasticConstants()
        e1, e2, nu12, nu21, g12 = elas_const.get_by_props(vf=vf, vm=vm, ef=self.ef, em=self.em, nuf=self.nuf, num=self.num, gf=self.gf, gm=self.gm)

        
        self.e1 = e1
        self.e2 = e2
        self.nu12 = nu12
        self.nu21 = nu21
        self.g12 = g12

    def get_mech_props(self):
        return (self.name, self.e1, self.e2,self.nu12,self.nu21,self.g12)

    def mech_props_to_pd(self)->pd.DataFrame:

        dic = {
            "name": self.name,
            "e1":self.e1,
            "e2":self.e2,
            "nu12":self.nu12,
            "nu21":self.nu21,
            "g12":self.g12
        }
        return pd.DataFrame([dic])
