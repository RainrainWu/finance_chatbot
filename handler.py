import utils


class MessageHandler():

    def __init__(self, machine):

        self.machine = machine


class HallHandler(MessageHandler):

    def handle(self, event, command):

        if (command == "vol"):
            self.machine.vol()
            utils.send_text_message(event.reply_token,
                                    "Enter volatility service")


class VoladilityHandler(MessageHandler):

    def handle(self, event, command):

        if (command == "hall"):
            self.machine.hall()
            utils.send_text_message(event.reply_token,
                                    "Enter hall")
