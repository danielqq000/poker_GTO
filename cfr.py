import numpy as np

class CFR:
    def __init__(self, num_actions):
        self.num_actions = num_actions
        self.regrets = np.zeros(num_actions)
        self.strategy = np.zeros(num_actions)

    def get_strategy(self):
        positive_regrets = np.maximum(self.regrets, 0)
        total_regret = np.sum(positive_regrets)
        if total_regret > 0:
            self.strategy = positive_regrets / total_regret
        else:
            self.strategy = np.ones(self.num_actions) / self.num_actions
        return self.strategy

    def update_regrets(self, action, utility):
        self.regrets[action] += utility

