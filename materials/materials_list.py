from material import Material
from compound import Compound
import pandas as pd


class MaterialsList:
    materials_list: list[Material]

    def __init__(self) -> None:
        self.materials_list = []

    def add_material(self, material: Material) -> None:
        self.materials_list.append(material)

    def modificar_material(self):
        """
        In construction
        """
        pass

    def eliminar_material(self):
        """
        In construction
        """
        pass

    def show_list(self):
        l = []
        for material in self.materials_list:
            l.append(material.convert_to_pd())
        print(pd.concat(l, ignore_index=True))

    def create_compound(
        self,
        id_f: int,
        id_m: int,
        vf: float = None,
        vm: float = None,
        eclt: float = None,
        ectt: float = None,
        clhe: float = None,
        cthe: float = None,
    ) -> Compound:
        mf = self.materials_list[id_f]
        namef = mf.__name
        mm = self.materials_list[id_m]
        namem = mm.__name

        return Compound(
            name=f"{namef} / {namem}",
            fiber=mf,
            matrix=mm,
            vf=vf,
            vm=vm,
            eclt=eclt,
            ectt=ectt,
            clhe=clhe,
            cthe=cthe,
        )
