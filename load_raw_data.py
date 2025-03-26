import os
import pandas as pd 
from sqlalchemy import create_engine
from dotenv import load_dotenv 

load_dotenv()

def load_excel_to_postgres():
    """
    Loads raw data into the postgres database

    This is so we can use sql for data cleaning and quality checks
    """

    # Create SqlAlchemy engine
    connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '5432')}/{os.getenv('DB_NAME', 'people_analytics')}"
    engine = create_engine(connection_string)

    # Load excel files into dataframes
    requisitions_df = pd.read_excel('data/Data File.xlsx', sheet_name='Requisition')
    candidate_df = pd.read_excel('data/Data File.xlsx', sheet_name='Candidate')
    candidate_status_df = pd.read_excel('data/Data File.xlsx', sheet_name='Candidate Status')
    department_df = pd.read_excel('data/Data File.xlsx', sheet_name='Department')

    # Write dataframes to postgreql database
    requisitions_df.to_sql('raw_requisitions', engine, if_exists='replace', index=False)
    candidate_df.to_sql('raw_candidate', engine, if_exists='replace', index=False)
    candidate_status_df.to_sql('raw_candidate_status', engine, if_exists='replace', index=False)
    department_df.to_sql('raw_department', engine, if_exists='replace', index=False)
    
    print("Data loaded successfully into PostgreSQL!")

if __name__ == '__main__':
    load_excel_to_postgres()

    