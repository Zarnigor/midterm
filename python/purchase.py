import json
from ui import get_car_type_ui, get_car_model_ui, get_car_color_ui

class Purchase:
    def __init__(self, data_file):
        with open(data_file, 'r') as f:
            self.cars = json.load(f)
        self.colors = {
            1: ("Black", 200),
            2: ("White", 100),
            3: ("Gray", 300)
        }

    def calculate_price(self, model, car_color_choice):
        base_price = model['price']
        color_price = self.colors[car_color_choice][1]
        total_price = base_price + color_price
        return total_price

    def purchase_car(self):
        car_type = get_car_type_ui(self.cars)
        model = get_car_model_ui(car_type, self.cars)
        car_color_choice = get_car_color_ui(self.colors)
        total_price = self.calculate_price(model, car_color_choice)
        print(f"\\nTanlangan avtomobil: {model['name']} {self.cars[str(car_type)]['type']} ({self.colors[car_color_choice][0]})")
        print(f"Narxi: ${total_price}")
