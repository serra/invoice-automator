from jinja2 import Environment, FileSystemLoader
from decimal import Decimal, ROUND_HALF_UP


def currency_format(value, symbol="€"):
    try:
        # Convert to Decimal and round using ROUND_HALF_UP strategy
        decimal_value = Decimal(str(value)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        # Format with thousand separators
        money = "{:,.2f}".format(decimal_value)
        money = money.replace(",", " ").replace(".", ",")
        return f"{symbol} {money}"
    except (ValueError, TypeError):
        return value


env = Environment(loader=FileSystemLoader("templates"))
env.filters["currency"] = currency_format


def get_template(template_name):
    return env.get_template(template_name)
