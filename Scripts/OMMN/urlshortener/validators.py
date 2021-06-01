from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
    url_validator = URLValidator()
    if "http" in value:
        new_value = value
    else:
        new_value = "http://" + value #as links without 'http' prefix can still be valid, changing the url value to accomodate this
    try:
        url_validator(new_value)
    except:
        raise ValidationError("Invalid URL for this field")
    return new_value

def validate_dot_com(value):
    if not "com" in value:
        raise ValidationError("This is not valid due to lack of trailing .com")
    return value