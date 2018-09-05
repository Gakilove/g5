import pandas as pd
import numpy as np
import os
from os.path import join as pjoin

baseline = pd.read_csv('./data/CAM-IQ-96.csv', index_col=0)

for f in os.listdir('./data'):
    if f.endswith('.csv') and f != 'CAM-IQ-96.csv':
        path = pjoin('./data', f)
        ipcs = pd.read_csv(path, index_col=0)
        print(f)
        try:
            result = ipcs.values / baseline.values
            print(result)
            print(result.mean())
        except Exception as e:
            pass
