from django.core.exceptions import ValidationError


def validate_satisfaction_range(value):
    if not (0 <= value <= 10):
        raise ValidationError(f"{value} is not between 0 and 10!")
