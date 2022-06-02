from calculator import *

deck_and_probs = [
    ["Brave", 7],
    ["Therions", 6],
    ["ABC", 7],
    ["Hangar", 3],
    ["Terra", 1],
    ["SetRot", 1],
    ["Second", 9],
    ["React", 2],
    [X, 4],
]

combo_hands = {
    0: {"ABC"},
    1: {"Brave"},
    2: {"ABC", "Brave"},
    # 0: {"ABC", "Brave", "Therions"},
    # 1: {"Terra", "Brave", "Therions"},
    # 2: {"ABC", "Brave", "Terra"},
    # 3: {"SetRot", "Brave"},
}

if __name__ == "__main__":
    c = Calculator(deck_and_probs)
    c.calculateProbs(combo_hands, 100000)

