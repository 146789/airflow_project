from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


def hello_world_py(*arga. **kwargs):
    print("hello world from pythonOperator")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(-dag
    'dummy_dag',
    default_args=default_args,
    description='A dummy dag',
    schedule_interval=None,
    catchup=False,
    tags=['dev']
)

t1 = BashOperator(
    task_id = 'bash_hellow',
    bash_command='echo "hello owrld from bash operator"',
    dag=dag,
)

t2 = PythonOperator(
    task_id = 'Pythion_hello',
    python_callable=hello_world_py,
    dag=dag
)

t1 >> t2