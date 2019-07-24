import numpy as np
import pandas as pd
import random

STREAMS = "data.csv"
COUNT = 1000

random.seed(1)


class Environment:
    def __init__(self):
        self.data = None
        self.stream = None
        self.threshold = None
        self._load()

    def _load(self):

        df = pd.read_csv(STREAMS)
        df["A.targetTime"] = pd.to_datetime(df["A.targetTime"])
        time = df["A.targetTime"]
        keep = df.columns.str.contains(r"A.\d")

        data_ = df.loc[:, keep]
        data_.columns = np.arange(len(data_.columns))
        self.data = data_

        self.threshold = self.data.iloc[-1].mean().item()

    def render(self):
        index = random.randint(0, COUNT)
        self.stream = self.data[index].to_list()
