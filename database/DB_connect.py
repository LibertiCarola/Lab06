import mysql.connector
from mysql.connector import errorcode
import pathlib

# questa parte di codice è quasi sempre la stessa (attenzione alla porta) serve ad accedere al database

def get_connection() -> mysql.connector.connection:
    try:                              # (user='root',password='',host='localhost',port=3306,database='DepositoStrumenti')
        cnx = mysql.connector.connect(option_files=f"{pathlib.Path(__file__).parent.resolve()}/connector.cnf")
        print('ti sei collegato con successo al database :)')
        return cnx
                                                                                # se tutto funziona restituisce collegamento col database
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:                       # errore con chiavi d'accesso USERNAME o PASSWORD
            print("Something is wrong with your user name or password")
            return None
        elif err.errno == errorcode.ER_BAD_DB_ERROR:                            # database non trovato
            print("Database does not exist")
            return None
        else:                                                                   # altri tipi di errore
            print(err)
            return None
