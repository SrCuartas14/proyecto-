import mysql.connector
from tkinter import messagebox


def execute_query(db_config, query, params=None):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        if query.strip().upper().startswith("SELECT"):
            result = cursor.fetchall()
        else:
            connection.commit()
            result = None

        return result
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error de base de datos: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def insert_record(db_config, table_name, columns, values):
    query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(values))})"
    execute_query(db_config, query, tuple(values))


def update_record(db_config, table_name, columns, values, record_id):
    query = f"UPDATE {table_name} SET {', '.join([f'{col} = %s' for col in columns])} WHERE id = %s"
    execute_query(db_config, query, tuple(values) + (record_id,))


def delete_record(db_config, table_name, record_id):
    query = f"DELETE FROM {table_name} WHERE id = %s"
    execute_query(db_config, query, (record_id,))


def load_data(db_config, table_name):
    query = f"SELECT * FROM {table_name}"
    return execute_query(db_config, query)


def search_by_id(db_config, table_name, record_id):
    query = f"SELECT * FROM {table_name} WHERE id = %s"
    return execute_query(db_config, query, (record_id,))