import os

import plotly.graph_objects as go
import chart_studio.tools as chst_tl
import chart_studio.plotly as chst_pl
from dotenv import load_dotenv

import visualizer
import data

user = visualizer.GithubUser()

load_dotenv()
chst_tl.set_credentials_file(
    username=os.getenv("CHART_STUDIO_USERNAME"),
    api_key=os.getenv("CHART_STUDIO_APIKEY")
)


class IndexPlot():

    def __init__(self):
        pass

    def plot_k(self, index, period):

        # extracy data
        holder = data.IndexDataHolder(
                         "../finance_data/indexes_us/{id}.csv"
                         .format(id=index)
                     )
        date = holder.extract_column("date")[-period:]
        open = holder.extract_column("open")[-period:]
        high = holder.extract_column("high")[-period:]
        low = holder.extract_column("low")[-period:]
        close = holder.extract_column("close")[-period:]

        # plot figure
        fig = go.Figure(data=[go.Candlestick(x=date,
                                             open=open,
                                             high=high,
                                             low=low,
                                             close=close)])
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showgrid=False, zeroline=False,
                         range=[min(low) - 150, max(high) + 150])
        url = chst_pl.plot(fig, filename="temp")
        return url
