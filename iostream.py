from types import FunctionType


def get_customer_name(
        validator: FunctionType,
        prompt: str = "Name: "
) -> str:
    while True:
        try:
            name = input(prompt)
            if validator(name):
                return name
        except ValueError:
            print("Please enter a valid name.")


def get_customer_phone_number(
        validator: FunctionType,
        phone_number_type=str,
        prompt: str = "Phone number: "
) -> str | int:
    while True:
        try:
            phone_number = input(prompt)
            if validator(phone_number):
                return phone_number_type(phone_number)
        except ValueError:
            print("Please enter a valid phone number.")


def get_order(
        menu: dict[str, str],
        validator: FunctionType,
        error: str = "Your order is not valid.",
        prompt: str =
        "Please enter your order (split them with spaces): "
) -> list[str]:
    while True:
        try:
            order = input(prompt)
            order = order.split(" ")
            if validator(order, menu):
                orders = []
                for item in order:
                    orders.append(menu[item])
                return orders
        except ValueError:
            print(error)


def get_choice(
        options: dict[str, str],
        validator: FunctionType,
        error: str = "Your choice is not valid.",
        prompt: str = "Please enter your choice: "
) -> str:
    while True:
        try:
            choice = input(prompt)
            if validator(choice, options):
                return choice
        except ValueError:
            print(error)


def print_options(options: dict[str, str]) -> None:
    print()
    for key, value in options.items():
        print(f"{key}: {value}")
