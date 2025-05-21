from dataclasses import dataclass
from datetime import datetime


@dataclass
class Rotta:
    DESTINATION_AIRPORT_ID: int
    ORIGIN_AIRPORT_ID: int
    num_voli: int
    somma_distanze: int

    def __post_init__(self):
        self.media = 0
