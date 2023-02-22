# type: ignore
import pandas as pd
import numpy as np
from prefect import task, flow

@task(name='generate data')
def generate_data() -> pd.DataFrame:
    data  = {
        'Ones': np.linspace(0, 100, 1),
        'Twos': np.linspace(0, 200, 2),
        'Threes': np.linspace(0, 300, 3),
    }
    return pd.DataFrame(data)

@task(name='transform data')
def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    return