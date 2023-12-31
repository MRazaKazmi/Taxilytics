from fileinput import filename
import os
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateExternalTableOperator

AIRFLOW_HOME = os.getenv("AIRFLOW_HOME")
GCP_PROJECT_ID = os.environ.get('GCP_PROJECT_ID', 'taxilytics')
GCP_GCS_BUCKET = os.environ.get('GCP_GCS_BUCKET', 'taxilytics_data_lake')
PATH_TO_AIRFLOW_HOME = os.environ.get('AIRFLOW_HOME', '/opt/airflow')
BIGQUERY_DATASET = 'dbt_stg'
BIG_QUERY_TABLE_NAME = 'src_green_tripdata'


default_args = {
    'owner' : 'airflow',
    'retries' : 1,
    'retry_delay' : timedelta(minutes=1)
} 

with DAG(
    dag_id='data_pipeline',
    default_args=default_args,
    description="data pipeline",
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

    dbt_debug_task = BashOperator(
        task_id = "dbt_debug",
        bash_command = f"cd {AIRFLOW_HOME}/dbt && dbt deps && dbt debug --profiles-dir ."
    )

    dbt_seed_task = BashOperator(
        task_id = "dbt_seed",
        bash_command = \
            f"cd {AIRFLOW_HOME}/dbt && dbt deps && dbt seed --profiles-dir ."
    )

    dbt_run_task = BashOperator(
        task_id = "dbt_run",
        bash_command = \
            f"cd {AIRFLOW_HOME}/dbt && dbt deps && dbt run --profiles-dir ."
    )

    dbt_test_task = BashOperator(
        task_id = "dbt_test",
        bash_command = \
            f"cd {AIRFLOW_HOME}/dbt && dbt deps && dbt test --profiles-dir ."
    )

    create_external_table_task>>dbt_debug_task >> dbt_seed_task >> dbt_run_task >> dbt_test_task