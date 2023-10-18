import json


class Importer:

    def __init__(self):
        pass

    def read_tasks(self):
        # TODO odczytaj plik i zdekoduj treść tutaj
        with open('taski.json') as f:
            return json.load(f)

    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj
        return self.read_tasks()
