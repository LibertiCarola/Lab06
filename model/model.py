from importlib.metadata import pass_none

from database.DB_connect import get_connection      # installazione connettore
from model.strumento import Strumento               # abbiamo importato la classe Strumento
from model.prestito import Prestito                 # abbiamo importato la classe Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:  # indica che è caldamente consigliato salvare le info del
                                                        # database come lista di oggetti della classe Strumento
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        lista_strumenti = []
        try:
            connessione = get_connection()      # stabiliamo connessione con database attraverso la funzione in DB_connect
                                                # questa connessione da ora permette un dialogo costante con il database
            cursore = connessione.cursor(dictionary=True)       # il cursore scorre le righe attraverso la connessione
            query = 'SELECT * FROM strumento'                   # la query seleziona i campi interessanti
            cursore.execute(query)                              # il cursore è un CONTENITORE DI RIGHE

            for riga in cursore: # ottengo una serie di dizionari (codice = '', tipo = '', marca, anno, prezzo)         #ricordati di aggiornare se non esiste lo strumento e viceversa
                strum = Strumento(riga['codice'],
                                  riga['tipo'],
                                  riga['marca'],
                                  riga['anno_acquisto'],
                                  riga['valore'])
                lista_strumenti.append(strum)
            cursore.close()
            return lista_strumenti
        except:
            return None


    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        try:
            pass

        except:
            return None
