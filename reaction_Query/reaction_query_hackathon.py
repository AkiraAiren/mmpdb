from __future__ import print_function
import pandas as pd
import sqlalchemy
from rdkit import Chem

def create_engine(path_to_db = './testSQLite.db'):
    return sqlalchemy.create_engine('sqlite:////{}'.format(path_to_db))

def read_molecules_to_pandas(engine, sqlstring):
    return pd.read_sql(sqlstring, engine)

def smarts_matching(smarts):
    pass

def parse_reaction():
    pass


def main():
    query = """
    SELECT * 
    FROM pair
    LIMIT 5
    """

    molecules = read_molecules_to_pandas(create_engine(), query)



if __name__ == 'main':
    main()