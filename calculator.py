from itertools import combinations
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

X = "WHATEVER"


class Calculator():
    def __init__(self, probs_and_cards, hand_size, combo_hands):
        self.hand_size = hand_size

        self.possible_hands = self.__allHands(probs_and_cards)
        #print("HANDS:", len(self.possible_hands), "\n", self.possible_hands)

        self.combo_hands = self.__addComboHands(combo_hands)
        self.combo_hands_list = combo_hands 
        #print("COMBO HANDS", len(self.combo_hands), "\n", self.combo_hands)

        self.results = {}

    def calculateProbs(self):
        self.matches = np.zeros(len(self.combo_hands))
        self.combo = 0
        for h in self.possible_hands:
            match = False
            for i in range(len(self.combo_hands)):
                if self.__match(h, self.combo_hands[i]):
                    self.matches[i] += 1
                    match = True
            if match:
                self.combo += 1
        # print(self.matches, self.combo)
        self.results = {
            "TOTAL_COMBO": self.__format(self.combo * 100 / len(self.possible_hands)),
            "HAND_VALUES": list(self.matches * 100 / len(self.possible_hands)),
            "HAND_NAMES" : self.combo_hands_list,
            "N_VALUES"   : np.arange(len(self.matches)),
        }

    
        self.results = {
            "TOTAL_COMBO": self.__format(self.combo * 100 / len(self.possible_hands)),
            "HAND_VALUES": [x for x in list(self.matches * 100 / len(self.possible_hands))],
            "HAND_NAMES" : self.combo_hands_list,
            "N_VALUES"   : np.arange(len(self.matches)),
        }
 
    def printResults(self):
        print("COMBO HANDS: {}%".format(self.results["TOTAL_COMBO"]))
        for name,value in list(zip(self.results["HAND_NAMES"], self.results["HAND_VALUES"])):
            print("{}: {}%".format(name, self.__format(value)))

    def plotResults(self):
        print(self.results["N_VALUES"])
        for x,y in list(zip(self.results["N_VALUES"], self.results["HAND_VALUES"])):
            plt.annotate(str(self.__format(y)), (x,y))
        plt.xticks(self.results["N_VALUES"], self.results["HAND_NAMES"])
        plt.yticks(np.arange(0, 101, 5))
        plt.title("COMBO HANDS: {}%".format(self.results["TOTAL_COMBO"]))
        plt.plot(self.results["N_VALUES"], self.results["HAND_VALUES"], "bo")
        plt.bar(self.results["N_VALUES"], self.results["HAND_VALUES"])
        plt.show()

    ###############################################################################
    def __format(self, data):
        f = "{:.2f}"
        return f.format(data)
        
    def __allHands(self, probs_and_cards):
        deck = []
        for p_c in probs_and_cards:
            deck += [p_c[1] for _ in range(p_c[0])]
        deck = list(combinations(deck, self.hand_size))
        return [Counter(d) for d in deck]

    def __addComboHands(self, combo_hands):
        return [Counter(ch) for ch in combo_hands]

    def __match(self, h1, h2):
        return sum(h1.values()) >= sum(h2.values()) and h1 & h2 == h2
            
    