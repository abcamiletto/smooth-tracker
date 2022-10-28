import numpy as np


class FadingFilter:
    def __init__(self, alpha: float = 0.5, beta: float = 0.5, decay_step: int = 5):
        self.alpha = alpha
        self.beta = beta
        self.sample_time = 1
        self.decay_step = decay_step

        self.decay_counter = 0
        self.value = None
        self.dvalue = None

    def __call__(self, value: np.ndarray):
        if self.value is None and value is None:
            return None
        elif self.value is None:
            self.value = value
            self.dvalue = np.zeros_like(value)

        self.value = self.step(value)
        self.dvalue = self.dstep(value)
        return self.value

    def step(self, value):
        a, b, dt, Xn_1, dXn_1 = self.get_parameters()

        prediction = Xn_1 + dXn_1 * dt
        if value is None:
            self.decay()
            return prediction

        return a * prediction + (1 - a) * value

    def dstep(self, value):
        a, b, dt, Xn_1, dXn_1 = self.get_parameters()

        if value is None:
            return dXn_1

        return b * dXn_1 + (1 - b) * (value - Xn_1) / dt

    def get_parameters(self):
        return self.alpha, self.beta, self.sample_time, self.value, self.dvalue

    def reset(self):
        self.value = None
        self.dvalue = None

    def decay(self):
        self.decay_counter += 1
        if self.decay_counter >= self.decay_step:
            self.reset()

    def get(self):
        return self.value, self.prev_value
