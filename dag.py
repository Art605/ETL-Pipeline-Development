from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.providers.google.cloud.operators.datafusion import CloudDataFusionStartPipelineOperator

# Default for DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 12, 18),
    'depends_on_past': False,
    'email': ['arthi1805@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Defining the DAG
dag = DAG('employee_data',
          default_args=default_args,
          description='Runs an external Python script and starts Cloud DataFusion pipeline',
          schedule_interval='@daily',  
          catchup=False) 

with dag:
    # BashOperator to run a Python script
    run_script_task = BashOperator(
        task_id='extract_data',
        bash_command='python/opt/airflow/dags/extract.py', 
    )

    # Cloud DataFusion task to start a pipeline
    start_pipeline = CloudDataFusionStartPipelineOperator(
        location="us-central1",
        pipeline_name="etl-pipeline",
        instance_name="datafusion-dev",
        task_id="start_datafusion_pipeline",
    )

    # Setting dependencies
    run_script_task >> start_pipeline
