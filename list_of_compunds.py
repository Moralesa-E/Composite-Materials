from compound import Compound
import pandas as pd

class ListofCompounds:

    list_of_compounds: list[Compound]

    def __init__(self) -> None:
        self.list_of_compounds = []

    def add(self, compound: Compound) -> None:
        self.list_of_compounds.append(compound)

    def get(self, id: int) -> Compound:
        return self.list_of_compounds[id-1]

    def show_list(self) -> None:
        """
        In construction
        """
        ls = []
        for comp in self.list_of_compounds:
            ls.append(comp.mech_props_to_pd())

        print(pd.concat(ls, ignore_index=True))

