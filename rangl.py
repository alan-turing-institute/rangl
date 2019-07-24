import logging
import random
import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

STREAMS = "data.csv"
COUNT = 1000

random.seed(1)


class Environment:
    def __init__(self):

        # constants
        self.DATA = None  # demand series
        self.THRESHOLD = None  # terminal demand

        self.TIME = None  # time series
        self.TERMINAL = None  # terminal time

        # variables
        self.stream = None
        self.spill = None

        self._load()

    def _load(self):

        df = pd.read_csv(STREAMS)
        df["A.targetTime"] = pd.to_datetime(df["A.targetTime"])

        time = df["A.targetTime"]
        time_delta = (time - time.iloc[0]) / pd.Timedelta(hours=1)

        self.TIME = time_delta.to_numpy()
        self.TERMINAL = self.TIME[-1].item()

        # consider power node A only
        keep = df.columns.str.contains(r"A.\d")
        data_ = df.loc[:, keep]
        data_.columns = np.arange(len(data_.columns))
        self.DATA = data_

        self.THRESHOLD = self.DATA.iloc[-1].mean().item()

    def render(self):
        index = random.randint(0, COUNT)
        self.stream = self.DATA[index].to_list()
        self.spill = self.stream[-1] > self.THRESHOLD

    def score(self, policy):

        t_pred, spill_pred = policy.apply(
            t_array=self.TIME, X_array=self.stream, env=self
        )
        logger.debug(f"Prediction: t_pred: {t_pred}, spill_pred:  {spill_pred}")

        I = int(spill_pred == self.spill)
        logger.debug(f"Output: spill: {self.spill}, I: {I}")

        alpha = 0.25
        _score = (self.TERMINAL - t_pred) * I - alpha * self.TERMINAL * (1 - I)
        logger.debug(f"score: {_score}")
        return _score


class Policy:
    def __init__(self, rule):
        self.rule = rule

    def apply(self, t_array, X_array, env):
        t_pred, spill_pred = self.rule(t_array, X_array, env)
        return t_pred, spill_pred

