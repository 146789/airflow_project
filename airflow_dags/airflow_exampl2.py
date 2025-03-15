from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {

    "onwer": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

dag  = DAG(
    "dag_for_parallel_jobs",
    default_args=default_args,
    description="My Frist dag",
    schedule_interval= "*/2 * * * *",
    start_date=datetime(2024, 12, 15),
    catchup=False,
    tags=['dev']
)

start_task = BashOperator(task_id="start_task", bash_command='echo "start task"', dag=dag)

parallel_task_1 = BashOperator(task_id="parallel_task_1", bash_command='echo "parallel task1"', dag=dag)
parallel_task_2 = BashOperator(task_id="parallel_task_2", bash_command='echo "parallel task2"', dag=dag)
parallel_task_3 = BashOperator(task_id="parallel_task_3", bash_command='echo "parallel task3"', dag=dag)

end_task = BashOperator(task_id="end_task", bash_command='echo "end task"', dag=dag)

start_task >> [parallel_task_1, parallel_task_2, parallel_task_2] >> end_task
