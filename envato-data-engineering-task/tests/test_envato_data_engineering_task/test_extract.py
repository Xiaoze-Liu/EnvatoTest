import os,json,sys
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),"../../src")))
from envato_data_engineering_task.extract import extract_pkm
def test_extract_creates_json(tmp_path):
    raw_dir = tmp_path / "data" / "raw"
    raw_dir.mkdir(parents=True)
    os.chdir(tmp_path)
    extract_pkm('bulbasaur')
    files = list(raw_dir.glob('*.json'))
    assert len(files) == 1
    with open(files[0]) as f:
        data = json.load(f)
        assert data['name'] == 'bulbasaur'