import sqlite3

class SQLite:
    def connection(db):
        """
        Creates a connection to the SQLite database and returns the connection object and cursor.

        Parameters:
        - db: The name or path of the database file.

        Returns:
        - con: SQLite database connection object.
        - cur: SQLite database cursor.
        """
        con = sqlite3.connect(db)
        cur = con.cursor()
        return con, cur

    def table(cur, table):
        """
        Creates a table in the database.

        Parameters:
        - cur: SQLite database cursor.
        - table: The name of the table to be created.
        """
        cur.execute(f'CREATE TABLE {table} (Digits INTEGER, Letter VARCHAR);')

    def insert(con, cur, table, digits, letter):
        """
        Inserts a new row into the table with the specified digits and letter values.

        Parameters:
        - con: SQLite database connection object.
        - cur: SQLite database cursor.
        - table: The name of the table.
        - digits: The value for the 'Digits' column.
        - letter: The value for the 'Letter' column.
        """
        cur.execute(f'INSERT INTO {table} (Digits, Letter) VALUES (?, ?);', (digits, letter))
        con.commit()

    def select(cur, table):
        """
        Retrieves all rows from the table.

        Parameters:
        - cur: SQLite database cursor.
        - table: The name of the table.

        Returns:
        - result: A list of tuples representing the selected rows.
        """
        return cur.execute(f'SELECT * FROM {table};').fetchall()

    def delete(con, cur, table, letter):
        """
        Deletes rows from the table where the 'Letter' column matches the specified letter.

        Parameters:
        - con: SQLite database connection object.
        - cur: SQLite database cursor.
        - table: The name of the table.
        - letter: The value to match in the 'Letter' column for deletion.
        """
        cur.execute(f'DELETE FROM {table} WHERE Letter = ?;', (letter))
        con.commit()

    def update(con, cur, table, digits, letter):
        """
        Updates the 'Letter' column in the table for rows where the 'Digits' column matches the specified digits.

        Parameters:
        - con: SQLite database connection object.
        - cur: SQLite database cursor.
        - table: The name of the table.
        - digits: The value to match in the 'Digits' column for updating.
        - letter: The new value for the 'Letter' column.
        """
        cur.execute(f'UPDATE {table} SET Letter = ? WHERE Digits = ?;', (letter, digits))
        con.commit()
