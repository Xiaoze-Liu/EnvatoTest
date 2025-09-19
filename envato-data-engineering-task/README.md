**Brief**
A Python-based command-line tool for transforming raw Pokemon data into structured formats suitable for APIs, analytics, or database ingetion. Built with *Click* for intuitive CLI usage and designed for modular ETL workflows.
**Core folder structure**
src/envato_data_engineering_task
|--entrypoint.py *the main script to invoke the pipeline by nominated CLI*
|--extract.py *the script for calling Pokemon docs API and landing to data/raw*
|--load.py *read the result of extract.py and upload data to duckdb raw schema*
|--transform.py *read the result of load.py and transform data from raw to pokeapi schema*
|--duckdb_connection.py *this script is returning duckdb connection to be referenced by other functions*
|--duckdb_query.py *a casual script for running duckdb queries to verify data*

**Installation**
I recommend using a virtual environment:
```Python -m venv.venv```
```source .venv/bin/activate```
```cd envato-data-engineering-task```
```pip install -e .```

**Usage**
```bash envato-data-engineering-task --pokemon {id or name}``
Sample:
```envato-data-engineering-task --pokemon 1``` or
```envato-data-engineering-task --pokemon bulbasaur```

**Design decision**
1. I decided to go with data modelling option 2 of multiple normalized tables, the reason is that it's easier for further dimentional star schema modelling, as well as for business teams for any further analysis, considering some of business team would not have advanced sql skills to unnest array/json
2. Currently it's full load pattern which means everything you run the command, all existing json files would be looped again, but it won't be duplicated in duckdb because I designed a de-duplication mechanism for being idempotent.