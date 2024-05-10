from materials.material import Material


class Fiber(Material):
    type: str

    def __init__(
        self,
        name: str,
        elastic_module: float,
        poisson_relation: float,
        cutting_module: float,
        coef_long_thermal_exp: float = 0,
        coef_trans_thermal_exp: float = 0,
        hygro_exp_coef: float = 0,
    ) -> None:
        self.type = "Fiber"
        super().__init__(
            name,
            elastic_module,
            poisson_relation,
            cutting_module,
            coef_long_thermal_exp,
            coef_trans_thermal_exp,
            hygro_exp_coef,
        )
