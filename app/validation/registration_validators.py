from email_validator import validate_email, EmailNotValidError
from app.validation.password_validation import PasswordValidator

class CommonValidators:
    @staticmethod
    def validate_email(email):
        try:
            validate_email(email)
        except EmailNotValidError as e:
            raise ValueError(str(e))
        return email

    @staticmethod
    def validate_password(password):
        password_validator = PasswordValidator(password)
        if not password_validator.is_valid():
            error_message = password_validator.get_error_message()
            raise ValueError(error_message)
        return password