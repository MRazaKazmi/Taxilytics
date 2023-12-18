# Taxilytics

## Summary

The goal of this project is to automate the flow of data from a data lake into a data warehouse to power a dashboard which enables users to extract insights on the Green taxi trips made in NYC in the 2022 year.

## Dataset

The data was downloaded from https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page in parquet format and loaded into Google Cloud Storage for access by the data pipeline. 

The taxi trips table is about the Green taxi trips made in NYC and is enriched with generated data about taxi zones, payment types, rate codes and trip types from the provided data dictionary and dates using dbt. 

## Architecture

![Blank diagram (2)](https://github.com/MRazaKazmi/Taxilytics/assets/23143869/16d02999-384e-4bf7-9afb-d86e511b814a)

## Setup

### Pre-requisites
- Terraform
- Docker

### Terraform

The following steps will help you spin up the required cloud infrastructure:

1. Move into the Terraform directory

`cd terraform`

2. Initiate Terraform and download the required dependencies

`terraform init`

3. View the Terraform plan

`terraform plan`

4. Apply the cloud infrastructure

`terraform apply`

### Airflow

1. Move into Airflow directory
   
`cd airflow`
   
2. Run the Docker container
   
`docker compose up`


## Future Work

- Inlclude CI/CD pipelines
- Include more data quality checks
- Add data visualizations to present insights from the data
