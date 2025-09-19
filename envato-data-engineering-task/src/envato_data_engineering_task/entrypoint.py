"""
entrypoint.py - This is the main function of this application
It supports to use bash command line "envato-data-engineering-task --pokemon {id or name}"
to invoke functions of API call, landing, and transforming
"""
import click
from envato_data_engineering_task.extract import extract_pkm
from envato_data_engineering_task.load import load_raw_to_duckdb
from envato_data_engineering_task.transform import data_normalization


@click.command()
@click.option("--pokemon", required=False, help="Pokemon ID or name")
def main(pokemon):
    """
    Core function to invoke extract.py, load.py, and transform.py in order
    """
    if not pokemon:
        print("Hello from Envato's data engineering take home task!")
        return
    extract_pkm(pokemon)
    load_raw_to_duckdb()
    data_normalization()
    print(f"ETL process is completed for Pokemon Id: {pokemon}")


if __name__ == "__main__":
    main("bulbasuar")
