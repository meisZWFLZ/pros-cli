from typing import *

from pros.common.ui.interactive.parameters.parameter import Parameter
from pros.common.ui.interactive.parameters.validatable_parameter import ValidatableParameter

T = TypeVar('T')


class OptionParameter(ValidatableParameter, Generic[T]):
    def __init__(self, initial_value: T, options: List[T]):
        super().__init__(initial_value)
        self.options = options

    def validate(self, value: Any):
        return value in self.options


class BooleanParameter(Parameter[bool]):
    def update(self, new_value):
        true_prefixes = ['T', 'Y']
        true_matches = ['1']
        v = str(new_value).upper()
        is_true = v in true_matches or any(v.startswith(p) for p in true_prefixes)
        super(BooleanParameter, self).update(is_true)


class RangeParameter(ValidatableParameter[int]):
    def __init__(self, initial_value: int, value_range: Tuple[int, int]):
        super().__init__(initial_value)
        self.value_range = value_range

    def validate(self, value: T):
        if self.value_range[0] <= value <= self.value_range[1]:
            return True
        return f'{value} is not within [{self.value_range[0]}, {self.value_range[1]}]'

    def update(self, new_value):
        super(RangeParameter, self).update(int(new_value))
