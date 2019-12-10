import utils
import news
import plot
import visualizer

news = news.News()
plot = plot.IndexPlot()
user = visualizer.GithubUser()


class MessageHandler():

    def __init__(self, machine):

        self.machine = machine


class HallHandler(MessageHandler):

    def handle(self, event, command):

        params = command.split(" ")

        if (len(params) == 1):
            if (params[0] == "vol"):
                self.machine.vol()
                utils.send_text_message(event.reply_token,
                                        "Enter volatility service")

            if (params[0] == "news"):
                self.machine.news()
                utils.send_text_message(event.reply_token,
                                        "Enter bulletin board")


class NewsHandler(MessageHandler):

    def handle(self, event, command):

        params = command.split(" ")

        if (len(params) == 1):
            if (params[0] == "hall"):
                self.machine.hall()
                utils.send_text_message(event.reply_token,
                                        "Enter hall")
                return

        if (len(params) == 2):
            if (params[0] == "cnyes"):
                urls = news.cnyes(int(params[1]))
                utils.send_text_message(event.reply_token,
                                        "\n\n".join(urls))


class VoladilityHandler(MessageHandler):

    def handle(self, event, command):

        params = command.split(" ")

        if (len(params) == 1):
            if (params[0] == "hall"):
                self.machine.hall()
                utils.send_text_message(event.reply_token,
                                        "Enter hall")
                return

        if (len(params) == 2):

            # parse period
            time = {"y": 261, "q": 65, "m": 22, "d": 1}
            period = int(params[1][:-1]) * time[params[1][-1]]

            # update plot
            plot_url = plot.plot_k(params[0], period)
            user.update_visualizer(plot_url)
            utils.send_text_message(event.reply_token,
                                    visualizer.ENDPOINT)
