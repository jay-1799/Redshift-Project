---

# Redshift Project

## Introduction

This project is aimed at building an ETL pipeline to extract data from S3, stage it in Redshift, and transform it into a set of dimensional tables for the analytics team at Sparkify, a music streaming startup. The data consists of JSON logs on user activity and JSON metadata on the songs in the app.

## Project Structure

- `create_tables.py`: This script drops old tables (if they exist) and re-creates new tables in Redshift.
- `etl.py`: This script orchestrates the ETL process, loading data from S3 into staging tables in Redshift and then inserting it into the final dimensional tables.
- `sql_queries.py`: This file contains SQL queries for creating tables, copying data from S3 to Redshift, and inserting data into the final tables.
- `dhw.cfg`: This configuration file contains information about AWS resources such as Redshift cluster, IAM role, and S3 paths.

## Data Sources

- **Songs data**: s3://udacity-dend/song_data
- **Events data**: s3://udacity-dend/log_data
- **Descriptor file for events**: s3://udacity-dend/log_json_path.json

## Schema Definition

### Staging Tables

- `staging_songs`
- `staging_events`

### Dimension Tables

- `users`
- `songs`
- `artists`
- `time`

### Fact Table

- `songplays`

## Setup and Running the Project

### Prerequisites

- Python 3
- Required Python packages: `psycopg2-binary`, `configparser`
- AWS Redshift cluster
- IAM role with S3 read access

### Steps

1. **Clone the repository and navigate to the project directory.**

   ```sh
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Install required packages.**

   ```sh
   pip install psycopg2-binary configparser
   ```

3. **Update `dhw.cfg` with your AWS credentials and configuration.**

4. **Run `create_tables.py` to create the tables in Redshift.**

   ```sh
   python create_tables.py
   ```

5. **Run `etl.py` to load data from S3 into staging tables and then insert it into the final tables.**
   ```sh
   python etl.py
   ```
