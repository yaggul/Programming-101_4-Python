import json


class JsonOperator:

    def __init__(self):
        self._json_cars = {}
        self._json_in = {}
        self._json_out = {}

    def json_cars_input(self):
        with open('./cars.json', 'r')as carsin:
            temp_data = json.load(carsin)
        self._json_cars = {l['name']: [l['car'], l['model'], l['max_speed']] for l in [v for k, v in temp_data.items()][0]}

    def json_result_input(self):
        with open('./result.json', 'r') as resultin:
            self._json_in = json.load(resultin)

    def json_result_output(self):
        with open('./result.json', 'w') as resultout:
            json.dump(self._json_in, resultout)

    def __getitem__(self, index):
        return self._json_cars[index]
