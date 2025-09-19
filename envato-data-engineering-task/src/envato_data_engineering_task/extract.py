"""
extract.py - calling Pokemon doc API by Pokemon id or name
landing raw json to envato-data-engineering-task/data/raw
"""

import json
import os
import requests


def extract_pkm(pkm_id):
    """
    calling API and landing raw data
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{pkm_id}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../../../data/raw"))
    with open(f"{data_path}/pokemon_{data['id']}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return data


if __name__ == "__main__":
    PKM_ID_TEST = "1"
    data_local_test = extract_pkm(PKM_ID_TEST)
    print("finish------------------")
