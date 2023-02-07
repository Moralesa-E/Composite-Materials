import pandas as pd

class Material:

    def __init__(self, type: str, name: str, elastic_mod: float, poisson_rel: float, cutting_mod: float, coef_long_thermal_exp: float = 0, coef_trans_thermal_exp: float = 0, hygro_exp_coef: float = 0) -> None:

        self.type = type
        self.name = name
        self.elastic_mod = elastic_mod
        self.poisson_rel = poisson_rel
        self.cutting_mod = cutting_mod
        self.coef_long_thermal_exp = coef_long_thermal_exp
        self.coef_trans_thermal_exp = coef_trans_thermal_exp
        self.hygro_exp_coef = hygro_exp_coef

    def convert_to_dic(self) -> dict:
        dic = {
            "tipo": self.type,
            "name": self.name,
            "mod_material": self.elastic_mod,
            "rel_poisson": self.poisson_rel,
            "mod_corte": self.cutting_mod,
            "coef_long_thermal_exp":self.hygro_exp_coef,
            "coef_trans_thermal_exp":self.coef_trans_thermal_exp,
            "hygro_exp_coef":self.hygro_exp_coef}
        return dic

    def convert_to_pd(self) -> pd.DataFrame:
        dic = self.convert_to_dic()
        return pd.DataFrame([dic])

    def extract_to_compound(self)->tuple:

        return (self.name, self.elastic_mod, self.poisson_rel, self.cutting_mod)
