from materials.compound import Compound


class Layer:
    composite: Compound
    angle: float
    thickness: float

    def __init__(self, composite: Compound = None, angle: float = None, thickness: float = float) -> None:
        self.composite = composite
        self.angle = angle
        self.thickness = thickness
