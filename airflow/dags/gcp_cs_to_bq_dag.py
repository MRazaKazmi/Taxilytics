from fileinput import filename
import os

from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateExternalTableOperator


GCP_PROJECT_ID = os.environ.get('GCP_PROJECT_ID', 'taxilytics')
GCP_GCS_BUCKET = os.environ.get('GCP_GCS_BUCKET', 'taxilytics_data_lake')
PATH_TO_AIRFLOW_HOME = os.environ.get('AIRFLOW_HOME', '/opt/airflow')
BIGQUERY_DATASET = os.environ.get('BIGQUERY_DATASET', 'stg')
BIG_QUERY_TABLE_NAME = 'green_taxi_trips'


default_args = {
    'owner' : 'airflow',
    'retries' : 1,
    'retry_delay' : timedelta(minutes=1)
} 

with DAG(
    dag_id='gcp_cs_to_bq_dag',
    default_args=default_args,
    description="gcp_cs_to_bq_dag",
    schedule_interval="@daily",
    start_date=datetime(2023,12,11),
    catchup=False,
    tags=['dtc-de-dags']
) as dag:


    create_external_table_task = BigQueryCreateExternalTableOperator(
    task_id="create_external_table",
    gcp_conn_id='google_cloud_default',
    table_resource={
        "tableReference": {
            "projectId": GCP_PROJECT_ID,
            "datasetId": BIGQUERY_DATASET,
            "tableId": BIG_QUERY_TABLE_NAME,
        },
        "externalDataConfiguration": {
            "sourceFormat": "PARQUET",
            "sourceUris": [f'gs://{GCP_GCS_BUCKET}/raw/green_tripdata/*'],
        },
    },
    )

    create_external_table_task