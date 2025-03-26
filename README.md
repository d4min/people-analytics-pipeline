# People Analytics Project

## Step 1: Enviroment Setup

In this inital step I have set up a basic dev environment for the People Analytics Assignment. 

### Project Structure

Created a minimal project structure:

- `data/` - Directory for Excel data file (included in .gitignore file for confidentiality purposes)
- `notebooks/` - Jupyter notebooks used for data exploration 
- `sql/` - SQL queries and schema files 


Set up env variables using `.env` file to store database credentials securely

### Core Utilities 

Created `db_connector.py` script with essential functions that will be used repeatedly:

- Database connection utilities using `psycopg2` and `SQLAlchemy`
- Data loading helpers to read from Excel files and the database

These utilities are necessary to minimise code duplication 



