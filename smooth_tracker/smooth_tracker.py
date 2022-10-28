from typing import Union

import numpy as np

from .filters.fading import FadingFilter

Value = Union[float, np.ndarray]


class SmoothTracker:
    def __init__(self, **kwargs):
        self.filter = FadingFilter(**kwargs)

    def update(self, value: Value):
        value = self.format_input(value)
        prediction = self.filter(value)
        return prediction

    def format_input(self, value: Value):
        if isinstance(value, (list, tuple)):
            return np.array(value)
        return value
