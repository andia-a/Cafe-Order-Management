from types import FunctionType
import validations
import iostream
import pprint


class Menu():
    def __init__(self, menu: dict[str, str] = None) -> None:
        self._menu = menu

    def set_menu(self, menu: dict[int | str, str] = None) -> None:
        if menu is not None:
            if isinstance(menu, dict):
                for value in menu.values():
                    if isinstance(value, str):
                        self._menu = menu
                    else:
                        raise ValueError
            else:
                raise ValueError
        else:
            self._menu = {"1": "Tea", "2": "Coffe", "3": "Cake"}

    def get_menu(self) -> dict[str, str]:
        return self._menu


class Customer():
    def __init__(
            self,
            name: str,
            phone_number: str | int = None
    ) -> None:
        self.name = name
        self.phone_number = phone_number

    def get_full_info(self) -> dict[str, str]:
        customer_info = {
            "name": self.name,
            "phone number": self.phone_number
        }
        return customer_info


class Order():
    total_orders = 0
    orders_info = {}

    def __init__(
            self,
            order: list[str],
            customer_name: str,
            price: float=None
    ) -> None:
        self.order = order
        self.customer_name = customer_name
        self.order_number = Order.total_orders + 1
        self.price = price

        Order.total_orders += 1

    def add_item(
            self,
            item: str,
            menu: dict[str, str],
            validator: FunctionType
    ) -> None:
        if validator(item, menu):
            self.order.append(menu[item])

    def show_details(self) -> None:
        print(f"Order {self.order_number} for {self.customer_name}.")
        print("Items:", *self.order)
        print("Price:", self.price)



    @classmethod
    def update_orders_info(
            cls,
            costumer_info: dict[str, str],
            order: list[str],
            price: float
    ) -> None:
        cls.orders_info.update({Order.total_orders: costumer_info})
        cls.orders_info[Order.total_orders].update({"orders": order})
        cls.orders_info[Order.total_orders].update({"price": price})


class PriceCalculator():
    tax_rate = 0.1

    def __init__(self) -> None:
        self.prices = {}
        self.order_price = None

    def set_prices(
            self,
            menu: dict[str, str],
            prices: list[float | int] = (3, 4.5, 7.2)
    ) -> None:
        if len(menu) == len(prices):
            index = 0
            for item in menu.values():
                self.prices.update({item: prices[index]})
                index += 1
        else:
            raise ValueError

    @staticmethod
    def calculate_price(
            prices: dict[str, float],
            tax_rate: float,
            order: list[str]
    ) -> float:
        price = 0

        for item in prices:
            if item in order:
                price += prices[item]

        tax = price * tax_rate
        price = price + tax

        return price

    @classmethod
    def update_tax_rate(cls) -> None:
        while True:
            new = input("Enter new tax rate: ")
            try:
                cls.tax_rate = float(new)
                break
            except ValueError:
                print("Please enter a float number")


class Manager():
    @staticmethod
    def main():
        options = {"1": "Change tax rate.",
                   "2": "Place orders.",
                   "3": "Get all orders information.",
                   "4": "Exit"}
        while True:
            iostream.print_options(options)
            validator = validations.is_valid_choice
            choice = iostream.get_choice(options, validator)

            match choice:
                case "1":
                    PriceCalculator.update_tax_rate()
                case "2":
                        menu = Menu()
                        menu.set_menu()
                        menu = menu.get_menu()
                        while True:
                            print("Welcome to my Cafe! Please enter your info to place your order:")
                            validator = validations.is_valid_name
                            customer_name = iostream.get_customer_name(validator)
                            validator = validations.is_valid_phone_num
                            customer_phone_num = iostream.get_customer_phone_number(validator)
                            customer = Customer(customer_name, customer_phone_num)

                            validator = validations.is_valid_choice
                            iostream.print_options(menu)
                            order = iostream.get_order(menu, validator)
                            order = Order(order, customer.name)

                            price = PriceCalculator()
                            price.set_prices(menu)
                            prices = price.prices
                            tax_rate = PriceCalculator.tax_rate
                            price = PriceCalculator.calculate_price(prices, tax_rate, order.order)
                            order.price = price


                            Order.update_orders_info(customer.get_full_info(), order.order, price)
                            order.show_details()

                            repeat = input("Do you want to place another order? (y/n): ")
                            if repeat == "y":
                                continue
                            break
                case "3":
                    pprint.pprint(Order.orders_info)
                case "4":
                    break
                case _ :
                    print("Please enter a valid choice.")



if __name__ == "__main__":
    Manager.main()




