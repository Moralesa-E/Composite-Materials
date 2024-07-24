import pandas as pd


class Material:
    def __init__(
        self,
        name: str,
        elastic_mod: float,
        poisson_rel: float,
        cutting_mod: float,
        coef_long_thermal_exp: float = 0,
        coef_trans_thermal_exp: float = 0,
        hygro_exp_coef: float = 0,
    ) -> None:
        self.__name = name
        self.__elastic_mod = elastic_mod
        self.__poisson_rel = poisson_rel
        self.__cutting_mod = cutting_mod
        self.__coef_long_thermal_exp = coef_long_thermal_exp
        self.__coef_trans_thermal_exp = coef_trans_thermal_exp
        self.__hygro_exp_coef = hygro_exp_coef

    def convert_to_pd(self) -> pd.DataFrame:
        return pd.DataFrame([self.__dict__])

    def extract_f3(self) -> tuple:
        return (self.__elastic_mod, self.__poisson_rel, self.__cutting_mod)

    def get_name(self):
        return self.__name
