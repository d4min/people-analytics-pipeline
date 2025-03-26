import os 
import pandas as pd
import psycopg2
from sqlalchemy import create_engine 
from dotenv import load_dotenv 

load_dotenv()

def get_db_connection():
    """
    Function to get postgresql database connection
    """
    conn = psycopg2.connect(
        dbname = os.getenv('DB_NAME'),
        user = os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )

    return conn 

def get_sqlalchemy_engine():
    """
    Function to get SQLAlchemy engine

    This engine is used for database operations like executing queries and managing connections
    """
    connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '5432')}/{os.getenv('DB_NAME', 'people_analytics')}"
    engine = create_engine(connection_string)

    return engine 

def load_from_excel():
    """
    Load all datasets from the Excel file
    """
    requisitions_df = pd.read_excel('data/Data File.xlsx', sheet_name='Requisition')
    candidate_df = pd.read_excel('data/Data File.xlsx', sheet_name='Candidate')
    candidate_status_df = pd.read_excel('data/Data File.xlsx', sheet_name='Candidate Status')
    department_df = pd.read_excel('data/Data File.xlsx', sheet_name='Department')

    return {
        'requisitions': requisitions_df,
        'candidate': candidate_df,
        'candidate_status': candidate_status_df,
        'department': department_df
    }

def load_from_db():
    """Load all datasets from database"""
    engine = get_sqlalchemy_engine()
    
    requisitions_df = pd.read_sql("SELECT * FROM raw_requisitions", engine)
    candidate_df = pd.read_sql("SELECT * FROM raw_candidate", engine)
    candidate_status_df = pd.read_sql("SELECT * FROM raw_candidate_status", engine)
    department_df = pd.read_sql("SELECT * FROM raw_department", engine)
    
    return {
        'requisitions': requisitions_df,
        'candidate': candidate_df,
        'candidate_status': candidate_status_df,
        'department': department_df
    }

# Test the connection 
if __name__ == "__main__":
    try:
        conn = get_db_connection()
        print("postgresql connection successful")
        conn.close()

        engine = get_sqlalchemy_engine()
        print("sqlalchemy engine created")
    except Exception as e:
        print(f"Connection error: {e}")