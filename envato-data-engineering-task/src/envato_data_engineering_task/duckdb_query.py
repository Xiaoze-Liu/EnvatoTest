import duckdb
import os
import json

def query():
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../../data/envato.db"))
    con = duckdb.connect(db_path)
    # data=con.execute("select count(*) from raw.pokemon_raw").fetchall()
    # print (data)
    # data=con.execute("describe raw.pokemon_raw").fetchall()
    # print (data)
    # data=con.execute("select data['name'] from raw.pokemon_raw where data['id'] = 1").fetchall()
    # print (data)
    # con.execute("delete from raw.pokemon_raw")
    # data=con.execute("select data['types'] from raw.pokemon_raw").fetchall()
    # print (data)
    # data=con.execute("select data['abilities'] from raw.pokemon_raw").fetchall()
    # print(data)
    con.execute("delete from raw.pokemon_raw")
    con.execute("delete from pokeapi.pokemon")
    con.execute("delete from pokeapi.types")
    con.execute("delete from pokeapi.abilities")
    data = con.execute("select * from raw.pokemon_raw").fetchall()
    print(data)
    data = con.execute("select * from pokeapi.pokemon").fetchall()
    print(data)
    data = con.execute("select * from pokeapi.types").fetchall()
    print(data)
    data = con.execute("select * from pokeapi.abilities").fetchall()
    print(data)


if __name__ == "__main__":
    query()
