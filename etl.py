import pandas as pd
import os
import glob


def extract_data(path: str) -> pd.DataFrame:
    # list all the json files in the folder 'data'
    json_files = glob.glob(os.path.join(path, '*.json'))

    # create a list of dataframes
    df_list = [pd.read_json(file) for file in json_files]

    # concating all dataframes
    df_total = pd.concat(df_list, ignore_index=True)

    return df_total

def calculate_kpi_total_sales(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantity"] * df["Price"]
    return df

def load_data(df: pd.DataFrame, output_format: list):
    for format in output_format:
        if format == "csv":
            df.to_csv("data.csv")
        if format == "parquet":
            df.to_parquet("data.parquet")

def pipeline_calculate_kpi_total_sales_consolidated(path: str, output_format: list):
    data_frame = extract_data(path=path)
    calculated_data_frame = calculate_kpi_total_sales(data_frame)
    load_data(calculated_data_frame, output_format)

