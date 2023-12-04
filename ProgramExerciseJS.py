class FoodOrder:
    def __init__(self, food, amount):
        self._food_name = None
        self._amount_in_pounds = None
        self._standard_price_per_pound = None
        self._calculated_price = None

        self._update_food_name(food)
        self._update_amount(amount)
        self._set_standard_price()

    def _update_food_name(self, food):
        self._food_name = food

    def _update_amount(self, amount):
        self._amount_in_pounds = amount

    def _set_standard_price(self):
        if self._food_name == 'Dry Cured Iberian Ham':
            self._standard_price_per_pound = 177.80
        elif self._food_name == 'Matsutake Mushrooms':
            self._standard_price_per_pound = 272.00
        elif self._food_name == 'Kopi Luwak Coffee':
            self._standard_price_per_pound = 306.50
        elif self._food_name == 'White Truffles':
            self._standard_price_per_pound = 3600.00
        elif self._food_name == 'Le Bonnotte Potatoes':
            self._standard_price_per_pound = 270.81
        elif self._food_name == 'Wagyu Steaks':
            self._standard_price_per_pound = 450.00
        elif self._food_name == 'Moose Cheese':
            self._standard_price_per_pound = 487.20
        elif self._food_name == 'Blue Fin Tuna':
            self._standard_price_per_pound = 3603.00
        else:
            self._standard_price_per_pound = 0.00

    def PriceListJS(self):
        print(f"Price per pound for {self._food_name}: ${self._standard_price_per_pound:.2f}")

    def calculate_cost(self):
        self._calculated_price = self._amount_in_pounds * self._standard_price_per_pound
        return self._calculated_price

    def get_food_name(self):
        return self._food_name

    def get_amount_in_pounds(self):
        return self._amount_in_pounds

    def get_standard_price_per_pound(self):
        return self._standard_price_per_pound

    def get_calculated_price(self):
        return self._calculated_price
