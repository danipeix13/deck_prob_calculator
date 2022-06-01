import numpy as np
from calculator import *

deck_and_probs = [
    ["P",  9], # Piezas y reactivaciones
    ["H",  3], # Hangar
    ["B",  7], # Brave
    ["HS", 9], # Handtraps
    ["T",  6], # Therion
    ["O",  4], # Brick
    ["TF", 1], # Terraforming
    ["SR", 1], # Set Rotation
]

X = "WHATEVER"
combo_hands = set(
    set(),
    set(),
    set(),
    set(),
    set(),
    set(),
    set(),
    set(),
    set(),

)

deck, probs = [], []
for k,v in deck_and_probs.items():


np.random.choice(deck, 5, probs)
