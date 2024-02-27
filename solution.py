class Node:
    def __init__(self, action, cost, parent=None):
        self.parent = parent
        self.action = action #Action performed on the parent to reach the current state/node
        if parent:
            cost = parent.cost + 1
        else:
            cost = 0


