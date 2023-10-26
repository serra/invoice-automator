from jinja2 import Environment, FileSystemLoader


def currency_format(value, symbol="€"):
    try:
        money = "{:,.2f}".format(value)
        money = money.replace(",", " ").replace(".", ",")
        return f"{symbol} {money}"
    except (ValueError, TypeError):
        return value


env = Environment(loader=FileSystemLoader("templates"))
env.filters["currency"] = currency_format


def get_template(template_name):
    return env.get_template(template_name)
