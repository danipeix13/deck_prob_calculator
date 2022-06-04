from calculator import *

DECK = [
    [15, "Starter"],
    [12, "Extender"],
    [8, "Handtrap"],
    [5, "BRICK"],
]

COMBO_HANDS = [
    ["Starter", "Starter"],
    ["Starter", "Handtrap"],
    ["Starter", "Extender", "Extender"],
    ["Extender", "Extender", "Handtrap"],
    ["BRICK", "BRICK"],
]

HAND_SIZE = 5

if __name__ == "__main__":
    c = Calculator(DECK, HAND_SIZE, COMBO_HANDS)
    c.calculateProbs()
    c.printResults()
    c.plotResults()
