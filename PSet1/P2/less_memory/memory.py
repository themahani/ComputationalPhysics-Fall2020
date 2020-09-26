
class cell:
    """ A cell for the CA problem. """
    def __init__(self, rule, state):
        self.right = None
        self.left = None
        self.rule = rule
        self.state = state

    def situate(self):
        """looks around itself and calculated its situation.
           Returns an int from 0 to 7"""
        return (self.right).state + (self.left).state + self.state

    def choose(self):
        """Looks at its own situation and chooses the next state
           based on the given rule"""
        return self.rule[-1 - self.situate()]
