import numpy as np

X = "WHATEVER"


class Calculator():
    def __init__(self, deck_and_probs):
        self.deck, self.probs = list(zip(*deck_and_probs))
        
    def calculateProbs(self, combo_hands, num_iters=10):
        dic = { "A": 0, "B": 0, "C": 0, "D": 0, "E": 0 }
        cont = 0
        for i in range(num_iters):
            hand = set(np.random.choice(self.deck, 5, True, np.array(self.probs) / np.sum(self.probs)))
            for ch in combo_hands:
                if len(hand.intersection(ch)) == len(ch):
                    cont += 1
                    break
        print(cont * 100 / num_iters, "%", dic)


    