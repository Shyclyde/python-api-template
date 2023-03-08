from dataclasses import dataclass

@dataclass
class IcedCoffee:
    title: str
    description: str
    ingredients: list[str]
    image: str
    id: int