class Combination:
    def __init__(self, pAntXTree, pAnts, pQuantAnts, pQuantLeaf):
        self.probability = 1
        self.antXTree = pAntXTree
        self.ants = pAnts
        self.order = []
        self.quantAnts = pQuantAnts
        self.quantLeaf = pQuantLeaf

    def __repr__(self):
        return '{}: Probability:{} Ants for Tree: {} Order:{} Max Ants: {} Leaf:{}'.format(self.__class__.__name__,
                                                                                           self.probability,
                                                                                           self.antXTree,
                                                                                           self.order,
                                                                                           self.quantAnts,
                                                                                           self.quantLeaf)
