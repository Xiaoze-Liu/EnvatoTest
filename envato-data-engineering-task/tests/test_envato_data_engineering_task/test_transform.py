import duckdb,os,sys,shutil,json
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),"../../src")))
from envato_data_engineering_task.transform import data_normalization

def test_transform_creates_normalization_tables(tmp_path):
    db_path = tmp_path / "data"
    db_file = tmp_path / "data" / "envato.db"
    db_path.mkdir(parents=True)
    os.chdir(tmp_path)
    shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__),"../../data/envato.db")),db_file)
    con = duckdb.connect(str(db_file))
    con.execute("create schema if not exists raw")
    con.execute("""create table if not exists raw.pokemon_raw (data JSON)""")#(id integer,name text, weight integer,height integer,base_experience integer)""")
    sample = {"base_experience": 64,
             "height": 69,
             "id": 1,
             "name": "bulbasaur",
             "weight": 7,
             "types":'',
             "abilities":''}
    con.execute("""insert into raw.pokemon_raw values (?) """, [json.dumps(sample)])
    data_normalization(con)
    result = con.execute("select * from pokeapi.pokemon").fetchall()
    assert result == [(1,'bulbasaur',69,7,64)]
