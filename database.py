from datetime import datetime
import sqlite3
import sys

from utility import update_error_log_transactions


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except:
        update_error_log_transactions('db', sys.exc_info())

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except:
        update_error_log_transactions('db', sys.exc_info())


def get_case_numbers(conn, get_cases_sql):
    try:
        c = conn.cursor()
        c.execute(get_cases_sql)
        case_numbers_tuple = c.fetchall()
        case_numbers = [tuple[0] for tuple in case_numbers_tuple]
        return case_numbers
    except sqlite3.OperationalError as e:
        return ['']
    finally:
        update_error_log_transactions('db', sys.exc_info())


def insert_new_cases_into_local_db(conn, insert_into_table_sql, cases_list):
    try:
        c = conn.cursor()
        c.executemany(insert_into_table_sql, cases_list)
        with open('log/imports.txt', 'a') as f:
            f.write('{}: Successfully imported {}\n\n'.format(datetime.now(), cases_list))
    except:
        update_error_log_transactions('db', sys.exc_info())


def commit_and_close(conn):
    try:
        conn.commit()
        conn.close()
    except:
        update_error_log_transactions('db', sys.exc_info())
