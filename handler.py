import utils
import plot
import data
import visualizer


plot = plot.IndexPlot()
user = visualizer.GithubUser()


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
            return
        else:
            print("Accident")
            cmd, param1 = command.split(" ")
            holder = data.IndexDataHolder(
                         "../finance_data/indexes_us/{id}.csv"
                         .format(id=cmd)
                     )
            series = holder.extract_column(param1)
            plot_url = plot.plot_scatter(series)
            user.update_visualizer(plot_url)
            utils.send_text_message(event.reply_token,
                                    visualizer.ENDPOINT)
