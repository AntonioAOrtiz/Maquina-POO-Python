from dataclasses import dataclass
from enum import Enum

@dataclass
class Fuerza(Enum):
    Animal=1
    Electrica=2
    Combustible=3