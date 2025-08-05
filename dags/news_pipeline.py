from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os


import app

default_args = {
    'owner': 'data-team',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'news_classification_pipeline',
    default_args=default_args,
    description='Pipeline de classification des news',
    schedule_interval=timedelta(hours=6),
    catchup=False
)

def run_keywords_classification():
    app.classify_using_keywords()

def run_llm_classification():
    app.classify_using_llm()

keywords_task = PythonOperator(
    task_id='classify_keywords',
    python_callable=run_keywords_classification,
    dag=dag
)

llm_task = PythonOperator(
    task_id='classify_llm',
    python_callable=run_llm_classification,
    dag=dag
)

keywords_task >> llm_task