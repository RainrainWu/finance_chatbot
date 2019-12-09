from transitions import Machine

import utils

class InvestMachine(object):

    states = ["home", "volatility", "strategy"]

    def __init__(self, name):

        self.name = name
        self.kittens_rescued = 0
        self.machine = Machine(model=self,
                               states=InvestMachine.states,
                               initial="home")

        self.machine.add_transition(trigger="vol",
                                    source="home",
                                    dest="volatility")

        self.machine.add_transition(trigger="home",
                                    source="volatility",
                                    dest="home")

    def on_enter_volatility(self):

        print("\nEnter vol\n")

    def on_enter_home(self):

        print("\nEnter home\n")