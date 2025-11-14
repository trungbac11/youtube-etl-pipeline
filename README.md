![image](https://github.com/user-attachments/assets/4ec4f2c3-a461-46c8-8f1f-aaf9a3839644)

# AI Usage Documentation

This document describes how AI was used to complete the self-serve metrics system assignment.

| Prompt Goal | Example Prompt | AI Response Summary | How You Used or Modified It | What You Learned / Observed |
|-------------|----------------|---------------------|----------------------------|----------------------------|
| [Example] Draft YAML validation logic | "Write a Python function that checks if a YAML file includes keys: metric_name, description, schedule, sql." | Generated a working outline but used PyYAML incorrectly. | Took structure, fixed import errors, added exception handling. | AI was good at scaffolding but needed correction for YAML edge cases. |
| [Example] Debug SQL syntax in DuckDB | "Why does DuckDB fail on `DATE('2023-09-01')` in a WHERE clause?" | Explained DATE syntax differences and suggested using `DATE '2023-09-01'`. | Applied change directly to query. | AI was accurate; learned DuckDB's date literal format. |

# SELF-SERVING-CUSTOMER-METRICS

A lightweight prototype system that allows Data Analysts to define customer metrics using YAML + SQL, with automatic materialization in DuckDB.

## Setup instructions
### Prerequisites
- Python 3.12+
- pip package manager

### Installation Steps
1. **Download the project files**

2. **Create virtual enviroments**
- python -m venv venv

3. **Active**
- source venv/bin/activate

4. **Install dependencies:**
- pip install --upgrade pip
- pip install -r requirements.txt

5. **Prepare data files:**
Place "customers.csv", "orders.csv", and "order_items.csv" in the data/ directory

6. **Initialize the database:**
- python src/setup_database.py

7. **Verify setup:**
- python src/validate_yaml.py

## How to add a new metric
**Step 1: Create YAML Metric Definition**
- Create a new .yaml file in the metrics/ directory with this structure

**Step 2: Validate the Metric**
- Run validation to check for errors: python src/validate_yaml.py

**Step 3:  Execute the Metric**
- Run the metric to create the table in DuckDB: python src/run_metrics.py

**This will:**
- Read all YAML files from /metrics
- Execute each SQL query against DuckDB
- Create or replace tables named after each metric


## Development guideline

### Project Structure
project/
├── data/                   # Source CSV files
├── metrics/               # Metric definitions (YAML)
│   ├── lifetime_revenue.yaml
│   ├── avg_order_revenue.yaml
│   └── customer_geography.yaml
├── src/                   # Python scripts
│   ├── validate_yaml.py   # YAML validation
│   ├── run_metrics.py     # Metric execution
│   ├── setup_database.py  # DB initialization
│   └── cleanup_database.py # DB cleanup
├── requirements.txt       # Dependencies
├── README.md              # Documentation
└── AI_USAGE.md            # AI collaboration documentation


### Testing Procedures

#### Database Setup Test:
`python src/setup_database.py`

#### Validation Test:
`python src/validate_yaml.py`

#### Execution Test:
`python src/run_metrics.py`

#### Cleanup Test:
`python src/clean_database.py`

### Test Cases
#### Validation Test Cases
- Test with missing required fields

- Test with invalid YAML syntax

- Test with malformed SQL queries

- Test with valid complete metric definitions

#### Error Handling
- All scripts include try-catch blocks for proper error handling

- Validation provides clear error messages for debugging

- Execution script continues processing other metrics if one fails

#### Maintenance
- Regular dependency updates: `pip install -r requirements.txt --upgrade`

- Database cleanup when needed: `python src/cleanup_database.py`

- Backup important data before major changes
