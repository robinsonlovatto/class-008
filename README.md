# ETL - From Json files to csv or Parquet

A project that extracts data from json files, concatenate them, add a calculated column to the Pandas' Dataframe, then save the data to a csv or parquet file or both.

Were used decorators to add logs with Loguru and measure time in each function.


### Installation

1. Clone the repository:
```bash
git clone https://github.com/robinsonlovatto/python_etl_from_json_to_csv_or_parquet.git
cd python_etl_from_json_to_csv_or_parquet

```

2. Configure the right version of Python with `pyenv`:
```bash
pyenv install 3.11.5
pyenv local 3.11.5
```

3. Configure Poetry para Python version 3.11.5 and activate the virtual environment:

```bash
poetry env use 3.11.5
poetry shell
```

4. Install the project dependencies:

```bash
poetry install
```

5. Run the project:
```bash
poetry run python pipeline.py
```  
