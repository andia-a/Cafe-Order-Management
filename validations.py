def is_valid_name(name: str) -> bool:
    name = name.strip()
    name_parts = name.split()

    match len(name_parts):
        case 1:
            length = 3
        case 2:
            length = 6
        case 3:
            length = 9
        case _:
            length = None

    name_joined = "".join(name_parts)
    if (
            length
            and len(name_joined) >= length
            and name_joined.isalpha()
    ):
        return True
    raise ValueError


def is_valid_phone_num(phone_number: str) -> bool:
    if phone_number.startswith("+98"):
        phone_number = phone_number.replace("+98", "0")
    main_num = phone_number
    national_code = ("0996", "0994", "0993", "0992", "0991", "0990", "0910",
                     "0938", "0937", "0936", "0935", "0939", "0930", "0933",
                     "0900", "0901", "0902", "0903", "0920", "0921", "0922",
                     "0923")
    phone_number = phone_number[:4:]
    if (
            phone_number in national_code
            and len(main_num) == 11
            and main_num.isnumeric()
    ):
        return True
    raise ValueError


def is_valid_choice(choice: list[str], options: dict[str, str]) -> bool:
    is_valid = []

    for item in choice:
        if item in options:
            is_valid.append(True)
        else:
            is_valid.append(False)

    if all(is_valid):
        return True
    raise ValueError
