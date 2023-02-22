import pandas as pd
from prefect import task, flow

@task(name='generate data')
def create_data() -> pd.DataFrame:
    data = {
        'A': [i for i in range(0, 10, 1)],
        'B': [i for i in range(0, 20, 2)],
        'C': [i for i in range(0, 30, 3)]
    }
    return pd.DataFrame(data)

@task(name='transform')
def transform(df: pd.DataFrame) -> pd.DataFrame:
    df.A = df.A.map(lambda a: a + 1) 
    df.B = df.B.map(lambda b: b + 2)
    df.C = df.C.map(lambda c: c + 3)
    return df

@flow(name='main flow')
def my_flow():
    df = create_data()
    transformed_df = transform(df)
    
if __name__ == "__main__":
    my_flow()