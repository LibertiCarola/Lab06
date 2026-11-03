import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    def mostra_strumenti(self, e):
        lista_strum = self._model.get_strumenti()
        # print('funziona')
        if lista_strum is not None:
            self._view.lista_strumenti.controls.clear()
            for strum in lista_strum:
                self._view.lista_strumenti.controls.append(ft.Text(f'{strum}'))
            self._view.update()
        else:
            print('si è verificato un errore nella lettura del database')


    def pulsante_cerca_per_tipo(self, e):
        self._view.lista_strumenti_ricerca.controls.clear()
        tipo_st = self._view.input_tipo_strumento.value
        T = tipo_st[0].upper()
        tipo_strumento = T + tipo_st[1:]
        lista_strum = self._model.get_strumenti()
        for strumento in lista_strum:
            if tipo_strumento in strumento.tipo:
                self._view.lista_strumenti_ricerca.controls.append(ft.Text(f'{strumento}'))
        self._view.update()




