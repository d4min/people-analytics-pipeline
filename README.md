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

## Step 2: Data Exploration and Understanding

This step focuses on exploring and understanding the dataset structure. Particularly focusing on the relationships between tables and department hierarchy:

- **Requisition-Candidate Relationship**:

    - 4,624 requisitions have candidates associated with them
    - 229 requisitions have no candidates, all of which are closed requisitions
    - The number of candidates per requisition varies widely (from 1 to over 4,000)

- **Department Hierarchy Structure**;

    - Identified 2 Region departments (e.g., "Region X - SD")
    - Found 22 Area departments (e.g., "Area X - SD")
    - Remaining 368 departments appear to be store-level (e.g., "0717 - SD")
    - All departments have a parent, confirming a complete hierarchical structure
    - Store departments have Area parents, and Areas have Region parents
