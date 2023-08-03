import pint
from pint import UndefinedUnitError
from django.core.exceptions import ValidationError
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def validate_unit_of_measure(value):
    ureg = pint.UnitRegistry()
    ureg.load_definitions(BASE_DIR / 'my_def.txt')
    try:
        single_unit = ureg[value]
    except UndefinedUnitError as e:
        raise ValidationError(f"{value} is not a valid unit of measure")
    except:
        raise ValidationError(f"'{value}' is invaild")
