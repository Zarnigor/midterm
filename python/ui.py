from colorama import Fore, init

init(autoreset=True)

def get_car_type_ui(cars):
    print(Fore.YELLOW + "Mashina turlari:")
    for idx, car in cars.items():
        print(Fore.CYAN + f"{idx}. {car['type']}")
    print(Fore.RED + "0. Chiqish")

    while True:
        try:
            car_type = int(input(Fore.GREEN + "Moshina turini tanlang: "))
            if car_type == 0:
                print(Fore.RED + "Dasturdan chiqilmoqda...")
                exit()
            elif 1 <= car_type <= len(cars):
                return car_type
            else:
                print(Fore.RED + "Bunday turdagi avtomobil mavjud emas.")
        except ValueError:
            print(Fore.RED + "Iltimos, raqam kiriting.")

def get_car_model_ui(car_type, cars):
    car_models = cars[str(car_type)]["models"]
    print(Fore.YELLOW + f"{cars[str(car_type)]['type']} modellari:")
    for idx, model in enumerate(car_models, 1):
        print(Fore.CYAN + f"{idx}. {model['name']} - ${model['price']}")
    print(Fore.RED + "0. Ortga qaytish")

    while True:
        try:
            model_choice = int(input(Fore.GREEN + "Modelni tanlang: "))
            if model_choice == 0:
                return None
            elif 1 <= model_choice <= len(car_models):
                return car_models[model_choice - 1]
            else:
                print(Fore.RED + "Bunday model mavjud emas.")
        except ValueError:
            print(Fore.RED + "Iltimos, raqam kiriting.")

def get_car_color_ui(colors):
    print(Fore.YELLOW + "Rang tanlash:")
    for idx, color in colors.items():
        print(Fore.CYAN + f"{idx}. {color[0]} - ${color[1]}")
    print(Fore.RED + "0. Ortga qaytish")

    while True:
        try:
            color_choice = int(input(Fore.GREEN + "Rangni tanlang: "))
            if color_choice == 0:
                return None
            elif 1 <= color_choice <= len(colors):
                return color_choice
            else:
                print(Fore.RED + "Bunday rang mavjud emas.")
        except ValueError:
            print(Fore.RED + "Iltimos, raqam kiriting.")
