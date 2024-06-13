from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.amazon.aws.hooks.redshift_sql import RedshiftSQLHook
from datetime import datetime, timedelta
import requests

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'load_country_info',
    default_args=default_args,
    description='Load country info from RestCountries API to Redshift',
    schedule_interval='30 6 * * 6',
    start_date=datetime(2024, 5, 1),
    catchup=False
)

def fetch_country_data():
    url = 'https://restcountries.com/v3/all'
    response = requests.get(url)
    countries = response.json()
    extracted_data = []

    for country in countries:
        country_info = {
            'country': country.get('name', {}).get('official', ''),
            'population': country.get('population', 0),
            'area': country.get('area', 0.0)
        }
        extracted_data.append(country_info)

    return extracted_data

def load_data_to_redshift(**context):
    data = context['task_instance'].xcom_pull(task_ids='fetch_country_data')
    redshift_hook = RedshiftSQLHook(redshift_conn_id='redshift_default')

    create_table_sql = """
    CREATE TABLE IF NOT EXISTS public.country_info (
        country VARCHAR(256),
        population BIGINT,
        area FLOAT
    );
    """

    delete_sql = "DELETE FROM public.country_info;"

    insert_sql = """
    INSERT INTO public.country_info (country, population, area)
    VALUES (%s, %s, %s);
    """

    redshift_hook.run(create_table_sql)
    redshift_hook.run(delete_sql)

    for record in data:
        redshift_hook.run(insert_sql, parameters=(record['country'], record['population'], record['area']))

fetch_task = PythonOperator(
    task_id='fetch_country_data',
    python_callable=fetch_country_data,
    dag=dag
)

load_task = PythonOperator(
    task_id='load_data_to_redshift',
    python_callable=load_data_to_redshift,
    provide_context=True,
    dag=dag
)

fetch_task >> load_task
