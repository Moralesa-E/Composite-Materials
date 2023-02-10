from layer import Layer


class CompositeByLayers:

    __composites: list[Layer]

    def add(self, lyr: Layer) -> None:
        self.__composites.append(lyr)
