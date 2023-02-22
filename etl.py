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
    df.Ones = df.Ones.map(lambda x: np.sin(x))
    df.Twos = df.Twos.map(lambda x: np.cos(x))
    return df

# @task(name='save to lfs')
# def save_data(df: pd.DataFrame) -> None:
#     df.to_csv()

@flow(name='main flow')
def main_flow():
    df = generate_data()
    transormed_df = transform_data(df)
    
if __name__ == "__main__":
    main_flow()
        