from configuration_data import currencies


class ConversionException(Exception):
    pass


def data_checking(entrance, exodus, factor):
    if entrance not in currencies:
        raise ConversionException(f"я {entrance} валюты не знаю")
    elif exodus not in currencies:
        raise ConversionException(f"я {exodus} валюты не знаю")
    elif entrance == exodus:
        raise ConversionException(f"надо перевести {entrance} в {exodus}?\n он же уже {exodus}!")
    elif not factor.replace(".", "").replace(",", "").isdigit():
        raise ConversionException(f"это число? - {factor}")
    elif "." in factor:
        if len(factor.split(".")) > 2:
            raise ConversionException(f"это число по какой системе? - {factor}")
    elif "," in factor:
        if len(factor.split(",")) > 2:
            raise ConversionException(f"ты в какой системе число пишешь? - {factor}")
