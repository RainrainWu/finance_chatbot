import pandas as pd
import numpy as np
import plotly.graph_objects as go

spx_data = pd.read_csv("../finance_data/indexes_us/SPX.csv")
spx_date_array = np.array(["{y}-{m}-{d}".format(y=x.split("/")[2],
                                                m=x.split("/")[0],
                                                d=x.split("/")[1])
                           for x in spx_data.iloc[:, 0:1].to_numpy()[:, 0]])
spx_date_frame = pd.DataFrame(spx_date_array, columns=["Date"])
spx_data_fresh = pd.concat([spx_data.iloc[:, 1:], spx_date_frame], axis=1)
spx_data_fresh = spx_data_fresh.sort_values(by="Date", ascending=True)
spx_close = spx_data_fresh.iloc[:, 0:1].to_numpy()[:, 0]


fig = go.Figure()
fig.add_trace(go.Scatter(y=spx_close))
fig.update_layout(title='Hello Figure')
fig.update_xaxes(showgrid=False, zeroline=False)
fig.update_yaxes(showgrid=False, zeroline=False, range=[1750, 3500])
fig.show()
