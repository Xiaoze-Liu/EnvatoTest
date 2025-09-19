import duckdb
import json,os,sys,shutil
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),"../../src")))
from envato_data_engineering_task.load import load_raw_to_duckdb

def test_load_inserts_to_duckdb(tmp_path):
    raw_dir = tmp_path / "data" / "raw"
    raw_dir.mkdir(parents=True)
    db_path = tmp_path / "data" / "envato.db"
    shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__),"../../data/envato.db")),db_path)
    os.chdir(tmp_path)
    #mock a json file
    sample = {"base_experience":64,
              "height":7,
              "id":1,
              "name":"bulbasaur",
              "weight":69}
    with open(raw_dir / "pokemon_1.json", "w") as f:
        json.dump(sample,f)
    con = duckdb.connect(str(db_path))
    load_raw_to_duckdb(con,raw_dir)
    result = con.execute("select * from raw.pokemon_raw").fetchall()[0][0]
    json_format=json.loads(result)
    assert str(json_format) == "{'base_experience': 64, 'height': 7, 'id': 1, 'name': 'bulbasaur', 'weight': 69}"
