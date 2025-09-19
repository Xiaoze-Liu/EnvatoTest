"""
duckdb_connection.py - build a common function for all py file to 
establish connection to duckdb
"""
import os
import duckdb

def db_connection():
    """
    Core function to establish connection to duckdb
    """
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../../../data/envato.db"))
    con = duckdb.connect(db_path)
    return con
