import pandas as pd

class Log:
    def __init__(self, no, time, source, protocol, length, info):
        self.No = no
        self.Time = time
        self.Source = source
        self.Protocol = protocol
        self.Length = length
        self.Info = info


def getData():
    df = pd.read_excel('data/Data.xlsx')

    logs = []

    for i, row in df.iterrows():
        logs.append(
                    Log(
                        row['No.'], 
                        row['Time'],
                        row['Source'],
                        row['Protocol'],
                        row['Length'],
                        row['Info']))
    return logs
