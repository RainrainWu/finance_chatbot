from transitions import Machine


class InvestMachine(object):

    states = ["hall", "volatility", "strategy"]

    def __init__(self, name):

        self.name = name
        self.kittens_rescued = 0
        self.machine = Machine(model=self,
                               states=InvestMachine.states,
                               initial="hall")

        self.machine.add_transition(trigger="vol",
                                    source="hall",
                                    dest="volatility")

        self.machine.add_transition(trigger="hall",
                                    source="volatility",
                                    dest="hall")

    def on_enter_volatility(self):

        print("\nEnter vol\n")

    def on_enter_hall(self):

        print("\nEnter hall\n")
