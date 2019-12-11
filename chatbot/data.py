import pandas as pd
import numpy as np


class DataHolder():

    def __init__(self, dir):

        # load raw data from csv and rename column
        self.raw_data = pd.read_csv(dir)
        self.raw_data.rename(columns={" Close/Last": "close",
                                      " Volume": "volumn",
                                      " Open": "open",
                                      " High": "high",
                                      " Low": "low"},
                             inplace=True)

        # refactor date column
        raw_date = self.raw_data.iloc[:, 0:1].to_numpy()[:, 0]
        date_series = np.array(["{y}-{m}-{d}".format(y=x.split("/")[2],
                                                     m=x.split("/")[0],
                                                     d=x.split("/")[1])
                                for x in raw_date])
        date_frame = pd.DataFrame(date_series, columns=["date"])
        data_frame = pd.concat([date_frame, self.raw_data.iloc[:, 1:]],
                               axis=1)

        # sort by date
        self.sort_frame = data_frame.sort_values(by="date",
                                                 ascending=True)

    # get whole dataframe
    def get_frame(self):
        self.sort_frame


class IndexDataHolder(DataHolder):
    data_type = "index"

    # extract specified column
    def extract_column(self, col):
        index = self.sort_frame.columns.tolist().index(col)
        series = self.sort_frame.iloc[:, index:index + 1].to_numpy()[:, 0]
        return series


class StockDataHolder(DataHolder):
    data_type = "stock"

    # extract specified column
    def extract_column(self, col):

        index = self.sort_frame.columns.tolist().index(col)
        series = self.sort_frame.iloc[:, index:index + 1].to_numpy()[:, 0]
        if (series[0][0] not in "0123456789"):
            series = [float(x[2:]) for x in series]
        return series
