from calculator import Calculator

deck_and_probs = [
    ["A", 1], 
    ["B", 4],  
]

combo_hands = [
    {"A"},
]

if __name__ == "__main__":
    print(type(deck_and_probs), type(combo_hands))
    c = Calculator(deck_and_probs)
    c.calculateProbs(combo_hands, 100000)

