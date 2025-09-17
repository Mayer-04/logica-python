from typing import Self


class Result[T]:
    def __init__(self, value: T | None, is_success: bool, error: str | None):
        self._value = value
        self._is_success = is_success
        self._error = error

    @property
    def value(self) -> T | None:
        return self._value

    @property
    def is_success(self) -> bool:
        return self._is_success

    @property
    def error(self) -> str | None:
        return self._error

    @classmethod
    def success(cls, value: T) -> Self:
        return cls(value=value, is_success=True, error=None)

    # @staticmethod
    # def success(value: T) -> "Result[T]":
    #     return Result(value=value, is_success=True, error=None)

    @classmethod
    def failure(cls, error: str) -> Self:
        return cls(value=None, is_success=False, error=error)

    # @staticmethod
    # def failure(error: str) -> "Result[T]":
    #     return Result(value=None, is_success=False, error=error)

    def __repr__(self) -> str:
        if self.is_success:
            return f"Result.success({self.value!r})"
        else:
            return f"Result.failure({self.error!r})"
