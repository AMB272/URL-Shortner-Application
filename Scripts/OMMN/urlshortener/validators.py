from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
    url_validator = URLValidator()
    val_1_invalid = False
    val_2_invalid = False
    try:
        url_validator(value)
    except:
        val_1_invalid = True
    
    val_2_url = "http://" + value #as links without 'http' prefix can still be valid, changing the url value to accomodate this

    try:
        url_validator(val_2_url)
    except:
        val_2_invalid = True

    if val_1_invalid and val_2_invalid:
        raise ValidationError("Invalid URL for this field")
    return value

def validate_dot_com(value):
    if not "com" in value:
        raise ValidationError("This is not valid due to lack of trailing .com")
    return value