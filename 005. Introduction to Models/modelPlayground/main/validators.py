from django.core.exceptions import ValidationError

def validateAgeEven(value):
    if(value % 2):
        raise ValidationError(message="Given value is not even")