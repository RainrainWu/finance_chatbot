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

    help_message = (
        "Welcome to the hall, "
        "here are some command you can use:\n"
        "\n"
        "help\n"
        "pop up the help message\n"
        "\n"
        "news\n"
        "Go to bulletin board for breaking news\n"
        "\n"
        "vol\n"
        "Plot the finance voladility"
    )

    def handle(self, event, command):

        params = command.split(" ")

        if (len(params) == 1):

            if (params[0] == "help"):
                utils.send_text_message(event.reply_token,
                                        HallHandler.help_message)

            elif (params[0] == "vol"):
                self.machine.vol()
                utils.send_text_message(event.reply_token,
                                        VoladilityHandler.help_message)

            elif (params[0] == "news"):
                self.machine.news()
                utils.send_text_message(event.reply_token,
                                        NewsHandler.help_message)


class NewsHandler(MessageHandler):

    help_message = (
        "Welcome to the bulletin board, "
        "here are some command you can use:\n"
        "\n"
        "help\n"
        "pop up the help message\n"
        "\n"
        "hall:\n"
        "Back to the hall\n"
        "\n"
        "cnyes <number>\n"
        "Scrape some news from cnyes\n"
        "number:\n"
        "Number of news to scrape"
    )

    def handle(self, event, command):

        params = command.split(" ")

        if (len(params) == 1):
            if (params[0] == "help"):
                utils.send_text_message(event.reply_token,
                                        NewsHandler.help_message)

            elif (params[0] == "hall"):
                self.machine.hall()
                utils.send_text_message(event.reply_token,
                                        HallHandler.help_message)

        if (len(params) == 2):
            if (params[0] == "cnyes"):
                urls = news.cnyes(int(params[1]))
                utils.send_text_message(event.reply_token,
                                        "\n\n".join(urls))


class VoladilityHandler(MessageHandler):

    help_message = (
        "Welcome to the bulletin board, "
        "here are some command you can use:\n"
        "\n"
        "help\n"
        "pop up the help message\n"
        "\n"
        "hall\n"
        "Back to the hall\n"
        "\n"
        "<group> <index> <period>\n"
        "Plot the latest voladility\n"
        "group:\n"
        "should be us_indexes or us_stocks\n"
        "index:\n"
        "spx, ndx, nya, ixic, rut for us_indexes\n"
        "aapl, amzn, nflx, tsla, msft for us_stocks\n"
        "period:\n"
        "use y for year, q for season, m for month, d for day, "
        "like 3y, 2q, 3m...etc, we only have 5 years data now"
    )

    def handle(self, event, command):

        params = command.split(" ")

        if (len(params) == 1):
            if (params[0] == "help"):
                utils.send_text_message(event.reply_token,
                                        VoladilityHandler.help_message)
            if (params[0] == "hall"):
                self.machine.hall()
                utils.send_text_message(event.reply_token,
                                        HallHandler.help_message)
                return

        if (len(params) == 3):

            # parse period
            time = {"y": 261, "q": 65, "m": 22, "d": 1}
            period = int(params[-1][:-1]) * time[params[-1][-1]]

            # update plot
            plot_url = plot.plot_k(params[0], params[1], period)
            # user.update_visualizer(plot_url)
            utils.send_text_message(event.reply_token,
                                    plot_url)
