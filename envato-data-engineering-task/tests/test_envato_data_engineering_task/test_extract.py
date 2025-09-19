import os,json,sys
from pathlib import Path
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),"../../src")))
from envato_data_engineering_task.extract import extract_pkm
def test_extract_creates_json(tmp_path):
    data_path=Path(os.path.abspath(os.path.join(os.path.dirname(__file__),"../../data/raw")))
    extract_pkm(1)
    files = list(data_path.glob('*.json'))
    assert len(files) == 1
    with open(files[0]) as f:
        data = json.load(f)
        assert data['name'] == 'bulbasaur'