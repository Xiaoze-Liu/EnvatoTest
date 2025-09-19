"""
transform.py - Transforming and standardizing data from duckdb schema raw to pokeapi
Target tables are
1. pokeapi.pokemon
2. pokeapi.types
3. pokeapi.abilities
"""

import json
from envato_data_engineering_task.duckdb_connection import db_connection


def data_normalization(db_path=None):
    """
    Core function of normalizing data from raw to pokeapi
    """
    if db_path: #for unit testing
        con = db_path
    else:
        con = db_connection()
    con.execute("""create schema if not exists pokeapi""")
    con.execute(
        """create table if not exists pokeapi.pokemon
        (id integer,name text,height integer, weight integer, base_experience integer)"""
    )
    con.execute(
        """create table if not exists pokeapi.types(pokemon_id integer, slot integer, type text)"""
    )
    con.execute(
        """create table if not exists pokeapi.abilities 
        (pokemon_id integer, slot integer, ability text, is_hidden boolean)"""
    )
    raw_data = con.execute("select data from raw.pokemon_raw").fetchall()
    for entry in raw_data:
        data = json.loads(entry[0])
        print("Checking duplication(idempotent) for pokeapi.pokemon...")
        exists = con.execute(
            "select count(*) from pokeapi.pokemon where id = ?", [data["id"]]
        ).fetchone()[0]
        if exists:
            print(
                f"Pokemon id {data['id']} is already existed\n"
                f"in table pokeapi.pokemon, skip loading..."
            )
        else:
            con.execute(
                "insert into pokeapi.pokemon values (?,?,?,?,?)",
                [
                    data["id"],
                    data["name"],
                    data["height"],
                    data["weight"],
                    data["base_experience"],
                ],
            )
        for type_ in data["types"]:
            print("Checking duplication(Idempotent) for pokeapi.types")
            exists_type = con.execute(
                "select count(*) from pokeapi.types where pokemon_id = ? and slot = ?",
                [data["id"], type_["slot"]],
            ).fetchone()[0]
            if exists_type:
                print(
                    f"Pokemon Id {data['id']} and Slot {type_['slot']} is already existed\n"
                    f"in table pokeapi.types, skip loading..."
                )
            else:
                con.execute(
                    "insert into pokeapi.types values (?,?,?)",
                    [data["id"], type_["slot"], type_["type"]["name"]],
                )
        for ability in data["abilities"]:
            print("Checking duplication(Idempotent) for table pokeapi.abilities...")
            exists_ability = con.execute(
                "select count(*) from pokeapi.abilities where pokemon_id = ? and slot = ?",
                [data["id"], ability["slot"]],
            ).fetchone()[0]
            if exists_ability:
                print(
                    f"Pokemon Id {data['id']} and Slot {ability['slot']} is already existed\n"
                    f"in table pokeapi.ability, skip loading... "
                )
            else:
                con.execute(
                    "insert into pokeapi.abilities values (?,?,?,?)",
                    [
                        data["id"],
                        ability["slot"],
                        ability["ability"]["name"],
                        ability["is_hidden"],
                    ],
                )


if __name__ == "__main__":
    data_normalization()
