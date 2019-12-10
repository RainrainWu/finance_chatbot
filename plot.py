import os

import plotly.graph_objects as go
import chart_studio.tools as chst_tl
import chart_studio.plotly as chst_pl
from dotenv import load_dotenv

import visualizer

user = visualizer.GithubUser()

load_dotenv()
chst_tl.set_credentials_file(
    username=os.getenv("CHART_STUDIO_USERNAME"),
    api_key=os.getenv("CHART_STUDIO_APIKEY")
)


class IndexPlot():

    def __init__(self):
        pass

    def plot_scatter(self, list):
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=list))
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showgrid=False, zeroline=False,
                         range=[min(list) - 150, max(list) + 150])
        url = chst_pl.plot(fig, filename="temp")
        return url
