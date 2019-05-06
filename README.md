# Data Warehouse with Redshift: Song Play Analysis
> José Luis Gil Aguilar
## Project Summary

This ETL Pipeline was designed for a startup **Sparkify**, who wants to analyze the data comming from their songs and user activity on their new music streaming app. This project creates a star-schema database using Amazon Redshift from a directory in S3 of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

## Files in Project
Tha main files for running the project are:

* `dwh.cfg`: which stores Redshift and S3 config 
* `sql_queries.py`: SQL scripts used in `create_tables.py` and `etl.py`
* `create_tables.py`: connects to Redshift and drop and creates tables
* `etl.py`: connects to Redshift and ingest data from S3 and insert data into fact and dimensional tables

## How to run
1. Deploy a data warehouse on Amazon Redshift using IAM Role for S3 access.
2. Configure `dwh.cfg` file with credentials and information for your Redshift connection and S3 roots.
3. Run `python create_tables.py`
4. Run `python etl.py`
