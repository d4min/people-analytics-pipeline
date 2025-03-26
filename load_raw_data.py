import os
import pandas as pd 
from sqlalchemy import create_engine
from dotenv import load_dotenv 

from db_connector import get_sqlalchemy_engine, load_from_excel

load_dotenv()

def load_excel_to_postgres():
    """
    Loads raw data into the postgres database

    This is so we can use sql for data cleaning and quality checks
    """

    engine = get_sqlalchemy_engine()

    # Load excel files into dataframes
    data_dict = load_from_excel()

    # Write dataframes to postgreql database
    data_dict['requisitions'].to_sql('raw_requisitions', engine, if_exists='replace', index=False)
    data_dict['candidate'].to_sql('raw_candidate', engine, if_exists='replace', index=False)
    data_dict['candidate_status'].to_sql('raw_candidate_status', engine, if_exists='replace', index=False)
    data_dict['department'].to_sql('raw_department', engine, if_exists='replace', index=False)
    
    print("Data loaded successfully into PostgreSQL!")

if __name__ == '__main__':
    load_excel_to_postgres()

