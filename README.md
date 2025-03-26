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

## Step 3: Data Quality Assessment

Following the data exploration phase, I have implemented comprehensive data quality checks to validate the integrity of the datasets. 

### Quality Check Framework

- **Basic Quality Metrics**: Identifies duplicates, missing values, and verifies data types across all tables
- **Cross-Referenced Validation**: Ensures relationships between tables are valid and consistent
- **Logical Consistency**: Verifies that dates follow a logical sequence (e.g., submission date before interview date)

### KPI-Critical Outlier Detection 

I added specific outlier detection for fields critical to the dashboard KPIs:

- **Number of Active Vacancies**: Identified outliers in NUMBER_OF_OPENINGS
- **Time to Fill:**: Detected statistically significant outliers in requisition time-to-fill calculations
- **Conversion Rates**: Found unusual submission-to-interview and interview-to-hire times that may skew conversion metrics

### Candidate Pipeline Validation 

- **Status Logic**: Enhanced verification of candidate status progression
- **Date Sequence Validation**: Ensured all pipeline stage dates follow logical progression

## 4. Data Cleaning

The data cleaning process focused on four main tables: requisitions, candidate, candidate_status, and department. Each table underwent specific cleaning steps to ensure data quality while preserving original information through flagging rather than modification.

### Requisitions Table Cleaning

1. **Missing Value Handling**
   - RECRUITER field (30.6% missing)
     - Used RECRUITER_ID mapping to fill missing values where possible
     - Remaining missing values flagged for analysis
   - CLOSE_DATE (5.9% missing)
     - Cross-validated with STATUS_IN field
     - Missing close dates for 'Open' status maintained
     - Corrected STATUS_IN where inconsistent

2. **Data Validation**
   - Flagged requisitions with more than 10 openings for review
   - Identified and flagged invalid date sequences (close date before open date)
   - Added time-to-fill calculations and outlier detection using IQR method

### Candidate Table Cleaning

1. **Basic Cleaning**
   - Removed duplicate records
   - Standardized date formats across all date columns
   - Flagged missing CANDIDATE_ID values

2. **Timeline Validation**
   - Identified illogical date sequences
   - Added flags for:
     - Status dates before submission
     - Interview timing outliers
     - Hire timing outliers

3. **Status Progression**
   - Implemented status order validation
   - Created flags for invalid progression paths
   - Special handling for terminal statuses (Rejected/Withdrawn)

### Candidate Status Table Cleaning

1. **Duplicate Management**
   - Removed duplicate status values
   - Preserved unique status definitions

2. **Stage Mapping**
   - Filled missing stage mappings with 'Unknown'
   - Maintained relationship between status and stages

## Cleaning Approach 
The cleaning process followed these principles:
1. Preserve original data where possible
2. Flag issues rather than modify data
3. Document all changes and anomalies
4. Enable traceability of data quality issues
5. Maintain relationships between tables