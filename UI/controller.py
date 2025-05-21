import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza(self, e):
        distanza = int(self._view.txt_distanza.value)
        if distanza is None or distanza == "":
            self._view.create_alert("Inserire la distanza")
            return
        self._model.buildGraph(distanza)
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato!"))
        self._view.update_page()
