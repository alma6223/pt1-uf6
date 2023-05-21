from sqlite import SQLite
from dni import DNI

def check_dnis(con, cur):
    """
    Checks the validity of DNIs in the 'DNIs_origen_AM' table.
    Moves valid DNIs to 'DNIs_correctos_AM' table, corrects and moves invalid DNIs to 'DNIs_corregidos_AM' table,
    and deletes invalid DNIs from 'DNIs_origen_AM' table.
    Finally, displays the contents of 'DNIs_correctos_AM' and 'DNIs_corregidos_AM' tables.

    Parameters:
    - con: SQLite database connection object.
    - cur: SQLite database cursor.
    """
    for row in SQLite.select(cur, 'DNIs_origen_AM'):
        if DNI.letter(row[0]) == row[1]:
            SQLite.insert(con, cur, 'DNIs_correctos_AM', row[0], row[1])
        else:
            SQLite.insert(con, cur, 'DNIs_corregidos_AM', row[0], DNI.letter(row[0]))
            SQLite.delete(con, cur, 'DNIs_origen_AM', 'A')
    display_tables(cur, 'DNIs_correctos_AM')
    display_tables(cur, 'DNIs_corregidos_AM')

def create_tables(cur):
    """
    Creates necessary tables in the database.

    Parameters:
    - cur: SQLite database cursor.
    """
    tables = ['DNIs_origen_AM', 'DNIs_origen2_AM', 'DNIs_correctos_AM', 'DNIs_corregidos_AM','DNIs_ordenados_AM']
    for table in tables:
        SQLite.table(cur, table)

def dictionary_inserts(con, cur):
    """
    Inserts DNIs and their corresponding letters from the 'dni.csv' file into 'DNIs_origen_AM' and 'DNIs_origen2_AM' tables.

    Parameters:
    - con: SQLite database connection object.
    - cur: SQLite database cursor.
    """
    for digits, letter in DNI.dictionary('dni.csv').items():
        SQLite.insert(con, cur, 'DNIs_origen_AM', digits, letter)
        SQLite.insert(con, cur, 'DNIs_origen2_AM', digits, letter)
    display_tables(cur, 'DNIs_origen_AM')

def sort_inserts(con, cur):
    """
    Sorts the DNIs in 'DNIs_correctos_AM' and 'DNIs_corregidos_AM' tables and inserts them into 'DNIs_ordenados_AM' table.

    Parameters:
    - con: SQLite database connection object.
    - cur: SQLite database cursor.
    """
    for row in sorted(SQLite.select(cur, 'DNIs_correctos_AM') + SQLite.select(cur, 'DNIs_corregidos_AM')):
        SQLite.insert(con, cur, 'DNIs_ordenados_AM', row[0], row[1])
    display_tables(cur, 'DNIs_ordenados_AM')

def update_dnis(con, cur):
    """
    Updates the 'DNIs_origen2_AM' table with corrected letters for invalid DNIs.

    Parameters:
    - con: SQLite database connection object.
    - cur: SQLite database cursor.
    """
    for row in SQLite.select(cur, 'DNIs_origen2_AM'):
        if DNI.letter(row[0]) != row[1]:
            SQLite.update(con, cur, 'DNIs_origen2_AM', row[0], DNI.letter(row[0]))
    display_tables(cur, 'DNIs_origen2_AM')

def display_tables(cur, table):
    """
    Displays the contents of a specific table.

    Parameters:
    - cur: SQLite database cursor.
    - table: The name of the table to display.
    """
    print(table)
    for row in SQLite.select(cur, table):
        print(row[0], row[1], sep='-')

