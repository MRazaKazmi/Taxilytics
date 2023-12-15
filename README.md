# Taxilytics

## Summary

The goal of this project is to automate the flow of data from a data lake into a data warehouse to power a dashboard which enables users to extract insights on the Green taxi trips made in NYC in the 2022 year.

## Dataset

The data was downloaded from https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page in parquet format and loaded into Google Cloud Storage for access by the data pipeline. 

The taxi trips table is about the Green taxi trips made in NYC and is enriched with generated data about taxi zones and dates. 

## Requirements

## Architecture

![Blank diagram](https://github.com/MRazaKazmi/Taxilytics/assets/23143869/f3607d59-fd44-4407-8858-ed9ab4429ba8)


## DAG

<img width="720" alt="Screenshot 2023-12-14 at 11 14 02 PM" src="https://github.com/MRazaKazmi/Taxilytics/assets/23143869/4136d048-02a5-402b-9ee3-b26be7fe201d">
