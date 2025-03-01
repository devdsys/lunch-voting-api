import re
from typing import Optional

class PasswordValidator:
    def __init__(self, password: str):
        self.password = password

    def is_valid(self) -> bool:
        return (
            self._has_minimum_length()
            and self._has_at_least_one_number()
            and self._has_at_least_one_special_character()
        )

    def _has_minimum_length(self) -> bool:
        return len(self.password) >= 8

    def _has_at_least_one_number(self) -> bool:
        return any(char.isdigit() for char in self.password)

    def _has_at_least_one_special_character(self) -> bool:
        return bool(re.search(r"[^A-Za-z0-9]", self.password))

    def get_error_message(self) -> Optional[str]:
        if not self._has_minimum_length():
            return "Password must be at least 8 characters long"
        if not self._has_at_least_one_number():
            return "Password must contain at least one number"
        if not self._has_at_least_one_special_character():
            return "Password must contain at least one special character"
        return None