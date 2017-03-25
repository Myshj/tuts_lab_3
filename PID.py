class PID(object):
    def __init__(
            self,
            proportional: float,
            integral: float,
            differential: float,
            period: float,
            min_value: float,
            max_value: float,
            formula: str
    ):
        self.proportional = proportional
        self.integral = integral
        self.differential = differential
        self.period = period
        self.min_value = min_value
        self.max_value = max_value

        self._last_sum = 0.0
        self._last_input = 0.0

        self.formula = formula

    def next_value(self, x: float):
        sum = self._last_sum + self.integral * self.period * x
        diff = self.differential / self.period * (x - self._last_input)
        prop = self.proportional * x

        result = 0.0
        if 'p' in self.formula:
            result += prop
        if 'i' in self.formula:
            result += sum
        if 'd' in self.formula:
            result += diff

        # result = prop * x + sum + diff

        result = min(result, self.max_value)
        result = max(result, self.min_value)

        self._last_sum = sum
        self._last_input = x

        return result
