"""
load.py - Loading data from local storage to duckdb
Target table is raw.pokemon_raw
"""

import json
import os
from envato_data_engineering_task.duckdb_connection import db_connection


def load_raw_to_duckdb(db_path=None,file_path=None):
    """
    core function of loading data from local to duckdb raw
    """
    if db_path: #for testing env
        con = db_path
    else:
        con = db_connection()
    con.execute("CREATE SCHEMA IF NOT EXISTS raw")
    con.execute("CREATE TABLE IF NOT EXISTS raw.pokemon_raw (data JSON)")
    if file_path: #for testing env
        data_path = file_path
    else:
        data_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../../data/raw"))
    for file in os.listdir(data_path):
        with open(f"{data_path}/{file}", encoding="utf-8") as f:
            data = json.load(f)
            print("checking duplication(idempotent)...")
            exists = con.execute(
                "select count(*) from raw.pokemon_raw where data['id']=?", [data["id"]]
            ).fetchone()[0]
            if exists:
                print(f"Pokemon id {data['id']} is already existed, skipping it...")
                continue
            print(f"Inserting new pokemon id {data['id']} to duckdb...")
            con.execute("INSERT INTO raw.pokemon_raw VALUES (?)", [json.dumps(data)])


if __name__ == "__main__":
    load_raw_to_duckdb()
