from dni import DNI
from sqlite import SQLite
import app

def main():
    # Establishes a connection to the SQLite database
    con, cur = SQLite.connection('pt1_uf6.db')

    # Creates necessary tables in the database
    app.create_tables(cur)

    # Inserts DNIs and their corresponding letters into the tables
    app.dictionary_inserts(con, cur)

    # Checks the validity of DNIs and performs necessary operations
    app.check_dnis(con, cur)

    # Sorts and inserts DNIs into 'DNIs_ordenados_AM' table
    app.sort_inserts(con, cur)

    # Updates incorrect DNIs in 'DNIs_origen2_AM' table
    app.update_dnis(con, cur)

if __name__ == '__main__':
    main()










