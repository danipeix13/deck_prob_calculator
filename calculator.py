from nis import match
import numpy as np

X = "WHATEVER"


class Calculator():
    def __init__(self, deck_and_probs):
        self.deck, self.probs = list(zip(*deck_and_probs))
        
    def calculateProbs(self, combo_hands, num_iters=10):
        matches, cont = [], 0
        for ch in combo_hands.values():
            matches.append(0)
            
        for _ in range(num_iters):
            hand = set(np.random.choice(self.deck, 5, True, np.array(self.probs) / np.sum(self.probs)))
            isMatch = False
            for id,ch in combo_hands.items():
                if len(hand.intersection(ch)) == len(ch):
                    isMatch = True
                    matches[id] += 1
            if isMatch:
                cont += 1

        print("TOTAL COMBO HANDS:", cont * 100 / num_iters, "%")
        for id,ch in combo_hands.items():
            print(ch, ":", matches[id] * 100 / num_iters, "%")


    